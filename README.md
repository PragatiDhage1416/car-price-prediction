# 🚗 Car Price Prediction

A Machine Learning web application that predicts the estimated selling price of a used car based on its details.

## 📌 Project Overview

This project uses Machine Learning to predict the selling price of a used car based on details such as year, kilometers driven, fuel type, seller type, transmission, and number of previous owners.

The trained Machine Learning model is integrated with a Streamlit web application, allowing users to enter car details and get an estimated price.

## 🚀 Features

- Predicts the estimated price of a used car
- Interactive Streamlit web interface
- Supports different fuel types
- Supports dealer and individual sellers
- Supports manual and automatic transmission
- Takes kilometers driven and previous owners into consideration
- Uses a trained Machine Learning model for prediction

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Machine Learning

## 🤖 Machine Learning Model

The project uses a trained Machine Learning regression model to predict car prices.

### Machine Learning Workflow

1. Load the car price dataset.
2. Perform data preprocessing.
3. Select the required input features.
4. Convert categorical variables into numerical values.
5. Prepare the training data.
6. Train the Machine Learning regression model.
7. Evaluate the model.
8. Save the trained model using Pickle.
9. Save the model feature columns.
10. Load the saved model in the Streamlit application.
11. Take car details as input from the user.
12. Convert the user input into the required format.
13. Predict the estimated car price.
14. Display the predicted price in the Streamlit application.

## ▶️ How to Run the Project

### 1. Clone the Repository

git clone https://github.com/PragatiDhage1416/car-price-prediction.git

### 2.Open the project folder
cd car-price-prediction

### 3. Install Required Libraries
pip install -r requirements.txt

### 4. Run the Streamlit Application
streamlit run app.py

### 5. Open the appllications
after running the commond,Streamlit will providen a local URL

Usually:
https://localhost:8501

Open this URL in your web browser to use the Car Price Precdition application.

## 📂 Project Structure
car-price-prediction/
│
 app.py
| main.py
| car_price_model.pkl
|model_columns.pkl
| requirements.txt
| README.md

## 👩‍💻 Author 
**Pragati Dhage**
GitHub: https://github.com/PragatiDhage1416
