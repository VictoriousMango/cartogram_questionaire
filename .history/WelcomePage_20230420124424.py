import streamlit as st
def app():
    st.title('Welcome User')
    Name = st.text_input('Enter Your Name')
    Email = st.text_input('Enter Your Email Address')
    Save = st.button('Save')
    return(Name, Email, True)
    