import pytest
import os
from app import app
import database

TEST_DB = 'test_blog.db'

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    # Use test database
    database.DATABASE_NAME = TEST_DB
    
    # Configure app for testing
    app.config['TESTING'] = True
    
    # Initialize test database
    database.init_db()
    
    with app.test_client() as client:
        yield client
    
    # Clean up after test
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


# ============================================================================
# INTEGRATION TESTS
# These tests use the Flask test client AND database functions for setup
# They verify that routes work correctly with the database layer
# ============================================================================

def test_integration_home_page(client):
    """Test that the home page loads."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Personal Blog' in response.data

def test_integration_create_post_page_get(client):
    """Test loading the create post page."""
    response = client.get('/create')
    assert response.status_code == 200
    assert b'Create New Post' in response.data

def test_integration_create_post_via_form(client):
    """Test creating a post through the form submission."""
    response = client.post('/create', data={
        'title': 'Test Post Title',
        'content': 'This is test content for the post.',
        'tags': 'python, testing'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Test Post Title' in response.data
    
    # Verify post was created in database
    posts = database.get_all_posts()
    assert len(posts) == 1
    assert posts[0]['title'] == 'Test Post Title'
    assert posts[0]['content'] == 'This is test content for the post.'

def test_integration_view_post_detail(client):
    """Test viewing a specific post detail page."""
    # Create a post first (using database function for setup)
    database.create_post('Sample Post', 'This is sample content.')
    
    # Get the post ID
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    # View the post
    response = client.get(f'/post/{post_id}')
    assert response.status_code == 200
    assert b'Sample Post' in response.data
    assert b'This is sample content.' in response.data
    assert b'Add a Comment' in response.data

def test_integration_add_comment(client):
    """Test adding a comment to a post."""
    # Create a post first (using database function for setup)
    database.create_post('Post with Comment', 'Content for commenting.')
    posts = database.get_all_posts()
    post_id = posts[0]['id']
    
    # Add a comment
    response = client.post(f'/post/{post_id}/comment', data={
        'author': 'Test Author',
        'title': 'Test Comment Title',
        'content': 'This is a test comment.'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Test Comment Title' in response.data
    assert b'Test Author' in response.data
    assert b'This is a test comment.' in response.data
    
    # Verify comment was created in database
    comments = database.get_comments_by_post(post_id)
    assert len(comments) == 1
    assert comments[0]['author'] == 'Test Author'
    assert comments[0]['title'] == 'Test Comment Title'
