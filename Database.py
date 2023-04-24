import pymongo
# from google.cloud import firestore
import pyrebase
import streamlit as st


def app(Key, Ans):
    client = pymongo.MongoClient('mongodb+srv://yadashesh:yadashesh@cluster0.lqsjbx0.mongodb.net/CartogramAssessment')
    db = client['CartogramAssessment']
    # collection = db['Answers']
    posts = db.Answers
    post_id = posts.insert_one({Key: str(Ans)}).inserted_id
    print(post_id)
    st.write('Answers Saved')


if __name__ == '__main__':
    print('Welcome To Pymongo')
    # client = pymongo.MongoClient()
    # app()
