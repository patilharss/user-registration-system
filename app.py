
from flask import Flask, render_template,redirect,session
from functools import wraps


#database config
import pymongo
client=pymongo.MongoClient('localhost',27017)

db=client.user_login_system

#decorator
def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            return redirect('/')
    return wrap


# create and configure the app, an instance of Flask
app = Flask(__name__)

app.secret_key=b'N\xa5\xf7@\x1b\xdc\x8a\xfa\xddB\xba\xcdh"#5'

# account routes
from user import routes

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template("dashboard.html")



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000,
            use_reloader=True, threaded=True)