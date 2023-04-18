# Imports
import streamlit as st
import numpy as np
from PIL import Image
import time
# Importing Files
import QuizGiver as QG
# Importing Files
# Imports

def app():

   # Session States
   if 'time_stamp' not in st.session_state:
      st.session_state['time_stamp'] = 0
   if 'QuizDoc' not in st.session_state:
      st.session_state['QuizDoc'] = 0
   # End Session States

   #Global Variables
   st.session_state['QuizDoc'] = 'Questions.txt'
   #Global Variables

   # Test Functions
   def clicked():
      st.write('Finished')
      

   # Test Functions

   # Title Bar
   col1, col2 = st.columns([6, 4])
   col1.title("Cartogram Assessment")
   ph = col2.empty()
   # Title Bar

   #Columns Part 2
   Endcol1, Endcol2 = st.columns([6, 4])
   #Columns Part 2
   Finish = Endcol2.button('Finish', on_click = clicked)

   if st.session_state['QuizDoc']:  
      def Quizzer():
         Ans = QG.app(st.session_state['QuizDoc'], st.session_state['time_stamp'])
         return Ans
      Ans = Quizzer()

   while Finish == False:
      mins, secs = divmod(st.session_state['time_stamp'], 60)
      ph.metric("Countdown", f"{mins:02d}:{secs:02d}")
      time.sleep(1)
      st.session_state['time_stamp'] += 1
   if Finish:
      return st.write('Thank You')

app()
   # Doc to Quiz