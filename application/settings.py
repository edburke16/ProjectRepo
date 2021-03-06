from application import app, collections
from flask import render_template, session, redirect, url_for
from collections import User
from os import urandom
import hashlib
from forms import changePassword



@app.route('/settings')
def settings():
    form = changePassword()

    if not session.get('logged_in'):

        return redirect(url_for('index'))
    user = User.objects(alias = session.get("alias")).get()

    return render_template('settings.html', apikey = user.apiKey, form = form)

@app.route('/generate_api_key')
def generateapikey():
    if not session.get("logged_in"):
        return redirect(url_for('index'))
    user = User.objects(alias = session.get("alias")).get()
    api_key = urandom(9).encode('base_64').replace("=","").strip()
    user.apiKey = api_key
    user.save()
    return redirect(url_for('settings'))
