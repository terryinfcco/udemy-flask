# Video 72 url_for() function
# You can link between pages using the function name of the page you want to link to.

# import Flask and render_template for rendering templates...
from flask import Flask, render_template

# Create instance of Flask and call it app
app = Flask(__name__)

# Set a route for the app - just root of the website here.
@app.route('/')
# function that defines what shows at this route
def index():
    # templates should be in a folder called templates.
    return render_template('home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html', name=name)
    
# Run the application
if __name__ == '__main__':
    app.run(debug=True)