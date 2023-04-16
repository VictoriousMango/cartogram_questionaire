import streamlit as st
from PIL import Image
import numpy as np
#from matplotlib.image import imread
#import matplotlib.pyplot as plt
import time

def timer(ts):
    with st.empty():
      while ts < 100:
        mins, secs = divmod(ts, 60)
        time_now = '{:02d}:{:02d}'.format(mins, secs)
        st.markdown(time_now)
        time.sleep(1)
        ts += 1 

def app(QuizDoc, time_stamp):
    col1, col2 = st.columns([6, 4])
    if 'Answer' not in st.session_state:
        st.session_state['Answer'] = 0
    if 'AnswerList' not in st.session_state:
        st.session_state['AnswerList'] = dict()
    if 'Index' not in st.session_state:
        st.session_state['Index'] = 0

    raw_text = {1:[]}
    Answered = dict()
    Questionaire = dict()
    count = 1
    Esc_Char = 'break'
    for i in QuizDoc.readlines():
        temp = str(i) 
        if Esc_Char in temp:
            #st.write('Found Escape Character')
            count += 1
            raw_text[count] = []
            #Answered[count] = []
        else:    
            #st.write(temp)
            raw_text[count].append(temp)
            #st.write(temp)
        #i = str(i,"utf-8")
        #if 'break' in i:
        #    count += 1
        #raw_text[count].append(str(i,"utf-8")) # works with st.text and st.write,used for further processing

                # st.text(raw_text) # Work
        
    switch = 0
    for i in raw_text:
        switch = 1
        Question = ''
        A = ''
        B = ''
        C = ''
        D = ''
        for j in raw_text[i]:
            if 'A)' in j:
                switch = 0
                A += j
            if 'B)' in j:
                B += j
            if 'C)' in j:
                C += j
            if 'D)' in j:
                D += j
            if switch:
                Question += j
        Questionaire[Question] = [A, B, C, D]

    count = 1
    Ques = []
    for i in Questionaire:
        Ques.append(i)
    #ts = 0

    for Index in range(len(Ques)):
        pass
    #Index = 0
    Save = col1.button("Save for Q " + str(st.session_state['Index'] + 1))
    def Questions(Index):
        st.empty()
        st.write()
        col1.write('-----------------------------------------------------------')
        st.session_state['Answer'] = col1.radio(Ques[Index], Questionaire[Ques[Index]])
        img_src = 'Images/1.jpg'
        img = Image.open(img_src)
        arr = np.array(img)
        #img = imread(img_src)\
        col1.write('-----------------------------------------------------------')
        st.write()
        col2.image(arr)
    

    

    if Save:
        st.empty()
        st.session_state['AnswerList'][st.session_state['Index'] + 1] = [st.session_state['Answer'][0], time_stamp]
        #st.write(st.session_state['Answer'])
        
        if st.session_state['Index'] < len(Ques) - 1:
            st.session_state['Index'] += 1
            #Questions(st.session_state['Index'])
    
    Questions(st.session_state['Index'])
    
    #timer(ts)

    #def AppScreen(ques, count, Index, Ques):
    #    st.empty()
    #    Save = False
    #    #for j in Questionaire[i]:
    #    #    st.write(j)
    #    st.write()
    #    st.write('-----------------------------------------------------------')
    #    #Answered[i] = st.selectbox("Choose Your Option", options = Option)
    #    Answered[count] = st.radio(ques, Questionaire[ques])[0]
    #    count += 1
    #    st.write('-----------------------------------------------------------')
    #    st.write()
    #    
    #    Save = st.button("Save for Question " + ques[1])
    #    
    #   ts = 0
    #    with st.empty():
    #        while Save == False:
    #            mins, secs = divmod(ts, 60)
    #            time_now = '{:02d}:{:02d}'.format(mins, secs)
    #            st.header(time_now)
    #            time.sleep(1)
    #            ts += 1 

    #    if Save:
    #        Index += 1
    #        if Index < len(Ques):
    #            AppScreen(Ques[Index], count, Index, Ques)
    
    ques = Ques[Index]
    #AppScreen(ques, count, Index, Ques)
    # To Review Answers.
    #for i in Answered:
    #    st.write(Answered[i])

    return st.session_state['AnswerList']
    #Answer = st.selectbox('Enter you choice', options = Option)
    #Next = st.button("Next")
    #st.write("Found Break")
            #if Next:
            #    Next = False
            #    raw_text = []
            #else:
                #while True:
            #        pa
            



    #col1, col2, col3 = st.columns([2, 2, 1])
    #col1.markdown('# Questions Tracker')
    #col2.markdown('# Questions with Choices')
    #col3.markdown('# Additional Space')