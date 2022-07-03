# tests/test_app.py
import json
import unittest
import unittest.mock
import os
import urllib.request
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>John & Andy</title>" in html
        #TO DO Add more tests relating to the home page 
        #assert urllib.request.url2pathname("http://project-python-and-piranha.duckdns.org:5000/") # checking duck dns url works

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        test_post = {'name': ' Doe', 'email': 'john@example.com','content': ' world, I\'m Jane!'}
        timeline = self.client.get("/timeline")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        #TO DO Add more test relating to /api/timeline_post GET and POST apis
        #checking POST
        post = self.client.post("/api/timeline_post", data=test_post)
        self.assertEqual(post.status_code, 200)
        assert timeline.status_code ==200
        #TO DO Add more test relating to timeline page 
    @unittest.skip("TBD")
    def test_malformed_timeline_post(self):
        #POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@email.com", "content": "Hello world, I'm John"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Name" in html

        #POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": "Hello"})
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        #POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Does", "email": "email@john.com", "content": "Hello world, I'm John"})
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

