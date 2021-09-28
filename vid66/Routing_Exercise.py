# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return("<h1>Welcome to Puppy Latin Website</h1>")

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1] != "y":
        new_name = name+'y'
    else:
        new_name = name[0:-1] + 'iful'
    return(f"Puppy Latin Name is {new_name}")
if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
