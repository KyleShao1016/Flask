from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Test Page</h1>"


@app.route("/jinja")
def test_jinja():
    first_name = "John"
    stuff = "this is <strong>bold</strong> text"
    fav_sports = ["basketball", "baseball", "badminton", 41]
    data = [-10, -45, 3, -2, 6, 7, 10, -20]
    data.sort(reverse=1)
    return render_template(
        "jinja.html",
        first_name=first_name,
        stuff=stuff,
        fav_sports=fav_sports,
        data=data)

@app.route("/user/<name>") # passing parameter to the website
def test(name):
    return render_template("user.html", user_name = name) # pass url variable to html file

@app.route("/temp")
def temp():
    return render_template("index.html")

# Create Custom Error Pages(for error handling)
## Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

## Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)