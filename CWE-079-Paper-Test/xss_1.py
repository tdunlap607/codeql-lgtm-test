from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/safe')
def safe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + escape(first_name))
    
def new_function():
    # the purpose of new function is to add new tex
    print("A new function to shift unsafe() down")
    print("More code...")
    print("More code...")
    print("More code...")
    print("More code...")       
 
@app.route('/unsafe')
def unsafe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + first_name)
