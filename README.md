# 📊 Medical Appointment Dashboard

An interactive dashboard for analyzing **Medical Appointment No-Show** dataset.  
Built using **Python**, **Pandas**, **Plotly**, and **Dash** to provide visual insights into patient attendance patterns.

---

## 🚀 Features
- **Dynamic Filtering** by Gender and Neighborhood.
- **Interactive Visualizations**:
  - **Pie Chart**: Attendance vs No-Show percentage.
  - **Box Plot**: Age distribution by attendance status.
  - **Heatmap**: Attendance frequency by day of the week.
  - **Bar Chart**: Count of chronic conditions (Diabetes, Hypertension, Alcoholism).
- **Summary Insight** section showing:
  - Total appointments in selection.
  - No-show rate percentage.
  - Average patient age.

---

## 📂 Dataset
Dataset: **KaggleV2-May-2016.csv**  
Source: [Kaggle - Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)  

Main Columns Used:
- `Gender`
- `Neighbourhood`
- `Age`
- `AppointmentDay`
- `ScheduledDay`
- `No-show`
- `Hypertension`, `Diabetes`, `Alcoholism`

---

## 🛠 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ranav161304/Dash-board.git
   cd medical-dashboard
   ```

2. Install required dependencies:
   ```bash
   pip install pandas plotly dash
   ```

3. Place your dataset (`KaggleV2-May-2016.csv`) in the project folder.

---

## 📸 Preview
| Chart Type        | Description                              |
|-------------------|------------------------------------------|
| Pie Chart         | Attendance vs No-Show ratio              |
| Box Plot          | Age distribution per attendance status   |
| Heatmap           | Attendance by day of the week            |
| Bar Chart         | Count of chronic conditions              |

---

## 📌 Insights Example
- Higher no-show rates on certain weekdays.
- Older patients tend to have better attendance.
- Patients with chronic diseases tend to attend more consistently.

---

## 📜 License
This project is licensed under the MIT License.
