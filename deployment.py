import streamlit as st
import requests
import pandas as pd
import streamlit_lottie as st_lottie
from streamlit_option_menu import option_menu
import joblib
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Water Potability", page_icon="💧", layout="centered", initial_sidebar_state="collapsed")
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

model = joblib.load(open("ai", "rb"))

def predict(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
    features = np.array([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]).reshape(1, -1)
    prediction = model.predict(features)
    return prediction

with st.sidebar:
    choose = option_menu(None, ["Home", "Graphs", "About","Contact"],
                        icons = ["house", "kanban", "book","person lines fill"],
                        menu_icon="app-indicator",default_index=0,
                        styles = {
        "container": {"padding": "5!important","background-color":"#fafafa"},
        "icon": {"color": "#E0E0EF","font-size":"25px"},
        "nav-link": {"text-align":"left","font-size":"16px","margin":"0px","--hover-color": "#eee"},
        "nav-link:selected": {"background-color": "#02ab21"},                        
    }
    )
    
if choose == "Home":
    st.write("# Water Potability")
    st.subheader("Enter the values to predict the potability of water")
    ph= st.number_input("Enter the pH value of water",min_value=0.0,max_value=14.0,step=1.0)
    Hardness= st.number_input("Enter the Hardness value of water",min_value=0.0,step=1.0)
    Solids= st.number_input("Enter the Solids value of water",min_value=0.0,step=1.0)
    Chloramines= st.number_input("Enter the Chloramines value of water",min_value=0.0,step=1.0)
    Sulfate= st.number_input("Enter the Sulfate value of water",min_value=0.0,step=1.0)
    Conductivity= st.number_input("Enter the Conductivity value of water",min_value=0.0,step=1.0)
    Organic_carbon= st.number_input("Enter the Organic_carbon value of water",min_value=0.0,step=1.0)
    Trihalomethanes= st.number_input("Enter the Trihalomethanes value of water",min_value=0.0,step=1.0)
    Turbidity= st.number_input("Enter the Turbidity value of water",min_value=0.0,step=1.0)
    # predict the potability of water
    sample=predict(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity)
    if st.button("Predict"):
        if sample == 1:
            st.write("# The water is potable")
            st.balloons()
        elif sample == 0:
            st.write("# The water is not potable")
elif choose == "Graphs":
    st.write("# Water Potability Graphs")
    st.image("images/download.png")
    st.image("images/download (1).png")
    st.image("images/download (2).png")
    st.image("images/download (3).png")
    st.image("images/download (4).png")
elif choose == "About":
    st.write("# About Water Potability")
    st.write("Water potability refers to the quality of water in terms of its chemical, physical, and biological characteristics in relation to the health of humans and animals. This is a very important aspect of water quality since it determines the safety of water for human consumption and other uses.")
    st.write("The potability of water is determined by the presence of various chemical substances in water. These substances include pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity. The presence of these substances in water can affect its potability.")
    st.write("The potability of water can be determined using various methods such as chemical analysis, physical testing, and biological testing. These methods are used to determine the presence of harmful substances in water and to ensure that water is safe for human consumption.")
    
elif choose == "Contact":
    st.write("# Contact Us")
    
data = pd.read_csv("water_potability.csv")
df=pd.DataFrame(data)