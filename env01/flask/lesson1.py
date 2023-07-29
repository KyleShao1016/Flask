from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Test Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Pa ge</h1>"

@app.route("/user/<name>") # passing parameter to the website
def test(name):
    return render_template("user.html", user_name = name) # pass url variable to html file

@app.route("/temp")
def temp():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)