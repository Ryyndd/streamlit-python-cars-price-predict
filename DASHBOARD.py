import streamlit as st
import pandas as pd
import numpy as np
# Set page configuration
st.set_page_config(page_title="Car Dashboard", layout="wide")
# Title
st.title("CARS PREVIEW")

# Define a list of car models and their image URLs
car_images = {
    "ASTON MARTIN" :"https://images.autofun.co.id/file1/c53f7dae5ecd4b95ac845274b1d55dbe_606x402.jpg",
    "BMW Z4" : "https://images.autofun.co.id/file1/3ce98d37ebd34bcba00b3424acefd2db_606x402.jpg",
    "AUDI TT CUPO" : "https://images.autofun.co.id/file1/80c98efcf736468885d3296eef10e479_606x402.jpg",
    "FERRARI 488 GTB" : "https://images.autofun.co.id/file1/1ca32dcc4f5e44d29559c5304563bac8_606x402.jpg",
    "FERRARI 44 SPIDER" : "https://images.autofun.co.id/file1/cbb4b28c3967481ab50a25da10a9ac85_606x402.jpg",
    "LAMBORGINI AVENTADOR" : "https://images.autofun.co.id/file1/21cb91276b7643cd8e6e8239d91ad0b0_606x402.jpg",
    "MAZDA MX" : "https://images.autofun.co.id/file1/20e1f6beaa7c42dd92f229c99eb01abf_606x402.jpg",
    "LAMBORGHINI HURACAN" : "https://images.autofun.co.id/file1/f564513d50bb43b0976cdd988c9907d2_606x402.jpg",
    "MCLERENT GT" : "https://images.autofun.co.id/file1/9418c56cfcb14138b49e170a509a9927_606x402.jpg"
}

# Create a grid using columns
columns = st.columns(3)  # This will create 3 columns for the grid

# Iterate through the car images and display them in the columns
for idx, (car_model, image_url) in enumerate(car_images.items()):
    col = columns[idx % 3]  # Rotate between 3 columns
    with col:
        st.image(image_url, caption=car_model, width=300)
