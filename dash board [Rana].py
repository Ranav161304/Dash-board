import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Read Data 
df = pd.read_csv(r"C:\Users\Rana\Downloads\KaggleV2-May-2016.csv")

# Data Preprocessing 
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
df['ScheduledDayOnly'] = df['ScheduledDay'].dt.date
df['AppointmentDayOnly'] = df['AppointmentDay'].dt.date
df['DayDiff'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days
df['AppointmentWeekDay'] = df['AppointmentDay'].dt.day_name()

# Convert No-show to binary
df['No-show'] = df['No-show'].map({'No': 'Showed Up', 'Yes': 'No Show'})
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Medical Appointment No-Show Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Neighborhood:"),
        dcc.Dropdown(
            id='neigh_filter',
            options=[{'label': n, 'value': n} for n in sorted(df['Neighbourhood'].unique())],
            value=None,
            placeholder="All Neighborhoods"
        ),
        html.Label("Select Gender:"),
        dcc.Dropdown(
            id='gender_filter',
            options=[{'label': g, 'value': g} for g in sorted(df['Gender'].unique())],
            value=None,
            placeholder="All Genders"
        )
    ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),

    html.Div([
        dcc.Graph(id='pie_chart'),
        dcc.Graph(id='box_plot'),
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Graph(id='heatmap_chart'),
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='bar_chart'),
    ], style={'width': '50%', 'display': 'inline-block'})
])

@app.callback(
    [Output('pie_chart', 'figure'),
     Output('box_plot', 'figure'),
     Output('heatmap_chart', 'figure'),
     Output('bar_chart', 'figure')],
    [Input('neigh_filter', 'value'),
     Input('gender_filter', 'value')]
)
def update_graphs(selected_neigh, selected_gender):
    dff = df.copy()
    if selected_neigh:
        dff = dff[dff['Neighbourhood'] == selected_neigh]
    if selected_gender:
        dff = dff[dff['Gender'] == selected_gender]

    # Pie chart: No-show vs Show
    pie_fig = px.pie(dff, names='No-show', title='Attendance Rate')

    # Box plot: Age distribution by show status
    box_fig = px.box(dff, x='No-show', y='Age', color='No-show', title='Age Distribution by Attendance')

    # Heatmap: Appointment weekday vs Scheduled weekday
    heat_data = dff.groupby(['ScheduledDayOnly', 'AppointmentWeekDay']).size().reset_index(name='Count')
    heat_fig = px.density_heatmap(
        heat_data, x='ScheduledDayOnly', y='AppointmentWeekDay', z='Count',
        title='Heatmap of Scheduled Date vs Appointment Day',
        color_continuous_scale='Viridis'
    )

    # Bar chart: Chronic condition impact
    chronic_cols = ['Hipertension', 'Diabetes', 'Alcoholism', 'SMS_received']
    chronic_data = dff[chronic_cols].sum().reset_index()
    chronic_data.columns = ['Condition', 'Count']
    bar_fig = px.bar(chronic_data, x='Condition', y='Count', title='Chronic Conditions Count')

    return pie_fig, box_fig, heat_fig, bar_fig

# Run App 
if __name__ == '__main__':
    app.run(debug=True, port=8050)

