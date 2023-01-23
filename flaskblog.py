from flask import Flask, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c86b967fa81f99441d3ed4d28ed9535c19fabf18'

posts = [
    {
        "author": "Nezar Ghanem",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Leen Ghanem",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018"
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
