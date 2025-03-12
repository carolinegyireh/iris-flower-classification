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
        **Predicted Species:** {predicted_class}
    </div>
    """, unsafe_allow_html=True)

    # Dictionary of images for each species
    species_images = {
        'Setosa': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Iris_setosa_3.jpg/800px-Iris_setosa_3.jpg',
        'Versicolor': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Iris_versicolor_4.jpg/800px-Iris_versicolor_4.jpg',
        'Virginica': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Iris_virginica_1.jpg/800px-Iris_virginica_1.jpg'
    }
    
    if predicted_class in species_images:
        st.image(species_images[predicted_class], width=300)
    else:
        st.error("Species image not found!")

    # Additional helpful message
    st.info("Note: The model classifies based on common Iris species: **Setosa, Versicolor, and Virginica**.")
    
    # Species descriptions
    species_info = {
        'Setosa': "Setosa is characterized by small flowers with shorter petals.",
        'Versicolor': "Versicolor has medium-sized flowers with moderate petal length.",
        'Virginica': "Virginica features large flowers with long petals."
    }
    
    st.markdown(f"### About **{predicted_class}**:")
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
