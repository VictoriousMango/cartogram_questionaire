import pymongo
# from google.cloud import firestore
import pyrebase
import streamlit as st
from deta import Deta


# Key : d0md8swdtzk_E7a3CqxYWfgL1E426fiH3gaBBSR2HgL6

def app(PersonalInfo, Ans, Feedback):

    # Load the environment variables
    DETA_KEY = 'd0md8swdtzk_E7a3CqxYWfgL1E426fiH3gaBBSR2HgL6'

    # Initialize with a project key
    deta = Deta(DETA_KEY)

    # This is how to create/connect a database
    db = deta.Base("CartogramANS")

    def insert_ans(PersonalInfo, Ans, Feedback):
        """Returns the report on a successful creation, otherwise raises an error"""
        return db.put({"key": PersonalInfo[0], "Answers": Ans, 'Personal Info': PersonalInfo[1:], 'Feedback': Feedback})

    def fetch_all_periods():
        """Returns a dict of all periods"""
        res = db.fetch()
        return res.items

    def get_period(period):
        """If not found, the function will return None"""
        return db.get(period)
    st.write('Hello')
    st.write(PersonalInfo, Ans, Feedback)
    # insert_ans(PersonalInfo, Ans, Feedback)
    st.success('Answers Saved Successful')
    return 1
    '''
    client = pymongo.MongoClient('mongodb+srv://yadashesh:yadashesh@cluster0.lqsjbx0.mongodb.net/CartogramAssessment')
    db = client['CartogramAssessment']
    # collection = db['Answers']
    posts = db.Answers
    post_id = posts.insert_one({Key: str(Ans)}).inserted_id
    print(post_id)
    st.write('Answers Saved')
    '''
    '''
    with open("Answer.json", 'r') as readfile:
        db = json.load(readfile)
        db[Key] = Ans
    with open("Answer.json", "w") as outfile:
        json.dump(db, outfile, indent=4)
    st.write('Answers Saved Successfully')
    '''


if __name__ == '__main__':
    print('Welcome To Deta')
    app('Key', 'Answers to the given question')
    # client = pymongo.MongoClient()
    # app()
