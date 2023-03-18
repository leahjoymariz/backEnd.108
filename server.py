from flask import Flask
import json
from about import me
from data import mock_data


app = Flask(__name__) # create a instance of Flask class


@app.get("/")
def home():
    return "Hello World from a flask server"


@app.get("/test")
def test():
    return "This is a test page"




@app.get("/api/version")
def version():
    return json.dumps("1.0")


@app.get("/api/about")
def about():
    return json.dumps(me)


# get /api/developer/name
# return the full name of the developer plus the email
# eg. Leah Joy Mariz Duco -- leahjoymariz@gmail.com
@app.get("/api/developer/name")
def dev_name():
    name = me["name"]
    last = me["last_name"]
    email = me["email"]
    response = f"{name} {last} -- {email}"
    return json.dumps(response)



def get_catalog():
    return json.dumps(mock_data)


# get /api/products/count
@app.get("/api/products/count")
def product_count():
    count = len(mock_data)
    return json.dumps(count)


# start the server
app.run(debug=True)