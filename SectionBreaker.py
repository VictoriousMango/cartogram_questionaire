import streamlit as st

def app(Section, Flag):
    ph = st.container()
    if Flag:
        ph = st.container()
        with ph:
            st.title(f"Section {Section}")
            st.success('Enjoy Break')
            st.balloons()
            #st.snow()


if __name__ == '__main__':
    app(1)