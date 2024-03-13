from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

'''
In the preceding code block, you first import the Flask object from the flask package. 
You then use it to create your Flask application instance with the name app. 
You pass the special variable __name__ that holds the name of the current Python module. 
It’s used to tell the instance where it’s located -— you need this because Flask sets up some paths behind the scenes.
'''
