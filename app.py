from flask import Flask, jsonify
import database

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint."""
    return jsonify({"message": "Personal Blog API"})

@app.route('/posts', methods=['GET'])
def get_posts():
    """Get all posts."""
    posts = database.get_all_posts()
    return jsonify([dict(post) for post in posts])

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    """Get a single post by ID."""
    post = database.get_post_by_id(post_id)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(dict(post))

if __name__ == '__main__':
    app.run(debug=True)
