
from flask import Flask, jsonify,request,session,redirect
from passlib.hash import pbkdf2_sha256
import uuid
from app import db


class User:


    def start_session(self,user):
        del user['password']
        session['logged_in']=True
        session['user']=user

        return jsonify(user),200


    def signup(self):
        print (request.form)

        #User obj
        user = {
        "_id": uuid.uuid4().hex, 
        "name":request.form.get('name'), 
        "email": request.form.get('email'), 
        "password": request.form.get('password')
        }

        # password encryption

        user['password']= pbkdf2_sha256.encrypt(user['password'])


        #checking if mail is already exists
        if db.users.find_one({"email":user['email']}):
            return jsonify({"error":"Email already in use"}),400

        #database:
        if db.users.insert_one(user):
            #if sucessful
            return self.start_session(user)
        else:
            return jsonify({"error":"Something went wrong"}),400
       
    def signout(self):
        session.clear()
        return redirect('/')



    def login(self):
        user=db.users.find_one({

            "email":request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'),user['password']):
            return self.start_session(user)
        
        return jsonify({'error':"Invalid credentials"}),401