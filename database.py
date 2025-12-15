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
def create_comment(post_id, author, title, content):
    """Create a new comment for a post."""
    conn = get_db_connection()
    conn.execute('INSERT INTO comments (post_id, author, title, content) VALUES (?, ?, ?, ?)', 
                 (post_id, author, title, content))
    conn.commit()
    conn.close()

def get_comments_by_post(post_id):
    """Get all comments for a specific post."""
    conn = get_db_connection()
    comments = conn.execute('SELECT * FROM comments WHERE post_id = ? ORDER BY created_at ASC', 
                           (post_id,)).fetchall()
    conn.close()
    return comments

# Tags functions
def create_tag(name):
    """Create a new tag."""
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO tags (name) VALUES (?)', (name,))
        conn.commit()
    except:
        pass  # Tag already exists
    conn.close()

def get_or_create_tag(name):
    """Get a tag by name or create it if it doesn't exist."""
    conn = get_db_connection()
    tag = conn.execute('SELECT * FROM tags WHERE name = ?', (name,)).fetchone()
    if tag is None:
        conn.execute('INSERT INTO tags (name) VALUES (?)', (name,))
        conn.commit()
        tag = conn.execute('SELECT * FROM tags WHERE name = ?', (name,)).fetchone()
    conn.close()
    return tag

def add_tag_to_post(post_id, tag_name):
    """Add a tag to a post."""
    tag = get_or_create_tag(tag_name)
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO post_tags (post_id, tag_id) VALUES (?, ?)', 
                     (post_id, tag['id']))
        conn.commit()
    except:
        pass  # Tag already associated with post
    conn.close()

def get_tags_for_post(post_id):
    """Get all tags for a specific post."""
    conn = get_db_connection()
    tags = conn.execute('''
        SELECT t.* FROM tags t
        JOIN post_tags pt ON t.id = pt.tag_id
        WHERE pt.post_id = ?
    ''', (post_id,)).fetchall()
    conn.close()
    return tags

def get_posts_by_tag(tag_name):
    """Get all posts for a specific tag."""
    conn = get_db_connection()
    posts = conn.execute('''
        SELECT p.* FROM posts p
        JOIN post_tags pt ON p.id = pt.post_id
        JOIN tags t ON pt.tag_id = t.id
        WHERE t.name = ?
        ORDER BY p.created_at DESC
    ''', (tag_name,)).fetchall()
    conn.close()
    return posts

def get_all_tags():
    """Get all tags."""
    conn = get_db_connection()
    tags = conn.execute('SELECT * FROM tags ORDER BY name').fetchall()
    conn.close()
    return tags
