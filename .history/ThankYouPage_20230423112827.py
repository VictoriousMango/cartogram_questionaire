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
    with open("Answer.json", 'r') as read:
          db = json.load(read)
          db[Key] = Ans
    with open("Answer.json", "w") as outfile:
        json.dump(db, outfile, indent = 4)
    st.write(Ans)