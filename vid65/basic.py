# Video 65 Debug Mode

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
    # Then can use the variable in an html statement and create an error by trying to access a char past the end of string
    return f"<h1>This is the page for {name[100]}</h1>"
    
# Run the application this time using debug=true in app.run()
# You'll get a debug PIN when you run this and you can select the console on the error page
# and it will ask you for the pin
if __name__ == '__main__':
    app.run(debug=True)