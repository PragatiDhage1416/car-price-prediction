import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("car_price_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.title(" Car Price Prediction App")

st.write("Enter car details below:")

# User Inputs
year = st.number_input("Year", 2000, 2026)
km_driven = st.number_input("Kilometers Driven", 0, 500000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.number_input("Number of Previous Owners", 0, 5)

# Create input dataframe
input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'owner': [owner],
    'fuel_Diesel': [1 if fuel == "Diesel" else 0],
    'seller_type_Individual': [1 if seller_type == "Individual" else 0],
    'transmission_Manual': [1 if transmission == "Manual" else 0]
})

# Add missing columns
for col in model_columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Arrange columns
input_data = input_data[model_columns]

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_data)

    st.success(f"Estimated Car Price: ₹ {round(prediction[0], 2)} Lakhs")