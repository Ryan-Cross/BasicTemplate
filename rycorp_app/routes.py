from rycorp_app import app

from flask import render_template,redirect,url_for,request,flash


@app.route('/')
def index():    
    return render_template("home.html")


