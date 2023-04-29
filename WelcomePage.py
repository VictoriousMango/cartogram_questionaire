import base64

import streamlit as st
def app():
    if 'Start' not in st.session_state:
        st.session_state['Start'] = 0
    if 'Key' not in st.session_state:
        st.session_state['Key'] = ''

    def click():
        st.session_state['Start'] = 1
    ph = st.empty()
    #Key = ''
    #Start = 0
    if st.session_state['Start'] == 0:    
        #with ph.contianer():
        st.title('Welcome to Cartogram Evaluation Portal')
        file_ = open("WelcomePage.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.image(
            data_url,  # I prefer to load the GIFs using GIPHY
            width=400, # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )
        Save = st.button('Proceed', on_click=click)
        if Save:
            st.empty()
    #Start = st.session_state['Start']
    #Key = st.session_state['Key']
    