from flask import Flask, render_template

# import the instance of app from app.py
# from file/module import instance
from app import app

# from folder.file import class
from user.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login',methods=['POST'])
def login():
    return User().login()