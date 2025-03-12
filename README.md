# Iris Flower Classification 🌸 
This project demonstrates the classification of Iris flowers into three species (Setosa, Versicolor, and Virginica) based on their sepal and petal measurements. I used the machine learning techniques **K-Nearest Neighbors (KNN)** algorithm, to build a predictive model. 


![iris app](https://github.com/user-attachments/assets/15678584-d1db-47eb-9e03-4e0451e31a9f)


## Project Overview

The project involves the following steps:

1. **Data Loading and Exploration:** The Iris dataset is loaded and explored using descriptive statistics and visualizations to understand the data's structure and features.
2. **Data Preprocessing:** The dataset is cleaned by handling missing values and irrelevant features.
3. **Data Visualization:** Various plots, including pair plots, histograms, box plots, heatmaps, and pie charts, are used to visualize the data and gain insights into the relationships between features and species.
4. **Data Splitting:** The dataset is split into training and testing sets to evaluate the model's performance.
5. **Model Training:** The KNN algorithm is used to train a classification model on the training data.
6. **Model Evaluation:** The model's accuracy is evaluated using metrics like accuracy score, classification report, and confusion matrix.
7. **Prediction:** The trained model is used to predict the species of new Iris flowers based on their measurements.
8. **Model Saving:** The trained model is saved for future use.
9. **Streamlit web app:** Deployed a web app built using streamlit that takes the values input by the user and predicts the Iris species.
## Dataset

The project uses the Iris dataset, a classic dataset in machine learning. It contains 150 samples of Iris flowers, with 50 samples for each of the three species. Each sample has four features: sepal length, sepal width, petal length, and petal width.

## Dependencies

The project requires the following libraries:

- Python 3.x
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- joblib
- streamlit

You can install these libraries using pip:

## Usage

1. Clone the repository: `git clone https://github.com/carolinegyireh/iris-flower-classification.git`
2. Navigate to the project directory: `cd iris-flower-classification`
3. Run the Jupyter notebook: `jupyter notebook Iris_Flower_Classification_Project.ipynb`
4. Follow the instructions in the notebook to load the data, train the model, and make predictions.

## Results

The trained KNN model achieved an accuracy of **1.0** on the test set, indicating its ability to accurately classify Iris flowers.
The classification report and confusion matrix further illustrate the model's performance, showing a perfect prediction.
![cm](https://github.com/user-attachments/assets/67424835-4b6a-4de3-b707-fba210759211)

## How the App Works
1. **User Input**:  
   - The user provides four numerical inputs:  
     - **Sepal Length**  
     - **Sepal Width**  
     - **Petal Length**  
     - **Petal Width**  

2. **Model Prediction**:  
   - The app uses a trained machine learning model KNN to classify the flower into one of three species:  
     - **Iris-setosa**  
     - **Iris-versicolor**  
     - **Iris-virginica**  

3. **Result Display**:  
   - The predicted species name is shown to the user.
   - Image of the species predicted is displayed
   - A brief description of the predicted species, including petal/sepal characteristics and common names, is displayed.
  
4. **Feedback/Suggestions**
   - It ask user for feedback and comments or suggestions so as to keep improving the model.

The user can input new values to classify another flower.  

## Contributing
Contributions to this project are welcome. Please feel free to submit pull requests or open issues for any bug fixes, improvements, or new features.

## License

This project is licensed under the MIT License.


## Deployed App

You can access the deployed Streamlit web app here:
[Iris Classification App](https://iris-flower-classification-vqyeqdl89gqdclx3nouw7a.streamlit.app/)

## Author
[Caroline Gyireh](https://github.com/carolinegyireh/)
