import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing patient summaries
df = pd.read_csv("patient_summaries.csv")

# Streamlit app
def main():
    st.title("Patient Summary Viewer")

    # Create a dropdown to select a Patient_ID
    selected_patient_id = st.selectbox("Select Patient_ID:", df["Patient_ID"].unique())

    # Create a radio button to switch between functionalities
    mode = st.radio("Select Mode:", ("View Summary", "View Enhanced Summary"))

    if mode == "View Summary":
        if st.button("View Summary"):
            if selected_patient_id:
                # Retrieve and display the summary for the selected Patient_ID
                selected_summary = df[df["Patient_ID"] == selected_patient_id]["Summary"].values[0]
                st.subheader("Patient Summary:")
                st.write(selected_summary)
            else:
                st.warning("Please select a Patient_ID.")
    else:
        if st.button("View Enhanced Summary"):
            if selected_patient_id:
                # Retrieve and display the enhanced summary for the selected Patient_ID
                enhanced_summary = df[df["Patient_ID"] == selected_patient_id]["Enhanced_Summary"].values[0]
                st.subheader("Enhanced Patient Summary:")
                st.write(enhanced_summary)
            else:
                st.warning("Please select a Patient_ID.")

if __name__ == "__main__":
    main()
