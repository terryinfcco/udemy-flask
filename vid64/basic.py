# Video 64 Dynamic Routing
# examples are having a different page for every user of a system
# done by passing a variable to 

# import Flask
from flask import Flask

# Create instance of Flask and call it app
app = Flask(__name__)

# Set a route for the app - just root of the website here.
@app.route('/')
# function that defines what shows at this route
def index():
    return '<h1>Hello Puppy! </h1>'

#  create a second webpage at /information
@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

# So sub page puppy followed by a variable name
@app.route('/puppy/<name>')
def puppy(name):
    # Then can use the variable in an html statement and you can use some python methods - here .upper
    return f"<h1>This is the page for {name.upper()}</h1>"
    
# Run the application
if __name__ == '__main__':
    app.run()