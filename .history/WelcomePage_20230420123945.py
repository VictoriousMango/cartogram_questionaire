import streamlit as st
def app():
    st.title('Welcome User')
    Name = st.text_input('Enter Your Name')
    Email = st.text_input('Enter Your Email Address')
    Save = st.button('Save')
    if Save:
        return(Name, Email, Save)
    