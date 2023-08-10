import base64

import streamlit as st
def app():
    if 'MoveForward' not in st.session_state:
        st.session_state['MoveForward'] = 0
    #if 'Key' not in st.session_state:
        #st.session_state['Key'] = ''

    def click():
        st.session_state['MoveForward'] = 1
    ph = st.empty()
    #Key = ''
    #Start = 0
    if st.session_state['MoveForward'] == 0:
        st.title('Guidelines')
        '''
        Instructions:
        Question Pattern: This survey has four sections, like Choropleth Map, Contiguous Cartogram, Non-Contiguous Cartogram and Dorling Cartogram. Each section focuses on a specific type of Map and its effectiveness. This survey is composed of 140 questions, with each section containing 35 questions.
        Avoid Glitches:  If any glitches come during the survey don’t click on Refresh. Just click on ‘Hide Assessment’ then click ‘Show Assessment.’
        Relax and Feel at Ease: There's no need to feel stressed. This survey is meant to gather your thoughts and opinions, so take your time and answer at your own pace.
        Your Views Matter: Your personal views and opinions are what we're interested in. There are no right or wrong answers. We value the unique perspectives you bring to the table.
        Honest Responses: Please provide honest responses. Your genuine feedback helps us gain a better understanding of how different map techniques are perceived and utilized.
        Complete all the Sections: We encourage you to complete all sections of the survey to provide a comprehensive perspective on different cartogram techniques.
        Submit Feedback: Please fill in the Feedback section at the end of the questions.
        Contact: If you have any questions or concerns about the survey, feel free to contact Satyam Mishra at  \n Phone Number : 6289926460 \nEmail ID : Satyam.mishra22@st.niituniveristy.in..
        '''
        Guidelines = {
            "Question Pattern": "This survey has four sections, like Choropleth Map, Contiguous Cartogram, Non-Contiguous Cartogram and Dorling Cartogram. Each section focuses on a specific type of Maps and its effectiveness. This survey is composed of 140 questions, with each section containing 35 questions.",
            "Avoid Glitches":  "If any glitches come during the survey don’t click on Refresh. Just click on ‘Hide Assessment’ then click ‘Show Assessment.’",
            "Relax and Feel at Ease": "There's no need to feel stressed. This survey is meant to gather your thoughts and opinions, so take your time and answer at your own pace.",
            "Your Views Matter": "Your personal views and opinions are what we're interested in. There are no right or wrong answers. We value the unique perspectives you bring to the table.",
            "Honest Responses": "Please provide honest responses. Your genuine feedback helps us gain a better understanding of how different map techniques are perceived and utilized.",
            "Complete all the Sections": "We encourage you to complete all sections of the survey to provide a comprehensive perspective on different map techniques.",
            "Submit Feedback": "Please fill in the Feedback section at the end of all questions.",
            "Contact": "If you have any questions or concerns about the survey, feel free to contact Satyam Mishra at"
        }
        keys = list(Guidelines.keys())
        for i in range(len(keys)):
            with st.expander(keys[i], expanded=False):
                st.markdown(f"<h3 style='text-align: center; color: grey;'>{keys[i]}</h3>", unsafe_allow_html=True)
                st.write(Guidelines[keys[i]])
                st.markdown(f"<h6 style='text-align: justify; color: grey;'>{Guidelines[keys[i]]}</h6>", unsafe_allow_html=True)
                if i == len(keys) - 1:
                    col1, col2 = st.columns([1, 1])
                    col1.write('Phone Number : ')
                    col2.write('6289926460')
                    col1.write('Email ID : ')
                    col2.write('Satyam.mishra22@st.niituniveristy.in')
        #
        #st.markdown("<h6 style='text-align: center; color: grey;'></h6>", unsafe_allow_html=True)
        #st.markdown("<h6 style='text-align: center; color: grey;'></h6>", unsafe_allow_html=True)
        #st.markdown("<h6 style='text-align: center; color: grey;'></h6>", unsafe_allow_html=True)

        Save = st.button('Proceed', on_click=click)
        if Save:
            st.empty()
    #Start = st.session_state['Start']
    MoveForward = st.session_state['MoveForward']
    if MoveForward:
        st.session_state['MoveForward'] = 1
        return 1
    else:
        return 0

    