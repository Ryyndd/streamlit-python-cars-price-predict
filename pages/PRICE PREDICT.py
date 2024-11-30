import pickle
import streamlit as st 
import altair as alt 
import pandas as pd 
import numpy as np 
# from joblib import dump

# Load the dataset
df1 = pd.read_csv('./pages/CarPrice_Assignment.csv')

# Load the trained model
model = pickle.load(open('./pages/model1.sav', 'rb'))
print(type(model))  # Check the model type (should be LinearRegression)

st.title("CARS PRICE PREDICT")

st.header("DATASET")
st.dataframe(df1)

# Display charts for each feature
st.write("Grafik Highway-mpg")
chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
st.line_chart(chart_highwaympg)

st.write("Grafik curbweight")
chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
st.line_chart(chart_curbweight)

st.write("Grafik horsepower")
chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chart_horsepower)

# Input fields for independent variables
highwaympg = st.number_input('Highway MPG', min_value=0)
curbweight = st.number_input('Curbweight', min_value=0)
horsepower = st.number_input('Horsepower', min_value=0)

if st.button('PREDICT'):
    # Make prediction with input values
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

    # Convert the prediction to a float and format the output
    harga_mobil_float = float(car_prediction[0])

    # Display the predicted car price
    st.write(f"Prediksi Harga Mobil: ${harga_mobil_float:,.2f}")
