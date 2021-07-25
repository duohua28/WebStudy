from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():

    a=10
    b=6
    c=0
    # result=(a+b)/c
    return '<h1>Happy</h1>'

app.run(debug=True)
