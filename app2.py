import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("house_price_model.pkl")

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Select the house details from the sidebar, review them below, then click **Predict**.")

# -----------------------------
# Sidebar - Numeric Inputs
# -----------------------------
st.sidebar.header("House Information")

overall_qual = st.sidebar.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.sidebar.number_input("Ground Living Area (sq ft)", min_value=200, value=1500)
garage_cars = st.sidebar.slider("Garage Capacity (cars)", 0, 5, 2)
garage_area = st.sidebar.number_input("Garage Area (sq ft)", min_value=0, value=500)
total_bsmt = st.sidebar.number_input("Total Basement Area (sq ft)", min_value=0, value=800)
first_floor = st.sidebar.number_input("1st Floor Area (sq ft)", min_value=300, value=1200)

# -----------------------------
# Sidebar - Categorical Inputs
# -----------------------------
mszoning = st.sidebar.selectbox("MS Zoning", ["RL", "RM", "FV", "RH", "C (all)"])
street = st.sidebar.selectbox("Street", ["Pave", "Grvl"])

neighborhood = st.sidebar.selectbox(
    "Neighborhood",
    ["NAmes", "CollgCr", "OldTown", "Edwards", "Somerst", "NridgHt", "Gilbert",
     "Sawyer", "NWAmes", "BrkSide", "Mitchel", "Crawfor", "Timber", "StoneBr",
     "NoRidge", "SWISU", "IDOTRR", "MeadowV", "ClearCr", "Blmngtn", "BrDale",
     "Veenker", "NPkVill", "Blueste"]
)

house_style = st.sidebar.selectbox(
    "House Style",
    ["1Story", "2Story", "1.5Fin", "1.5Unf", "SLvl", "SFoyer", "2.5Fin", "2.5Unf"]
)

quality_options = ["Ex", "Gd", "TA", "Fa", "Po", "unknown"]

exter_qual = st.sidebar.selectbox("Exterior Quality", quality_options)
bsmt_qual = st.sidebar.selectbox("Basement Quality", quality_options)
kitchen_qual = st.sidebar.selectbox("Kitchen Quality", quality_options)
garage_qual = st.sidebar.selectbox("Garage Quality", quality_options)

central_air = st.sidebar.selectbox("Central Air", ["Y", "N"])

sale_condition = st.sidebar.selectbox(
    "Sale Condition",
    ["Normal", "Partial", "Family", "Abnorml", "Alloca", "AdjLand"]
)

# -----------------------------
# Build Input DataFrame
# -----------------------------
input_df = pd.DataFrame({
    "OverallQual": [overall_qual],
    "GrLivArea": [gr_liv_area],
    "GarageCars": [garage_cars],
    "GarageArea": [garage_area],
    "TotalBsmtSF": [total_bsmt],
    "1stFlrSF": [first_floor],
    "MSZoning": [mszoning],
    "Street": [street],
    "Neighborhood": [neighborhood],
    "HouseStyle": [house_style],
    "ExterQual": [exter_qual],
    "BsmtQual": [bsmt_qual],
    "CentralAir": [central_air],
    "KitchenQual": [kitchen_qual],
    "GarageQual": [garage_qual],
    "SaleCondition": [sale_condition]
})

# -----------------------------
# Center - Show Selected Values
# -----------------------------
st.subheader("Selected Feature Values")

summary_df = pd.DataFrame({
    "Feature": [
        "Overall Quality",
        "Ground Living Area (sq ft)",
        "Garage Capacity (cars)",
        "Garage Area (sq ft)",
        "Total Basement Area (sq ft)",
        "1st Floor Area (sq ft)",
        "MS Zoning",
        "Street",
        "Neighborhood",
        "House Style",
        "Exterior Quality",
        "Basement Quality",
        "Kitchen Quality",
        "Garage Quality",
        "Central Air",
        "Sale Condition"
    ],
    "Value": [
        overall_qual,
        gr_liv_area,
        garage_cars,
        garage_area,
        total_bsmt,
        first_floor,
        mszoning,
        street,
        neighborhood,
        house_style,
        exter_qual,
        bsmt_qual,
        kitchen_qual,
        garage_qual,
        central_air,
        sale_condition
    ]
})

st.table(summary_df)

# -----------------------------
# Predict Button
# -----------------------------
st.write("")

if st.button("Predict House Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")