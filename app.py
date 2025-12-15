from flask import Flask, jsonify, request, render_template
import database

app = Flask(__name__)

# Initialize database on first run
try:
    database.init_db()
except:
    pass

@app.route('/')
def home():
    """Home page with all blog posts."""
    posts = database.get_all_posts()
    # Add tags to each post
    posts_with_tags = []
    for post in posts:
        post_dict = dict(post)
        post_dict['tags'] = database.get_tags_for_post(post['id'])
        posts_with_tags.append(post_dict)
    return render_template('home.html', posts=posts_with_tags)

@app.route('/api')
def api_home():
    """API endpoint."""
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

@app.route('/posts', methods=['POST'])
def create_post():
    """Create a new post."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    database.create_post(title, content)
    return jsonify({"message": "Post created successfully"}), 201

@app.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    """Get all comments for a post."""
    comments = database.get_comments_by_post(post_id)
    return jsonify([dict(comment) for comment in comments])

@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    """Create a new comment for a post."""
    data = request.get_json()
    author = data.get('author')
    content = data.get('content')
    
    if not author or not content:
        return jsonify({"error": "Author and content are required"}), 400
    
    database.create_comment(post_id, author, content)
    return jsonify({"message": "Comment created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
