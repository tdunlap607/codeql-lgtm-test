from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/safe')
def safe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + escape(first_name))
    

@app.route('/unsafe_one')
def unsafe_one():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + first_name)
    

@app.route('/unsafe_two')
def unsafe_two():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + first_name)
