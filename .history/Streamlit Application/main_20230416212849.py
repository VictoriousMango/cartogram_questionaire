import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
import json
#from googleapiclient.discovery import build
#from google.oauth2 import service_account

#from MultiApp import MultiApp
import Apps_L1.QuizGiver as QuizGiver
import Apps_L1.QuizTaker as QuizTaker
import Apps_L1.ImageImporter as ImgImport
import time

st.set_page_config()
col1, col2 = st.columns([8, 2])
ph = col2.empty()


# Try 2
if 'time_stamp' not in st.session_state:
   st.session_state['time_stamp'] = 0 
if 'QuizDoc' not in st.session_state:
   st.session_state['QuizDoc'] = []
if 'ImageDoc' not in st.session_state:
   st.session_state['ImageDoc'] = 0
# End Try 2


#col1.markdown('# Questions Tracker')
#col2.markdown('# Questions with Choices')
#col3.markdown('# Additional Space')

Config = {
  'apiKey': "AIzaSyBNXwH8oupVOdArox5ObhxDlsglQnxkRqA",
  'authDomain': "questionaire-262a9.firebaseapp.com",
  'projectId' : "questionaire-262a9",
  'storageBucket' : "questionaire-262a9.appspot.com",
  'messagingSenderId' : "524743361299",
  'appId' : "1:524743361299:web:1d474a59341485640bd0e6",
  'measurementId' : "G-S5H7M94WYT"
};

#app = MultiApp()

col1.title("Questionaire for Assessment")

# Functions
def saved(Index, Answer):
    with st.sidebar:
      st.write(Index + 1, '  :  ', Answer[0], ' -> ', st.session_state['time_stamp'])
# End of Function

#UserType = st.selectbox('What is your use for this web application : ', options = options)
Options = ['Quiz Taker', 'Quiz Giver']
QuizStart = 0
Answers = []
Ans = 0
Total_Time = []
st.sidebar.header("Welcome User")
with st.sidebar:
    #st.session_state['ImageDoc'] = ImgImport.app(Config)
    Name = QuizTaker.app(Config)
    st.session_state['QuizDoc'].append(Name)
    

      
          

      
      #UserType = st.selectbox('What is your use for this web application : ', options = Options)
      #if UserType == 'Quiz Taker':
      #    QuizStart = 0
      #else:
      #    QuizStart = 1
Finish = False


if len(st.session_state['QuizDoc'])>0:
    col21, col22, col23 = st.columns([1, 1, 1])
    
    def Quizzer():
      Index = 0
      st.session_state['QuizDoc'] = open('Questionaire Doc\Questions.txt', 'r')
      Ans = QuizGiver.app(st.session_state['QuizDoc'], st.session_state['time_stamp'])
      return Ans
      
    Ans = Quizzer()
    #Save = col21.button("Save")
    #Next = col22.button("Next")
    Finish = col23.button("Finish")

    count = -1
    #if Save:
    #    #Ans = Quizzer(count, Config, st.session_state['QuizDoc'])
    #    Answers.append(Ans)
    #    saved(1, Ans)

    #if Next:
    #    st.session_state['time_stamp'] = 0
    #    count += 1
    #    #st.write(Index)
    #    if count < 2:
    #      st.write(st.session_state['QuizDoc'])

    if Finish:
      st.empty()
      st.write('Finish')
      with st.sidebar:
         st.write(Ans)
         with open("Database.txt", "a") as db:
          #Ans = st.session_state['QuizDoc']
          db.write(st.session_state['QuizDoc'][0])
          db.write(json.dumps(st.session_state['QuizDoc'], indent=4))
         #st.write(jsonObject)
      st.write()


    if st.session_state['QuizDoc']:
        #pass
        while Finish == False:
          mins, secs = divmod(st.session_state['time_stamp'], 60)
          ph.metric("Countdown", f"{mins:02d}:{secs:02d}")
          time.sleep(1)
          st.session_state['time_stamp'] += 1

#with st.sidebar:
#def saved(Index, Answer):
#    st.write(Index, '  :  ', Answer[0])#, ' -> ', Total_Time[i])
 



#if QuizStart:
#    QuizGiver.app(Config)
#else:
#    QuizTaker.app(Config)
