from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simple in-memory post store (not persistent)
posts = []

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts_page():
    if request.method == 'POST':
        title = request.form.get('title', 'Untitled')
        body = request.form.get('body', '')
        post = {
            'id': len(posts) + 1,
            'title': title,
            'body': body,
            'created': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        posts.insert(0, post)
        return redirect(url_for('posts_page'))
    return render_template('posts.html', posts=posts)

@app.route('/posts/<int:post_id>')
def view_post(post_id):
    p = next((x for x in posts if x['id'] == post_id), None)
    if not p:
        return "Post not found", 404
    return render_template('view_post.html', post=p)

if __name__ == '__main__':
    app.run(debug=True)
