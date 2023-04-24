import pymongo
# from google.cloud import firestore
import pyrebase
import streamlit as st
import json


def app(Key, Ans):
    '''
    client = pymongo.MongoClient('mongodb+srv://yadashesh:yadashesh@cluster0.lqsjbx0.mongodb.net/CartogramAssessment')
    db = client['CartogramAssessment']
    # collection = db['Answers']
    posts = db.Answers
    post_id = posts.insert_one({Key: str(Ans)}).inserted_id
    print(post_id)
    st.write('Answers Saved')
    '''
    with open("DataBase.json", 'r') as readfile:
        db = json.load(readfile)
        db[Key] = Ans
    with open("DataBase.json", "w") as outfile:
        json.dump(db, outfile, indent=4)
    st.write('Answers Saved Successfully')

if __name__ == '__main__':
    print('Welcome To Pymongo')
    # client = pymongo.MongoClient()
    # app()
