# Imports
import streamlit as st
import numpy as np
from PIL import Image
import json
# Importing Files
import QuizGiver as QG


# Importing Files
# Imports

def app():
    st.title('Feedback')
    col1,colx, col2 = st.columns([5, 3, 5])
    col3, coly, col4 = st.columns([5, 3, 5])
    Name_Of_Cartogram = ['Choropleth Map', 'Contiguous Cartogram', 'Non-Contiguous Cartogram', 'Dorling cartogram']
    Parameters = ['Helpfulness', 'Acceptance', 'Readability', 'Overall Rating']
    ParamValues = {
        'Helpfulness': ['Not Helpful', 'Somewhat Helpful', 'Medium Helpful', 'Helpful', 'Super Helpful'],
        'Acceptance': ['Not Acceptable', 'Somewhat Acceptable', 'Medium Acceptable', 'Acceptable', 'Best Acceptable'],
        'Readability': ['Not Readable', 'Somewhat Readable', 'Medium Readable', 'Readable', 'Super Readable'],
        'Overall Rating': ['Worst', 'Bad', 'Medium', 'Better', 'Best']
    }
    # Cartogram 1
    col1.header(Name_Of_Cartogram[0])
    op11 = col1.select_slider(Parameters[0] + ' of ' + Name_Of_Cartogram[0], options=(ParamValues[Parameters[0]]))
    op12 = col1.select_slider(Parameters[1] + ' of ' + Name_Of_Cartogram[0], options=(ParamValues[Parameters[1]]))
    op13 = col1.select_slider(Parameters[2] + ' of ' + Name_Of_Cartogram[0], options=(ParamValues[Parameters[2]]))
    op14 = col1.select_slider(Parameters[3] + ' of ' + Name_Of_Cartogram[0], options=(ParamValues[Parameters[3]]))

    # Cartogram 2
    col2.header(Name_Of_Cartogram[1])
    op21 = col2.select_slider(Parameters[0] + ' of ' + Name_Of_Cartogram[1], options=(ParamValues[Parameters[0]]))
    op22 = col2.select_slider(Parameters[1] + ' of ' + Name_Of_Cartogram[1], options=(ParamValues[Parameters[1]]))
    op23 = col2.select_slider(Parameters[2] + ' of ' + Name_Of_Cartogram[1], options=(ParamValues[Parameters[2]]))
    op24 = col2.select_slider(Parameters[3] + ' of ' + Name_Of_Cartogram[1], options=(ParamValues[Parameters[3]]))

    # Cartogram 3
    col3.header(Name_Of_Cartogram[2])
    op31 = col3.select_slider(Parameters[0] + ' of ' + Name_Of_Cartogram[2], options=(ParamValues[Parameters[0]]))
    op32 = col3.select_slider(Parameters[1] + ' of ' + Name_Of_Cartogram[2], options=(ParamValues[Parameters[1]]))
    op33 = col3.select_slider(Parameters[2] + ' of ' + Name_Of_Cartogram[2], options=(ParamValues[Parameters[2]]))
    op34 = col3.select_slider(Parameters[3] + ' of ' + Name_Of_Cartogram[2], options=(ParamValues[Parameters[3]]))

    # Cartogram 4
    col4.header(Name_Of_Cartogram[3])
    op41 = col4.select_slider(Parameters[0] + ' of ' + Name_Of_Cartogram[3], options=(ParamValues[Parameters[0]]))
    op42 = col4.select_slider(Parameters[1] + ' of ' + Name_Of_Cartogram[3], options=(ParamValues[Parameters[1]]))
    op43 = col4.select_slider(Parameters[2] + ' of ' + Name_Of_Cartogram[3], options=(ParamValues[Parameters[2]]))
    op44 = col4.select_slider(Parameters[3] + ' of ' + Name_Of_Cartogram[3], options=(ParamValues[Parameters[3]]))

    Option = {
        'C1': [op11, op12, op13, op14],
        'C2': [op21, op22, op23, op24],
        'C3': [op31, op32, op33, op34],
        'C4': [op41, op42, op43, op44]}
    Submit = st.button('Submit Feedback')
    if Submit:
        #st.success(Option)
        st.balloons()
        return Option
    # st.write(Key)
    # st.write(Ans)

    # with open("Answer.txt", "w") as outfile:
    #    outfile.write(db)
    # json.dump(db, outfile, indent = 4)
    # st.write(Ans)


if __name__ == '__main__':
    app()
