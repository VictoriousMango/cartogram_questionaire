import base64

import streamlit as st
def app():
    if 'Proceed' not in st.session_state:
        st.session_state['Proceed'] = 0
    #if 'Key' not in st.session_state:
        #st.session_state['Key'] = ''

    def click():
        st.session_state['Proceed'] = 1
    ph = st.empty()
    #Key = ''
    #Start = 0
    if st.session_state['Proceed'] == 0:
        #with ph.contianer():
        st.title('Welcome to Cartogram Evaluation Portal')
        st.image('WelcomePage.gif')
        Save = st.button('Proceed', on_click=click)
        if Save:
            st.empty()
    #Start = st.session_state['Start']
    Proceed = st.session_state['Proceed']
    return Proceed

    