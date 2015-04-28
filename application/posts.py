from applications import app
from collections import User, Posts
from flask import session, render_template, redirect, flash, url_for, request

@app.route('/post')
def Posts():
    
