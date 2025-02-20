from flask import Flask, render_template
# Import the `render_template` function to render the `index.html` file.

app = Flask(__name__)


# Route to the root of the application
@app.route('/')
def home():
    return render_template("index.html") 

if __name__ == '__main__':
    app.run(debug=True)
