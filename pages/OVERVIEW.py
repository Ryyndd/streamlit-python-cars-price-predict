import streamlit as st

st.title("CAR PRICE PREDICT OVERVIEW")
st.write("""
Website ini menyediakan platform yang memungkinkan pengguna untuk mendapatkan prediksi harga mobil berdasarkan berbagai parameter yang dimasukkan, seperti merek, model, tahun pembuatan, kondisi kendaraan, dan lain-lain. Fitur utama dari website ini adalah kemampuan untuk memberikan estimasi harga mobil secara real-time menggunakan model prediksi berbasis machine learning.

Dengan menggunakan **Streamlit Elements**, website ini memberikan pengalaman pengguna yang interaktif dan mudah. Pengguna dapat memasukkan data terkait mobil yang ingin mereka jual atau beli, dan algoritma akan menghitung dan memberikan perkiraan harga pasar yang akurat.
""")
st.header("Fitur Utama")
st.write("""
Beberapa fitur utama yang dapat ditemukan di website ini antara lain:
""")

st.subheader("1. Input Parameter")
st.write("Pengguna dapat memilih atau mengisi detail mobil seperti highway, curbweigh, housepower dll")

st.subheader("2. Prediksi Harga")
st.write("Setelah data dimasukkan, sistem akan memberikan prediksi harga jual atau beli mobil berdasarkan analisis data historis dan algoritma prediksi.")

st.subheader("3. UI Interaktif")
st.write("Dibangun dengan **Streamlit Elements**, interface website ini responsif dan mudah digunakan, dengan desain yang sederhana namun informatif.")

st.subheader("4. Rekomendasi Harga")
st.write("Selain prediksi, website ini juga memberikan saran harga berdasarkan tren pasar terkini, membantu pengguna menentukan harga yang wajar.")


# import streamlit as st 
# import altair as alt 
# import pandas as pd 
# import numpy as np 


# # st.sidebar.title("THIS IS SIDEBAR")
# # app_mode = st.sidebar.selectbox('Select Mode', ['Image', 'Dataset', 'Grafik'])

# # if app_mode == 'Image':
# #     st.title('Image Python')
# #     st.image('python.jpg')

# # if app_mode == 'Dataset':
# #     st.title('Preview Dataset')
# #     data = pd.read_csv('depresionStudentDataset.csv')
# #     st.write(data.head(20))

    
# # if app_mode == 'Grafik':
# #     st.title("Bar Chart")
# #     data = pd.read_csv('depresionStudentDataset.csv')
# #     st.bar_chart(data[['Depression', 'Academic Pressure']].head(20))


