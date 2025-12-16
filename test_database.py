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
