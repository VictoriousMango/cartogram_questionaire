import streamlit as st
from PIL import Image
import numpy as np
# from matplotlib.image import imread
# import matplotlib.pyplot as plt
import time
import SectionBreaker as SB


def timer(ts):
    with st.empty():
        while ts < 100:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.markdown(time_now)
            time.sleep(1)
            ts += 1



def app(QuizDoc, time_stamp):
    col1, col11 = st.columns([9, 1])
    col2, col21 = st.columns([9, 1])
    col3, col31 = st.columns([1, 1])
    if 'Answer' not in st.session_state:
        st.session_state['Answer'] = 0
    if 'AnswerList' not in st.session_state:
        st.session_state['AnswerList'] = dict()
    if 'Index' not in st.session_state:
        st.session_state['Index'] = 0
    if 'SelfAnalysis' not in st.session_state:
        st.session_state['SelfAnalysis'] = 0
    if 'Section' not in st.session_state:
        st.session_state['Section'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    if 'SectionFlag' not in st.session_state:
        st.session_state['SectionFlag'] = 0





    # if st.session_state['Index'] == 7:
    # col3.empty()
    # Finish = col3.button('Finito')
    raw_text = {1: []}
    Answered = dict()
    Questionaire = dict()
    count = 1
    Esc_Char = 'break'
    with open(QuizDoc, 'r') as QD:
        for i in QD.readlines():
            temp = str(i)
            if Esc_Char in temp:
                # st.write('Found Escape Character')
                count += 1
                raw_text[count] = []
                # Answered[count] = []
            else:
                # st.write(temp)
                raw_text[count].append(temp)
            # st.write(temp)
        # i = str(i,"utf-8")
        # if 'break' in i:
        #    count += 1
        # raw_text[count].append(str(i,"utf-8")) # works with st.text and st.write,used for further processing

        # st.text(raw_text) # Work

    switch = 0
    for i in raw_text:
        switch = 1
        Question = ''
        A = ''
        B = ''
        C = ''
        D = ''
        E = ''
        F = ''
        G = ''
        H = ''
        I = ''
        Z = ''
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

            if 'E)' in j:
                E += j

            if 'F)' in j:
                F += j

            if 'G)' in j:
                G += j

            if 'H)' in j:
                H += j

            if 'I)' in j:
                I += j
            if 'Z)' in j:
                switch = 0
                Z += 'Take Break' + j
            if switch:
                Question += j
        Questionaire[Question] = ['Select Options']
        if Question != '':
            pass
            # Questionaire[Question].append(Question)
        if A != '':
            Questionaire[Question].append(A)
        if B != '':
            Questionaire[Question].append(B)
        if C != '':
            Questionaire[Question].append(C)
        if D != '':
            Questionaire[Question].append(D)
        if E != '':
            Questionaire[Question].append(E)
        if F != '':
            Questionaire[Question].append(F)
        if G != '':
            Questionaire[Question].append(G)
        if H != '':
            Questionaire[Question].append(H)
        if I != '':
            Questionaire[Question].append(I)
        if Z != '':
            Questionaire[Question].append(Z)

    count = 1
    Ques = []
    for i in Questionaire:
        Ques.append(i)
    # ts = 0

    for Index in range(len(Ques)):
        pass

    # Index = 0

    def Questions(Index):
            #SB.app((st.session_state['Index'] + 1)//36, (st.session_state['Index'] + 1) % 36 == 0)

            if st.session_state['Index'] < len(Ques):
                # st.empty()
                st.write()
                img_src = f'{Index}.png'
                try:
                    img = Image.open(img_src)
                    arr = np.array(img)
                except FileNotFoundError:
                    img_src = f'{Index}.jpg'
                try:
                    img = Image.open(img_src)
                    arr = np.array(img)
                except FileNotFoundError:
                    pass
                # img = imread(img_src)\
                col1.image(arr)
                if 'Section' in Ques[Index]:
                    st.session_state['SectionFlag'] = 1
                    #st.success(True)
                else:
                    st.session_state['SectionFlag'] = 0
                    #st.error(False)
                    col2.write('--------------------------------------------------------------')
                    st.session_state['SelfAnalysis'] = f"Q{st.session_state['Index'] + 1}) => Ans: {st.session_state['Answer']}"
    
                    st.session_state['Answer'] = col2.radio(Ques[Index], Questionaire[Ques[Index]])
    
                    img_src = f'{Index}.png'
                    try:
                        img = Image.open(img_src)
                        arr1 = np.array(img)
                    except FileNotFoundError:
                        img_src = f'{Index}.jpg'
                    try:
                        img = Image.open(img_src)
                        arr1 = np.array(img)
                    except FileNotFoundError:
                        pass
                    # img = imread(img_src)\
                    col2.write('-----------------------------------------------------------')
                    #try:
                        #col2.image(arr1)
                    #except:
                        #pass
                    # col2.write('-----------------------------------------------------------')
        
                    st.write('-----------------------------------------------------------')
                    st.write()

    if st.session_state['Index'] < len(Ques):
        if st.session_state['SectionFlag'] == 0:
            Save = col3.button("Save for Q " + str(st.session_state['Index']))
            # st.success(st.session_state['SelfAnalysis'])
            if Save:
                st.empty()
                st.session_state['AnswerList'][st.session_state['Index']] = [st.session_state['Answer'][0], time_stamp]
                st.success(f"Q{st.session_state['Index']}) : {st.session_state['AnswerList'][st.session_state['Index']][0]}")
                # st.write(st.session_state['Answer'])


                if st.session_state['Index'] < len(Ques):
                    st.session_state['Index'] += 1
        # Questions(st.session_state['Index'])
    # Finish = st.button('Finish Button Part 2')
        else:
            Next = st.button('Start Section ' + st.session_state['Section'][0])
            if Next:
                st.empty()
                st.session_state['Section'].pop(0)
                if st.session_state['Index'] < len(Ques):
                    st.session_state['Index'] += 1

        

    Questions(st.session_state['Index'])

    # timer(ts)

    # def AppScreen(ques, count, Index, Ques):
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
    # AppScreen(ques, count, Index, Ques)
    # To Review Answers.
    # for i in Answered:
    #    st.write(Answered[i])
    Ans = st.session_state['AnswerList']
    Index = st.session_state['Index']
    NumberOfQuestions = len(Ques)
    return (Ans, Index, NumberOfQuestions)
    # Answer = st.selectbox('Enter you choice', options = Option)
    # Next = st.button("Next")
    # st.write("Found Break")
    # if Next:
    #    Next = False
    #    raw_text = []
    # else:
    # while True:
    #        pa

    # col1, col2, col3 = st.columns([2, 2, 1])
    # col1.markdown('# Questions Tracker')
    # col2.markdown('# Questions with Choices')
    # col3.markdown('# Additional Space')
