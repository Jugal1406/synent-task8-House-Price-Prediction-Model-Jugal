import streamlit as st
import pickle
import numpy as np

model=pickle.load(open("house_price_model.pkl","rb"))
st.title("🏠 House Price Prediction App")
st.write("Enter house Details :")

GrLivArea = st.number_input("Living Area (sq ft)")
BedroomAbvGr = st.number_input("Bedrooms")
FullBath = st.number_input("Bathrooms")
GarageCars = st.number_input("Garage Capacity")
TotalBsmtSF = st.number_input("Basement Area")
OverallQual = st.slider("Overall Quality (1-10)", 1, 10)

if st.button("Predict Price"):
    input_data=np.array([[GrLivArea,BedroomAbvGr,FullBath,GarageCars,TotalBsmtSF,OverallQual]])
    prediction=model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
             