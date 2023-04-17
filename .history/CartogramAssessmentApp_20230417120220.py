import streamlit as st
import numpy as np
from PIL import Image

st.title("Cartogram Assessment")

img_src = 'BATMAN.jpg'
img = Image.open(img_src)
arr = np.array(img)
st.image(arr)

st.write("Above is a Yoga Image")

