# 🏠 House Price Prediction Web App

## 🔹 Project Overview
This project is an end-to-end Machine Learning application that predicts house prices based on user input features. It covers the complete data science workflow including data preprocessing, model building, evaluation, and deployment using Streamlit.

---

## 🔹 Objective
To build a regression model that can accurately predict house prices using key features such as living area, number of rooms, and overall quality.

---

## 🔹 Dataset
- Source: Kaggle  
- Dataset: House Prices – Advanced Regression Techniques  
- File Used: `train.csv`

---

## 🔹 Features Used
- GrLivArea (Living Area in sq ft)  
- BedroomAbvGr (Number of Bedrooms)  
- FullBath (Number of Bathrooms)  
- GarageCars (Garage Capacity)  
- TotalBsmtSF (Basement Area)  
- OverallQual (Overall Quality Rating)  

---

## 🔹 Machine Learning Workflow

### 1. Data Preprocessing
- Selected relevant features  
- Handled missing values using median imputation  

### 2. Feature Selection
- Reduced dataset to important numerical features for simplicity and performance  

### 3. Model Training
- Linear Regression  
- Random Forest Regressor  

### 4. Model Evaluation
- Evaluation Metric: RMSE (Root Mean Squared Error)

| Model               | RMSE      |
|--------------------|----------|
| Linear Regression  | 39240.83 |
| Random Forest      | 28642.50 |

👉 Random Forest performed better and was selected as the final model.

---

## 🔹 Deployment
The model is deployed using **Streamlit** to create an interactive web application.

### 🔗 Live App
👉 https://house-price-prediction-basic-model.streamlit.app/

---

## 🔹 Sample Input & Prediction

**Input:**
- Living Area: 2000 sq ft  
- Bedrooms: 3  
- Bathrooms: 2  
- Garage Capacity: 2  
- Basement Area: 800 sq ft  
- Overall Quality: 7  

**Output:**
👉 Estimated Price: **$217,773.60**

---

## 🔹 Key Learnings
- Understood the complete **machine learning pipeline** from data preprocessing to deployment  
- Learned how to handle **missing values and feature selection**  
- Implemented and compared **Linear Regression and Random Forest models**  
- Evaluated model performance using **RMSE**  
- Built and deployed an interactive web application using **Streamlit**  
- Gained experience in integrating **ML models with user interfaces**
