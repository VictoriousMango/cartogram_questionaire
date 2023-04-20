import streamlit as st
def app():
    st.title('Welcome User')
    Name = st.text_input('Enter Your Name')
    Email = st.text_input('Enter Your Email Address')
    Key = Name + Email
    Save = False
    Save = st.button('Save')
    return(Key, Save)
    