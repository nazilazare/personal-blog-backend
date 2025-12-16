import pytest
import os
import database

TEST_DB = 'test_blog.db'

@pytest.fixture
def test_db():
    """Create a test database for each test."""
    # Use test database
    database.DATABASE_NAME = TEST_DB
    
    # Initialize test database
    database.init_db()
    
    yield
    
    # Clean up after test
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_create_and_get_post(test_db):
    """Test creating and retrieving a post."""
    # Create a post
    database.create_post("Test Post", "This is test content")
    
    # Get all posts
    posts = database.get_all_posts()
    assert len(posts) == 1
    assert posts[0]['title'] == "Test Post"
    assert posts[0]['content'] == "This is test content"

def test_get_post_by_id(test_db):
    """Test retrieving a post by ID."""
    # Create a post
    database.create_post("Test Post", "Content")
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    # Get post by ID
    post = database.get_post_by_id(post_id)
    assert post is not None
    assert post['title'] == "Test Post"
    assert post['id'] == post_id

def test_update_post(test_db):
    """Test updating a post."""
    # Create a post
    database.create_post("Original Title", "Original Content")
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    # Update the post
    database.update_post(post_id, "Updated Title", "Updated Content")
    
    # Verify update
    post = database.get_post_by_id(post_id)
    assert post['title'] == "Updated Title"
    assert post['content'] == "Updated Content"

def test_create_and_get_comment(test_db):
    """Test creating and retrieving comments."""
    # Create a post first
    database.create_post("Post with Comments", "Content")
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    # Create comments
    database.create_comment(post_id, "Alice", "Great Post!", "This is helpful")
    database.create_comment(post_id, "Bob", "Thanks", "Nice article")
    
    # Get comments
    comments = database.get_comments_by_post(post_id)
    assert len(comments) == 2
    assert comments[0]['author'] == "Alice"
    assert comments[1]['author'] == "Bob"

def test_create_and_get_tags(test_db):
    """Test creating and retrieving tags."""
    # Create a post
    database.create_post("Tagged Post", "Content")
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    # Add tags
    database.add_tag_to_post(post_id, "python")
    database.add_tag_to_post(post_id, "flask")
    
    # Get tags for post
    tags = database.get_tags_for_post(post_id)
    assert len(tags) == 2
    tag_names = [tag['name'] for tag in tags]
    assert "python" in tag_names
    assert "flask" in tag_names

def test_get_posts_by_tag(test_db):
    """Test retrieving posts by tag."""
    # Create posts with tags
    database.create_post("Python Post 1", "Content 1")
    database.create_post("Python Post 2", "Content 2")
    database.create_post("JavaScript Post", "Content 3")
    
    posts = database.get_all_posts()
    database.add_tag_to_post(posts[0]['id'], "python")
    database.add_tag_to_post(posts[1]['id'], "python")
    database.add_tag_to_post(posts[2]['id'], "javascript")
    
    # Get posts by tag
    python_posts = database.get_posts_by_tag("python")
    assert len(python_posts) == 2
    
    js_posts = database.get_posts_by_tag("javascript")
    assert len(js_posts) == 1

def test_remove_post_tags(test_db):
    """Test removing tags from a post."""
    # Create post with tags
    database.create_post("Post", "Content")
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    database.add_tag_to_post(post_id, "tag1")
    database.add_tag_to_post(post_id, "tag2")
    
    # Verify tags exist
    tags = database.get_tags_for_post(post_id)
    assert len(tags) == 2
    
    # Remove tags
    database.remove_post_tags(post_id)
    
    # Verify tags removed
    tags = database.get_tags_for_post(post_id)
    assert len(tags) == 0

def test_post_ordering(test_db):
    """Test that posts are ordered by date (newest first)."""
    # Create multiple posts
    database.create_post("First Post", "Content 1")
    database.create_post("Second Post", "Content 2")
    database.create_post("Third Post", "Content 3")
    
    # Get all posts
    posts = database.get_all_posts()
    
    # Verify order (newest first)
    assert posts[0]['title'] == "Third Post"
    assert posts[1]['title'] == "Second Post"
    assert posts[2]['title'] == "First Post"
