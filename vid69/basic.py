# Video 69 Template Variables
# Flask uses Jinja templates
# variables are surrounded by double curly braces {{ some_variable }}
# variables are standard python - can be lists, dictionaries, etc.

# import Flask and render_template for rendering templates...
from flask import Flask, render_template

# Create instance of Flask and call it app
app = Flask(__name__)

# Set a route for the app - just root of the website here.
@app.route('/')
# function that defines what shows at this route
def index():
    # templates should be in a folder called templates.

    # some_variable = "Terry"
    my_variable = "Terry"
    # pass a list
    letters = list(my_variable)
    # pass a dictionary
    pup_dictionary = {'pup_name':'Sammy'}
    # passing a positional parameter to the html document. Usually these are the same
    # but they don't have to be. 
    # return render_template('basic.html', my_variable=some_variable)
    return render_template('basic.html', my_variable=my_variable, letters=letters, 
                                            pup_dictionary=pup_dictionary)
# Run the application
if __name__ == '__main__':
    app.run(debug=True)