import streamlit as st


def app():
    if 'Start' not in st.session_state:
        st.session_state['Start'] = 0
    if 'Key' not in st.session_state:
        st.session_state['Key'] = 0

    def click():
        st.session_state['Start'] = 1

    ph = st.empty()
    # Key = ''
    # Start = 0
    if st.session_state['Start'] == 0:
        # with ph.contianer():
        st.title('Welcome User')
        Name = st.text_input('Enter Your Name')
        Email = st.text_input('Enter Your Email Address')
        Gender = st.selectbox('Gender :', ['Male', 'Female', 'Others'])
        Age = st.text_input('Enter Your Age')
        UPPeople = st.slider('Are you from Uttar Pradesh', 0, 1)
        Address = st.text_input('Enter Your Address (Mention only District and State name): ')
        NOS = st.text_input('Name of your School/College/Institution/Organization:')
        NOB = st.text_input('Name of Your Board/University')
        EduQual = st.selectbox('Your Highest Qualification: ', ['School', 'Graduation', 'Post-Graduation', 'Doctorate'])
        CartoIdea = st.slider('Do you have any idea about Cartogram mapping?', ['Yes', 'No'])
        st.session_state['Key'] = Name + Email
        Save = st.button('Save', on_click=click)
        if Save:
            st.empty()
    Start = st.session_state['Start']
    Key = st.session_state['Key']
    PersonalInfo = [Key, Name, Email, Gender, Age, UPPeople, Address, NOS, NOB, EduQual, CartoIdea]
    return (PersonalInfo, Start)
