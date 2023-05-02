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
    (Key, Name, Email, Gender, Age, UPPeople, Address, NOS, NOB, EduQual, CartoIdea) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if st.session_state['Start'] == 0:
        ShowContainer = st.container()
        with ShowContainer:
            # with ph.contianer():
            st.title('Welcome User')
            Name = ph.text_input('Enter Your Name')
            Email = ph.text_input('Enter Your Email Address')
            Gender = ph.selectbox('Gender :', ['Male', 'Female', 'Others'])
            Age = ph.text_input('Enter Your Age')
            UPPeople = ph.selectbox('Are you from Uttar Pradesh', ['Yes', 'No'])
            Address = ph.text_input('Enter Your Address (Mention only District and State name): ')
            NOS = ph.text_input('Name of your School/College/Institution/Organization:')
            NOB = ph.text_input('Name of Your Board/University')
            EduQual = ph.selectbox('Your Highest Qualification: ', ['School', 'Graduation', 'Post-Graduation', 'Doctorate'])
            CartoIdea = ph.selectbox('Do you have any idea about Cartogram mapping?', ['Yes', 'No'])
            st.session_state['Key'] = Name + Email
            Save = ph.button('Save', on_click=click)
            if Save:
                st.empty()
    Start = st.session_state['Start']
    Key = st.session_state['Key']
    PersonalInfo = [Key, Name, Email, Gender, Age, UPPeople, Address, NOS, NOB, EduQual, CartoIdea]
    return (PersonalInfo, Start)
