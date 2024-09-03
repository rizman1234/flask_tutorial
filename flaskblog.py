from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"


if __name__ == '__main__':
    app.run(debug=True)





#export FLASK_DEBUG=1
#export FLASK_APP=flaskblog.py
