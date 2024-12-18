from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,PyMongoError

# establish connection to MongoDB local server

class MyDB:

    def __init__(self):
        try:
            self.client = MongoClient('mongodb://localhost:27017/')
            self.db = self.client['text_assistant']
        except ConnectionFailure as e:
            print(f"Couldn't connect to Database: {e}")
        else:
            print('Successfully connected to Database!')
            self.collection = self.db['user_feedback']

    def insert_feedback(self, name, qa_feedback, qa_rating, summarization_feedback, summarization_rating,
                        translation_feedback, translation_rating, additional_comments):
        try:
            feedback_data = {
                'name': name,
                'qa_feedback': qa_feedback,
                'qa_rating': qa_rating,
                'summarization_feedback': summarization_feedback,
                'summarization_rating': summarization_rating,
                'translation_feedback': translation_feedback,
                'translation_rating': translation_rating,
                'additional_comments': additional_comments
            }
            # Insert feedback into the collection
            self.collection.insert_one(feedback_data)
            return "Feedback Submitted Successfully!"
        except PyMongoError as e:
            print(f"An error occurred: {e}")
            return "Couldn't submit feedback to the Database"

# db = MyDB()
#
# print(db.insert_feedback('rohit', '1', '5', '1', '5', '1', '5', 'No'))