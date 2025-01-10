import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler  # Import scaler if needed

# Load the trained model and scaler
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

# If you saved the scaler separately, load it as well
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Title
st.title("Autism Prediction App")

# Input features
st.header("Input Features")
age = st.number_input("Age", min_value=0.000000, max_value=120.0000000, value=25.000000, step=0.000001,  format="%.6f")
a1_score = st.selectbox("A1 Score (1 or 0)", [0, 1])
a2_score = st.selectbox("A2 Score (1 or 0)", [0, 1])
a3_score = st.selectbox("A3 Score (1 or 0)", [0, 1])
a4_score = st.selectbox("A4 Score (1 or 0)", [0, 1])
a5_score = st.selectbox("A5 Score (1 or 0)", [0, 1])
a6_score = st.selectbox("A6 Score (1 or 0)", [0, 1])
a7_score = st.selectbox("A7 Score (1 or 0)", [0, 1])
a8_score = st.selectbox("A8 Score (1 or 0)", [0, 1])
a9_score = st.selectbox("A9 Score (1 or 0)", [0, 1])
a10_score = st.selectbox("A10 Score (1 or 0)", [0, 1])

# Handle categorical features: gender, ethnicity, country_of_res, relation, ageGroup
gender = st.selectbox("Gender", ["Male", "Female"])  # Assuming binary encoding for gender
gender = 0 if gender == "Male" else 1  # Binary encoding (0=Male, 1=Female)

# You need to replace these with actual categories available in your data
ethnicity = st.selectbox("Ethnicity", ["Ethnicity1", "Ethnicity2", "Ethnicity3"])  # Update with actual categories
ethnicity_dict = {"Ethnicity1": 9, "Ethnicity2": 1, "Ethnicity3": 2}  # Map categories to numbers
ethnicity = ethnicity_dict.get(ethnicity, 0)  # Default to 0 if category not found

country_of_res = st.selectbox("Country of Residence", ["Country1", "Country2", "Country3"])  # Update with actual countries
country_dict = {"Country1": 52, "Country2": 1, "Country3": 2}  # Update with actual mapping
country_of_res = country_dict.get(country_of_res, 0)  # Default to 0
result = st.selectbox("Result (Target Variable for Prediction)", [0, 15.112454])
relation = st.selectbox("Relation", ["Parent", "Sibling", "Other"])  # Update with actual relations
relation_dict = {"Parent": 4, "Sibling": 1, "Other": 2}  # Update with actual mapping
relation = relation_dict.get(relation, 0)  # Default to 0

age_group = st.selectbox("Age Group", ["Group1", "Group2", "Group3"])  # Update with actual age groups
age_group_dict = {"Group1": 4, "Group2": 2, "Group3": 2}  # Update with actual mapping
age_group = age_group_dict.get(age_group, 0)  # Default to 0

# Input features
jaundice = st.selectbox("Jaundice (1 or 0)", [0, 1])  # Assuming binary input for jaundice

# Sum score and individual score
sum_score = st.number_input("Sum Score", min_value=0, max_value=100, value=50)
ind = st.number_input("Individual Score", min_value=0, max_value=100, value=50)

# Predict
if st.button("Predict"):
    # Create the features array with transformed inputs
    features = np.array([[a1_score, a2_score, a3_score, a4_score, a5_score, a6_score, a7_score, a8_score, a9_score, a10_score,
                          age, gender, ethnicity, jaundice, country_of_res, result, relation, age_group, sum_score, ind]])

    # Scale the features using the saved scaler
    features_scaled = scaler.transform(features)

    # Make the prediction
    prediction = model.predict(features_scaled)

    # Display the result
    result = "Autistic" if prediction[0] == 1 else "Non-Autistic"
    st.subheader(f"Prediction: {result}")
