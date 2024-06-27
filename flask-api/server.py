from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def index():
    """yes, I know about Docstrings"""
    return "hello world"

@app.route("/no_content")
def no_content():
    """again, I know about Docstrings"""
    return ({"message":"No content found"}, 204)
# Note that even though you returned a JSON message,it is not sent back to the client as 204.
# By default, nothing is returned.
@app.route("/exp")
def index_explicit():
    """Docstrings are boring"""
    resp = make_response({"message":"My first explicit response!"})
    resp.status_code = 200
    return resp
