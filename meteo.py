import streamlit as st
import requests
import os
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

API_key=os.getenv("api_key")


def getweather(city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=it'
    
    response = requests.get(url)
    return response.json()   
    
def main():
    st.markdown(
        "<h1 style='color: white;'>Applicazione meteo</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/tree-736875_1280.jpg");
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }

        label {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    
    col1, col2 = st.columns(2)
    with col1:
        city_names = st.text_input("Inserisci il nome della città🌍")
        if city_names:
            data = getweather(city_names)
           
            df = pd.DataFrame({"lat":[ data['coord']['lat']], "lon": [data['coord']['lon']]})
            st.map(df)
           
        
    with col2:
        if city_names:
            data = getweather(city_names)
            
            temperatura = data["main"]["temp"]
            vento = data["wind"]["speed"]
            umidita = data["main"]["humidity"]
            pressione = data["main"]["pressure"]
            st.markdown(
    """
    <style>
    .stAlert > div {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
 )

        st.info(f"🌡️ Temperatura: {temperatura}°C")
        st.info(f"💨 Vento: {vento} m/s")
        st.info(f"💧 Umidità: {umidita}%")
        st.info(f"🌡️ Pressione: {pressione} hPa")

if __name__ == "__main__":
    main()



    
