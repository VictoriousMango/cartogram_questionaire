import streamlit as st


def app():
    if 'Start' not in st.session_state:
        st.session_state['Start'] = 0
    if 'Key' not in st.session_state:
        st.session_state['Key'] = 0
    if 'Name' not in st.session_state:
        st.session_state['Name'] = 0
    if 'Email' not in st.session_state:
        st.session_state['Email'] = 0
    if 'Gender' not in st.session_state:
        st.session_state['Gender'] = 0
    if 'Age' not in st.session_state:
        st.session_state['Age'] = 0
    if 'UPPeople' not in st.session_state:
        st.session_state['UPPeople'] = 0
    if 'Address' not in st.session_state:
        st.session_state['Address'] = 0
    if 'NOS' not in st.session_state:
        st.session_state['NOS'] = 0
    if 'NOB' not in st.session_state:
        st.session_state['NOB'] = 0
    if 'EduQual' not in st.session_state:
        st.session_state['EduQual'] = 0
    if 'CartoIdea' not in st.session_state:
        st.session_state['CartoIdea'] = 0
    def click():
        st.session_state['Start'] = 1

    ph = st.empty()
    # Key = ''
    # Start = 0
    # (Key, Name, Email, Gender, Age, UPPeople, Address, NOS, NOB, EduQual, CartoIdea) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if st.session_state['Start'] == 0:
        ShowContainer = st.container()
        with ShowContainer:
            # with ph.contianer():
            st.title('Welcome User')
            st.session_state['Name'] = st.text_input('Enter Your Name')
            st.session_state['Email'] = st.text_input('Enter Your Email Address')
            st.session_state['Gender'] = st.selectbox('Gender :', ['Male', 'Female', 'Others'])
            st.session_state['Age'] = st.text_input('Enter Your Age')
            st.session_state['UPPeople'] = st.selectbox('Are you from Uttar Pradesh', ['Yes', 'No'])
            st.session_state['Address'] = st.text_input('Enter Your Address (Mention only District and State name): ')
            st.session_state['NOS'] = st.text_input('Name of your School/College/Institution/Organization:')
            st.session_state['NOB'] = st.text_input('Name of Your Board/University')
            st.session_state['EduQual'] = st.selectbox('Your Highest Qualification: ', ['School', 'Graduation', 'Post-Graduation', 'Doctorate'])
            st.session_state['CartoIdea'] = st.selectbox('Do you have any idea about Cartogram mapping?', ['Yes', 'No'])
            st.session_state['Key'] = Name + Email
            Save = st.button('Save', on_click=click)
            if Save:
                st.empty()
    Start = st.session_state['Start']
    Key = st.session_state['Key']
    PersonalInfo = [
        st.session_state['Key'],
        st.session_state['Name'],
        st.session_state['Email'],
        st.session_state['Gender'],
        st.session_state['Age'],
        st.session_state['UPPeople'],
        st.session_state['Address'],
        st.session_state['NOS'],
        st.session_state['NOB'],
        st.session_state['EduQual'],
        st.session_state['CartoIdea']
    ]
    return (PersonalInfo, Start)
