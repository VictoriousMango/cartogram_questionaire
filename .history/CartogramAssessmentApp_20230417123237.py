import streamlit as st
import numpy as np
from PIL import Image
import QuizGiver as QG

# Session States
if 'time_stamp' not in st.session_state:
   st.session_state['time_stamp'] = 0
if 'QuizDoc' not in st.session_state:
   st.session_state['QuizDoc'] = 0

# End Session States

st.title("Cartogram Assessment")



img_src = 'BATMAN.jpg'
img = Image.open(img_src)
arr = np.array(img)
st.image(arr)

with open('Questions.txt', 'r') as Questions:
    st.session_state['QuizDoc'] = Questions.read()


st.write("Above is a Yoga Image")

# Doc to Quiz
Ans = QG.app(st.session_state['QuizDoc'], st.session_state['time_stamp'])
