from applications import app
from collections import User, Posts
from flask import session, render_template, redirect, flash, url_for, request

@app.route('/post')
<<<<<<< HEAD
def posts():

    if not session.get('logged_in'):
        return redirect(url_for('login')) '''If the user tries to post and is not logged in, redirects them to login. '''

    body = request.form["data"]
    title = request.form["title"]
    p = Posts(author = user, title = title, content = body)
    p.save() 
=======
def Posts():
    
>>>>>>> 0443485b4fe9f886520b4616cc5089a10154072b
