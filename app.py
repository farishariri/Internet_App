from flask import Flask, render_template, session
from flask.json import jsonify




# from flask_mail import Mail, Message 
import os

# mail = Mail()
app = Flask(__name__)
# mail.init_app(app)
# app.config.from_mapping(config)
# cache = Cache(app)
app.secret_key = 'fbd1eefad885bf835e1d5ea884244221'

posts = [
    {
        'Name': 'Sam',
        'Age': '23',
        'id': '0',
    },
    {
        'Name': 'Mohammed',
        'Age': '27',
        'id': '1',
    },
    {
        'Name': 'Jack',
        'Age': '25',
        'id': '2',
    },
    {
        'Name': 'Mark',
        'Age': '21',
        'id': '3',
    }

]

from json import dumps

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html', title= "Home Page", myposts=posts )


@app.route("/post/")
def json_posts():
    return dumps(posts)



@app.route("/post/<int:post_id>")
def post(post_id):
    if post_id < len(posts):
        p = posts[post_id]
        pv = [p['Name'], p['Age']]
        return render_template("post.html", title="Post", myposts = pv)
    else:
        return render_template('404.html')




# @app.route('/conatact', methods=['post'])
# def send_reset_email(user_email):

#    msg = Message('email title',
#                  sender = 'noreply@demo.com',
#                  recipients = [user_email] )

#    msg.body = f'''
#    	Hello { user_email }
#    '''
#    mail.send(msg)



@app.route("/about")
def about():
    return render_template('about.html', title= "About US")

@app.route("/contact")
def contact():
    return render_template('contact-us.html', title= "Contact US")

@app.route('/set/')
def set():
    session['current_user'] = 'ahemd'
    return "ok, current user is {session['current user']}"

@app.route('/get/')
def get():
    c= session.get('current user','Unknown')
    return "current user = {c}"

@app.route('/pop/')
def pop():
    c= session.pop('current user')
    return "current user is removed"
    
    
import os 
from waitress import serve

p = os.environ.get('PORT')
p = '5099' if p == None else p

serve(app, host='0.0.0.0', port=p)
