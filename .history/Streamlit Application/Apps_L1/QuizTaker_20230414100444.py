import streamlit as st

#import pymongo as py

def app(Config):
    if "QuizDoc" not in st.session_state:
        st.session_state["QuizDoc"] = "Not Done"
    def change_Doc_State():
        st.session_state["QuizDoc"] = "Done"
    QuizDoc = st.file_uploader("Upload your Quiz Document here", on_change=change_Doc_State)
    #st.write(QuizDoc)s
    #timer(ts)
    return QuizDoc
    #firebase = pr.initialize_app(Config)
    #storage = pr.storage()
    #path_on_cloud = 'doc/config'
    #storage.child(path_on_cloud).put(QuizDoc)

    