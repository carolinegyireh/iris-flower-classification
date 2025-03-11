import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("iris_classifier.pkl")

# Customizing the title and layout
st.set_page_config(page_title="Iris Flower Classifier", page_icon="🌺", layout="centered")

# Add a header with a nice description
st.title("🌺 Iris Flower Classifier")
st.subheader("Predict the species of Iris flowers based on their measurements.")

# Add a background image or color for style (optional)
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f4f7fa;
    }
    </style>
""", unsafe_allow_html=True)

# Create a more organized input form
with st.form(key='flower_form'):
    st.write("Please enter the measurements of the flower:")

    # Input fields for features with default values
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1, step=0.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

    # Add a submit button inside the form
    submit_button = st.form_submit_button(label='Predict')

# Handling the prediction logic and displaying the result
if submit_button:
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make a prediction
    predicted_class = model.predict(input_data)[0]

    # Display the prediction result with enhanced styling
    st.markdown(f"""
    <div style="font-size: 20px; font-weight: bold; color: #4CAF50;">
        Predicted Species: <span style="font-size: 22px;">{predicted_class}</span>
    </div>
    """, unsafe_allow_html=True)

    # Additional helpful message
    st.info("Note: The model classifies based on common Iris species, such as Setosa, Versicolor, and Virginica.")
