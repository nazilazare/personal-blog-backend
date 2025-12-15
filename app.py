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

if __name__ == '__main__':
    app.run(debug=True)
