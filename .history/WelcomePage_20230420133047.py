import streamlit as st
def app():
    if 'Start' not in st.session_state:
        st.session_state['Start'] = 0

    def click():
        st.session_state['Start'] = 1
    tmp = st.empty()
    st.title('Welcome User')
    Name = tmp.text_input('Enter Your Name')
    Email = tmp.text_input('Enter Your Email Address')
    Key = Name + Email
    Save = tmp.button('Save', on_click=click)
    if Save:
        st.empty()
    Start = st.session_state['Start']
    return(Key, Start)
    