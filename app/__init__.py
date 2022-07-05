import os
import sys
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
load_dotenv()

app = Flask(__name__)

# mydb=MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), 
# host=os.getenv("MYSQL_HOST"),
# port=3306
# )

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
# initialize mydb with a temporary testing in memeory database for testing
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(mydb)
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database=mydb
mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', pagetitle = 'Home')

@app.route('/blog/')
def blog(): 
    return render_template('blog.html', pagetitle = 'Blog')

@app.route('/aboutus/')
def aboutUs(): 
    return render_template('aboutUs.html', pagetitle = 'About Us')

@app.route('/contact-us/')
def contactUs(): 
    return render_template('contactPage.html')

@app.route('/hobbies/')
def hobbies(): 
    return render_template('hobbies.html', pagetitle = 'Hobbies')

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
	name = request.form['name']
	email = request.form['email']
	content = request.form['content']
	timeline_post = TimelinePost.create(name=name, email=email, content=content)
	return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return{
        'timeline_posts':[
	    model_to_dict(p)
	    for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
	]
    }

@app.route('/timeline', methods=['POST', 'GET'])
def timeline():
    data = get_time_line_post()
    return render_template('timeline.html', pagetitle="Timeline", data=data)
