import streamlit as st

#import pymongo as py

def app(Config):
    if "UserName" not in st.session_state:
        st.session_state["UserName"] = "Not Done"
    def change_Text_State():
        st.session_state["UserName"] = "Done"
    QuizDoc = st.text_input("Enter Your Name", on_change=change_Text_State)
    #st.write(QuizDoc)s
    #timer(ts)
    if st.session_state["UserName"] == "Done":
        return QuizDoc
    #firebase = pr.initialize_app(Config)
    #storage = pr.storage()
    #path_on_cloud = 'doc/config'
    #storage.child(path_on_cloud).put(QuizDoc)

    