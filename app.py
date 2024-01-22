import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("Final_Patient_Scores.csv") 
    return df

data = load_data()  # Load the cached data

# Define color mapping for BMI categories
bmi_colors = {"Normal": "green", "Overweight": "yellow", "Obese": "red"}

# Patient selection
selected_id = st.selectbox("Choose a patient ID", data["Patient_ID"].unique())
patient_data = data[data["Patient_ID"] == selected_id]

# Basic patient information
st.header(f"Patient ID: {selected_id}")
st.write(f"BMI: {patient_data['BMI'].values[0]}",
         safe_html=f"<span style='color:{bmi_colors[patient_data['BMI'].values[0]]}'>{patient_data['BMI'].values[0]}</span>")

# Compliance scores
st.subheader("Compliance Scores")
cols = ["History_Score", "Alcohol_Score", "Diabetes_Signs_Score", "Diet_Score", "Exercise_Score", "Medication_Score"]
table_data = [["Compliance Category", "Patient", "Population Average"]]

for col in cols:
    score = patient_data[col].values[0]
    normalized = patient_data[f"{col}_Normalized"].values[0]
    avg_normalized = data[data["BMI"] == patient_data["BMI"].values[0]][f"{col}_Normalized"].mean()
    
    table_data.append([col, f"{score:.2f}", f"{normalized:.2f}"])

st.table(table_data)

# Normalized scores comparison
st.subheader("Normalized Score Comparison")
fig, ax = plt.subplots()
bar_width = 0.35
bar_positions_patient = range(len(cols))
bar_positions_average = [pos + bar_width for pos in bar_positions_patient]

# Plotting patient scores
ax.bar(bar_positions_patient, patient_data[cols].values[0], width=bar_width, label="Patient")

# Plotting average scores
avg_normalized = data[cols].mean().values
ax.bar(bar_positions_average, avg_normalized, width=bar_width, label="Average", alpha=0.5)

ax.set_xticks([pos + bar_width / 2 for pos in bar_positions_patient])
ax.set_xticklabels(cols, rotation=45, ha="right")  # Adjust rotation angle as needed
ax.set_xlabel("Compliance Category")
ax.set_ylabel("Normalized Score")
ax.legend()

st.pyplot(fig)

# Overall compliance radar chart
st.subheader("Overall Compliance")
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
theta = range(len(cols))
radius = patient_data[cols].values[0]
ax.fill(theta, radius, color="blue", alpha=0.25)
# Calculate the overall average without filtering by BMI
avg_radius = data[cols].mean().values
ax.fill(theta, avg_radius, color="orange", alpha=0.25)
ax.set_xticks(theta)
ax.set_xticklabels(cols)
ax.set_ylabel("Score")
ax.set_title("Patient vs. Average")
st.pyplot(fig)

