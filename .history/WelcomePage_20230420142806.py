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
    if st.session_state['Start'] == 1:    
        with ph.contianer():
            st.title('Welcome User')
            Name = st.text_input('Enter Your Name')
            Email = st.text_input('Enter Your Email Address')
            st.session_state['Key'] = Name + Email
            Save = st.button('Save', on_click=click)
            if Save:
                st.empty()
    Start = st.session_state['Start']
    Key = st.session_state['Key']
    return(Key, Start)
    