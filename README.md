# Autism Spectrum Disorder Predciton using Machine Learning Models
## Overview
This project focuses on predicting where an individual falls on the Autism Spectrum Disorder (ASD) based on a set of input features. The dataset from Kaggle was cleaned and preprocessed, and used to develop and train multiple machine learning models, including Logistic Regression, XGBoost, Support Vector Classifier (SVC), and a Deep Learning model, for accurate predictions. The trained model with the best performance has been deployed using Streamlit, allowing users to input values interactively and receive predictions in real time. This system provides an efficient and accessible tool for ASD prediction.
## Performance
The models trained for Autism Spectrum Disorder (ASD) prediction showed promising results, with SVC emerging as the best performer, achieving an accuracy of 81% and a weighted F1-score of 0.82. Logistic Regression and XGBoost followed closely, both with 79% accuracy and F1-scores of 0.80. While all models demonstrated strong classification for non-autistic cases, SVC showed a better balance in predicting both autistic and non-autistic individuals, making it the most reliable model for this task.
## Organization

The project directory is organized as follows:

| **File/Folder**       | **Description**                                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------|
| `.gitignore`          | Specifies files and folders to be ignored by Git version control.                             |
| `Autism_Prediction.ipynb` | Jupyter notebook containing the main implementation of the autism prediction system.         |
| `app.py`              | Streamlit app file for user interaction and predictions.                                       |
| `best_model.pkl`      | Saved machine learning model with the best performance (used for predictions).                |
| `requirements.txt`    | List of Python dependencies required to run the project.                                       |
| `scaler.pkl`          | Saved scaler object for normalizing input features.                                            |
| `test.csv`            | Test dataset used for evaluation of the trained model.                                        |
| `train.csv`           | Training dataset used for building the machine learning model.                                |


### Sample Data to detect Autism

| **Feature**             | **Value**   |
|-------------------------|-------------|
| **A1 Score**            | 1           |
| **A2 Score**            | 1           |
| **A3 Score**            | 1           |
| **A4 Score**            | 1           |
| **A5 Score**            | 1           |
| **A6 Score**            | 1           |
| **A7 Score**            | 1           |
| **A8 Score**            | 0           |
| **A9 Score**            | 1           |
| **A10 Score**           | 1           |
| **Age**                 | 3.432316    |
| **Gender (Male/Female)**| 0           |
| **Ethnicity**           | 9           |
| **Jaundice**            | 1           |
| **Country of Residence**| 52          |
| **Result**              | 15.112454   |
| **Relation**            | 4           |
| **Age Group**           | 4           |
| **Sum Score**           | 9           |
| **Individual Score**    | 2           |


