# Imports
import streamlit as st
import numpy as np
from PIL import Image
import json
# Importing Files
import QuizGiver as QG
# Importing Files
# Imports

def app(Key, Ans):
    st.header('Thank You For Your Patience')
    st.write(Ans)
    #with open("Answer.txt", 'r') as file:
    #      db = file.read()
    #      db += ', '
    #with open("Answer.txt", "w") as outfile:
    #    outfile.write(db)
        #json.dump(db, outfile, indent = 4)
    st.write(Ans)