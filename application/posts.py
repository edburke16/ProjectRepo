from applications import app
from collections import User, Posts
from flask import session, render_template, redirect, flash, url_for, request

@app.route('/post')
def posts():

    if not session.get('logged_in'):
        return redirect(url_for('login')) '''If the user tries to post and is not logged in, redirects them to login. '''

    body = request.form["data"]
    title = request.form["title"]
    p = Posts(author = user, title = title, content = body)
    p.save()

    return render_template('post.html')
