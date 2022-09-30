from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", blog=blog_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)
