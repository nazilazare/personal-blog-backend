# Personal Blog Backend

A simple blog application built with Flask and SQLite. This project lets you create, view, and comment on blog posts, plus organize posts with tags.

## What's Inside

- Flask web framework for the backend
- SQLite database for storing posts, comments, and tags
- HTML templates for the frontend pages
- Tests to make sure everything works

## Getting Started

### 1. Set Up Virtual Environment

First, create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Requirements

Install the packages you need:

```bash
pip install -r requirements.txt
```

### 3. Initialize the Database

Create the database and tables:

```bash
python -c "import database; database.init_db()"
```

### 4. (Optional) Add Sample Data

If you want to start with some example posts and comments, run:

```bash
python add_sample_data.py
```

This will create 5 blog posts with tags and a few comments.

### 5. Run the Application

Start the Flask server:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

You should see your blog homepage!

### 6. Add More Posts

You can add more blog posts anytime:

1. Click on "New Post" in the navigation
2. Fill in the title and content
3. Add some tags separated by commas (like: python, flask, learning)
4. Click "Create Post"

Then you can:
- Click on any post to read it and add comments
- Click on tags to filter posts by that tag
- Click "Edit" on a post to update it

## Running Tests

To run all the tests:

```bash
pytest
```

To see more details about each test:

```bash
pytest -v
```

To run specific test files:

```bash
pytest test_database.py
pytest test_app.py
```

## Project Structure

- `app.py` - Main Flask application with routes
- `database.py` - Database functions for posts, comments, and tags
- `schema.sql` - Database schema
- `templates/` - HTML templates
- `test_database.py` - Tests for database functions
- `test_app.py` - Integration and end-to-end tests

### 5. Add Some Posts

Once the app is running, you can add blog posts:

1. Click on "New Post" in the navigation
2. Fill in the title and content
3. Add some tags separated by commas (like: python, flask, learning)
4. Click "Create Post"

Then you can:
- Click on any post to read it and add comments
- Click on tags to filter posts by that tag
- Click "Edit" on a post to update it

## Features

- Create and edit blog posts
- Add comments to posts
- Tag posts with keywords
- Filter posts by tag
- View all posts on the homepage

## Notes

- The database file `blog.db` is created automatically when you run the app
- Tests use a separate `test_blog.db` file that gets deleted after each test
- All your data is stored locally in the SQLite database