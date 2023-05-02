import streamlit as st

def app(Section):
    st.title(f"Section {Section}")
    st.success('Enjoy Break')
    st.balloons()
    #st.snow()


if __name__ == '__main__':
    app(1)