from flask import Flask, render_template, url_for
# Import the `render_template` function to render the `index.html` file.

# Set app name
app = Flask(__name__)


# Map root URL at "/" to home() function, which renders the `index.html` page
@app.route('/')
def home():
    return render_template("index.html") 

if __name__ == '__main__':
    app.run(debug=True) # Run the application in "debug" mode to get diagnostics in terminal
