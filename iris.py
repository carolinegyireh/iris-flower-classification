import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("iris_classifier.pkl")

# title and layout
st.set_page_config(page_title="Iris Flower Classifier", page_icon="🌺", layout="centered")

# Add a header with a nice description
st.title("🌺 Iris Flower Classifier")
st.subheader("Predict the species of Iris flowers based on their measurements.")

# Enhanced CSS styling
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f4f7fa;
    }
    .css-18e3b6p {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Introduction text
st.markdown("""
    <div style="font-size:18px; color: #5c6bc0; font-weight: bold;">
        Enter the flower measurements and we’ll predict the species for you!
    </div>
""", unsafe_allow_html=True)

# Organized input form
with st.form(key='flower_form'):
    st.write("Please enter the measurements of the flower:")

    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1, step=0.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5, step=0.1)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

    submit_button = st.form_submit_button(label='Predict')

# Handling the prediction logic and displaying the result
if submit_button:
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    predicted_class = model.predict(input_data)[0].strip().capitalize()

    # Display the prediction result
    st.markdown(f"""
    <div style="font-size: 22px; font-weight: bold; color: #4CAF50;">
        Predicted Species: {predicted_class}
    </div>
    """, unsafe_allow_html=True)

    # Dictionary of images for each species
    species_images = {
        'Iris-setosa': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/220px-Irissetosa1.jpg',
        'Iris-versicolor': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg',
        'Iris-virginica': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/220px-Iris_virginica_2.jpg'
    }
    
    if predicted_class in species_images:
        st.image(species_images[predicted_class], width=300)
    else:
        st.error("Species image not found!")

    # A model message
    st.info("Side Note: The model classifies based on common Iris species: **Setosa, Versicolor, and Virginica**.")
    
    # Species descriptions
    species_info = {
    'Iris-setosa': """
    It has small and consistently sized, with petals not exceeding the base of the sepals.
    The sepals are relatively smaller compared to versicolor and virginica.
    
    Distribution: Found in arctic and coastal regions.
    Common name: Beachhead Iris
    """,
    
    'Iris-versicolor': """
    Both sepals and petals are moderate in size, falling between setosa and virginica.
    
    Distribution: Found in wetlands and marshy areas of eastern and central North America.
    Common names: Blue Flag, Harlequin Blue Flag, Larger Blue Flag, Northern Blue Flag
    """,
    
    'Iris-virginica': """
    It has generally larger petals and sepals than setosa and versicolor, with notable variability in petal and sepal measurements.
    
    Distribution: Found in wetlands, marshy areas, and along river and lake shores of eastern North America.
    Common name: Southern Blue Flag Iris
    """
}

    st.markdown(f"### About {predicted_class}:")
    st.write(species_info.get(predicted_class, "No description available."))

    # User feedback section
    st.markdown("### Feedback")
    feedback = st.radio("Was this prediction helpful?", ['👍 Yes', '👎 No'])
    comments = st.text_area("Any suggestions or comments?")
    
    if st.button('Submit Feedback'):
        st.success("Thank you for your feedback! 🎉")
        st.write(f"You rated this: {feedback}")
        if comments:
            st.write(f"Your comments: {comments}")
