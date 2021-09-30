# Video 70 Control Flow
# Flask uses Jinja templates
# Control Flow statements are surrounded by curly brace, percent {% loop %}


# import Flask and render_template for rendering templates...
from flask import Flask, render_template

# Create instance of Flask and call it app
app = Flask(__name__)

# Set a route for the app - just root of the website here.
@app.route('/')
# function that defines what shows at this route
def index():
    # templates should be in a folder called templates.

    # pass a list
    name = "Terry"
    letters = list(name)
    puppies = ['Fluffy','Rufus','Spike']
    # passing a positional parameter to the html document. Usually these are the same
    # but they don't have to be. 
    return render_template('basic.html', letters=letters, puppies=puppies)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)