import streamlit as st
import numpy as np
from PIL import Image

st.title("Cartogram Assessment")

img_src = 'src\BATMAN.jpg'
img = Image.open(img_src)
arr = np.array(img)
st.image(arr)

with open('src\Questions.txt', 'r') as Questions:
    st.write(Questions.read()) 

st.write("Above is a Yoga Image")

