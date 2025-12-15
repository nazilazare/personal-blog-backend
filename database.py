import sqlite3

DATABASE_NAME = 'blog.db'

def get_db_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with the schema."""
    conn = get_db_connection()
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

# Posts functions
def create_post(title, content):
    """Create a new blog post."""
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()

def get_all_posts():
    """Get all blog posts."""
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
    conn.close()
    return posts

def get_post_by_id(post_id):
    """Get a single post by ID."""
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post

# Comments functions
def create_comment(post_id, author, content):
    """Create a new comment for a post."""
    conn = get_db_connection()
    conn.execute('INSERT INTO comments (post_id, author, content) VALUES (?, ?, ?)', 
                 (post_id, author, content))
    conn.commit()
    conn.close()

def get_comments_by_post(post_id):
    """Get all comments for a specific post."""
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY created_at ASC', 
                           (post_id,)).fetchall()
    conn.close()
    return comments
