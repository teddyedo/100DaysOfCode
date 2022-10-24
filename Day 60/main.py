from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()

app = Flask(__name__)

MY_EMAIL = "*********************"
MY_PASSWORD = "*********************"


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg="Contact me")
    else:
        send_email("*********************", request)
        return render_template("contact.html", msg="Successfully send message!")


def send_email(receiver, request):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, receiver,
                            msg=str("Subject:Someone want to talk with you!\n\n" + f"Name: {request.form['name']}\nEmail: {request.form['email']}\nPhone: {request.form['phone']}\nMessage: {request.form['message']}\n").encode('utf-8'))


if __name__ == "__main__":
    app.run(debug=True)
