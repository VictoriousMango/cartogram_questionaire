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
        file_ = open("WelcomePage.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="700">',
            unsafe_allow_html=True,
        )
        Save = st.button('Proceed', on_click=click)
        if Save:
            st.empty()
    #Start = st.session_state['Start']
    Proceed = st.session_state['Proceed']
    return Proceed

    