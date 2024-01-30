import streamlit as st
import pandas as pd

# Load the CSV file containing patient summaries
df = pd.read_csv("patient_summaries.csv")

# Streamlit app
def main():
    st.title("Patient Summary Viewer")

    # Create a dropdown to select a Patient_ID
    selected_patient_id = st.selectbox("Select Patient_ID:", df["Patient_ID"].unique())

    # Create a button to trigger the selected functionality
    if st.button("View Summary"):
        if selected_patient_id:
            # Retrieve and display the summary for the selected Patient_ID
            selected_summary = df[df["Patient_ID"] == selected_patient_id]["Summaries"].values[0]
            st.subheader("Patient Summary:")
            st.write(selected_summary)
        else:
            st.warning("Please select a Patient_ID.")

if __name__ == "__main__":
    main()
