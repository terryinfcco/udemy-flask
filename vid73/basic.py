# Video 73 HTML Forms

# import Flask and render_template for rendering templates...
from flask import Flask, render_template, request

# Create instance of Flask and call it app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thankyou.html', first=first, last=last)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)