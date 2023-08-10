import base64

import streamlit as st
def app():
    if 'MoveForward' not in st.session_state:
        st.session_state['MoveForward'] = 0
    #if 'Key' not in st.session_state:
        #st.session_state['Key'] = ''

    def click():
        st.session_state['MoveForward'] = 1
    ph = st.empty()
    #Key = ''
    #Start = 0
    if st.session_state['MoveForward'] == 0:

        st.markdown("<h5 style='text-align: center; color: grey;'>Cartogram is a Thematic map of a set of features (countries, provinces, etc.), in which their geographic size is altered which is directly proportional to a selected ratio-level variable, such as travel time, population, or GNP. </h5>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: grey;'>       to be directly proportional to a selected ratio-level variable, such as travel time, population, or GNP. </h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: grey;'>                                Your responses are appreciated. Feel free to answer without any stress.</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: grey;'>                                                   You can take <u><i>BREAK</i></u> in every section</h6>", unsafe_allow_html=True)

        Save = st.button('MoveForward', on_click=click)
        if Save:
            st.empty()
    #Start = st.session_state['Start']
    MoveForward = st.session_state['MoveForward']
    if MoveForward:
        st.session_state['MoveForward'] = 1
        return 1
    else:
        return 0

    