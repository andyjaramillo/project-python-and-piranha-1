# test_db.py
#written by Caroline Silva to test data base

import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

#use an in-memeory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Blind model classes to test deb. Since we have a complete lost of all models, we do not need to recursilvey bind dependencies 
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        #Not strickly necessary since SQLite in-memory databases only live for the duration of the connection, and in the next step we close the connection ... but a good practice all the same
        test_db.drop_tables(MODELS)

        #Close connection to db
        test_db.close()

    def test_timeline_post(self):
        #create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        #TO DO: Get timeline posts and assert that they are correct
    
