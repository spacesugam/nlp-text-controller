#corre Pkgs
import streamlit as st

#EDA Pkgs
import pandas as pa
import numpy as np 

#utils
import joblib

def main():
    st.title("emotio classifier app")
    menu = ["Home","Monitor","About"]
    
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("home-Emotion in text")
       
    elif choice == "Monitor":
        st.subheader("Monitor app")

    else:
        st.subheader("about")

if __name__ == 'main__':
    main()
