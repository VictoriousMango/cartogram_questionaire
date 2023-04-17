# Imports
import streamlit as st
import numpy as np
from PIL import Image
import time
# Importing Files
import QuizGiver as QG
# Importing Files
# Imports

# Session States
if 'time_stamp' not in st.session_state:
   st.session_state['time_stamp'] = 0
if 'QuizDoc' not in st.session_state:
   st.session_state['QuizDoc'] = 0

# End Session States

# Test Functions
def clicked():
   st.write('Finished')
        
def Quizzer():
   st.session_state['QuizDoc'] = open('Questionaire Doc\Questions.txt', 'r')
   Ans = QG.app(st.session_state['QuizDoc'], st.session_state['time_stamp'])
   return Ans
# Test Functions

# Title Bar
col1, col2 = st.columns([6, 4])
col1.title("Cartogram Assessment")
ph = col2.empty()
# Title Bar


# Doc to Quiz
st.session_state['QuizDoc'] = 'Questions.txt'
Endcol1, Endcol2 = st.columns([6, 4])



if st.session_state['QuizDoc']:    
    Ans = Quizzer()
    Finish = Endcol2.button('Finish', on_click = clicked)
    while Finish == False:
        mins, secs = divmod(st.session_state['time_stamp'], 60)
        ph.metric("Countdown", f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state['time_stamp'] += 1