# Initial Imports
import streamlit as st
import numpy as np
from PIL import Image
import QuizGiver as QG
import time
# Initial Imports

# Session States
if 'time_stamp' not in st.session_state:
   st.session_state['time_stamp'] = 0
if 'QuizDoc' not in st.session_state:
   st.session_state['QuizDoc'] = 0

# End Session States

# Test Functions
def clicked():
   st.write('Finished')
# Test Functions

# Title Bar
col1, col2 = st.columns([6, 4])
col1.title("Cartogram Assessment")
ph = col2.empty()
# Title Bar


# Doc to Quiz
Ans = QG.app(st.session_state['QuizDoc'], st.session_state['time_stamp'])
Endcol1, Endcol2 = st.columns([8, 2])
Finish = Endcol2.button('Finish', on_click = clicked)

if st.session_state['QuizDoc']:
    #pass
    while Finish == False:
        mins, secs = divmod(st.session_state['time_stamp'], 60)
        ph.metric("Countdown", f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state['time_stamp'] += 1