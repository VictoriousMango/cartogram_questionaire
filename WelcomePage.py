import streamlit as st
def app():
    def click():
        pass
    st.title('Welcome User')
    Name = st.text_input('Enter Your Name')
    Email = st.text_input('Enter Your Email Address')
    st.button('Save', on_click=click)
    return (Name, Email)