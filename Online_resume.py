import streamlit as st
st.title("Online Resume")
from PIL import Image
img=Image.open("kkk.jpg")
st.image(img,width=300,caption="Simple") 
st.sidebar.selectbox("Select Menu",["Home","About","Projects"])
st.balloons()
