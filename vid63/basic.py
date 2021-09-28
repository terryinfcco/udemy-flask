# Video 63 Basic Routes
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
    
# Run the application
if __name__ == '__main__':
    app.run()