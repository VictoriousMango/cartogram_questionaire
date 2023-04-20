import streamlit as st
def app():
    if 'Start' not in st.session_state:
        st.session_state['Start'] = 0
    Start = 0
    st.title('Welcome User')
    Name = st.text_input('Enter Your Name')
    Email = st.text_input('Enter Your Email Address')
    Key = Name + Email
    Save = st.button('Save')
    if Save:
        Start = 0
    else: 
        Start = 1
    return (Start)
    