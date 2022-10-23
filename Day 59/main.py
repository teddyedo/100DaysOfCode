from flask import Flask, render_template
import requests

from post import Post

app = Flask(__name__)


def get_posts():
    response = requests.get("https://api.npoint.io/4af156202f984d3464c3")
    posts = [Post(post["title"], post["subtitle"], post["body"]) for post in
             response.json()]
    return posts


@app.route('/')
def home():
    return render_template("index.html", posts=get_posts())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/posts/<int:id>")
def get_post(id):
    posts = get_posts()
    return render_template("post.html", post=posts[id])


if __name__ == "__main__":
    app.run(debug=True)
