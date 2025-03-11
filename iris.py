import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("iris_classifier.pkl")

st.title("🌺 Iris Flower Classifier")
st.write("Enter flower measurements to predict its species.")

# Input fields for features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict"):
    # Prepare the input data
    input_data = ([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make a prediction
    predicted_class = model.predict(input_data)[0]

    # Display the result
    st.success(f"Predicted Species: **{predicted_class}**")
