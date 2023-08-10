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
        st.markdown("<h1 style='text-align: center;'> Welcome to Map Evaluation Portal </h1>", unsafe_allow_html=True)
        #st.header('Welcome to Map Evaluation Portal')
        file_ = open("WelcomePage.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="700">',
            unsafe_allow_html=True,
        )

        st.markdown("<h3 style='text-align: center; color: grey;'>Hello</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: grey;'>Everyone!</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: grey;'>We're excited to have you participate in our survey on cartogram evaluation.</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: grey;'>Your insights and opinions are invaluable as we delve into the world of geographic visualization.</h5>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([2, 1, 1])
        Save = col2.button('Proceed To Guidelines', on_click=click)
        if Save:
            st.empty()
    #Start = st.session_state['Start']
    Proceed = st.session_state['Proceed']
    if Proceed:
        st.session_state['Proceed'] = 1
        return 1
    else:
        return 0

    