import streamlit as st
def app():
    if 'Start' not in st.session_state:
        st.session_state['Start'] = 0

    def click():
        st.session_state['Start'] = 1
        st.empty()
    st.title('Welcome User')
    Name = st.text_input('Enter Your Name')
    Email = st.text_input('Enter Your Email Address')
    Key = Name + Email
    Save = st.button('Save', on_click=click)
    Start = st.session_state['Start']
    return(Key, Start)
    