"""
Script to add sample blog posts and tags to the database.
Run this after initializing the database to populate it with example content.
"""
import database

print("Adding sample blog posts...")

# Create sample posts
post1_id = database.create_post(
    "Welcome to My Blog",
    "This is my first blog post! I'm excited to share my journey learning web development with Flask and Python. Stay tuned for more posts about coding, tutorials, and my projects."
)

post2_id = database.create_post(
    "Getting Started with Python",
    "Python is an amazing programming language for beginners. It has simple syntax and is very powerful. In this post, I'll share some tips for getting started with Python and resources that helped me learn."
)

post3_id = database.create_post(
    "Building Web Apps with Flask",
    "Flask is a lightweight web framework for Python. It's perfect for building small to medium-sized web applications. Today I learned how to set up routes, templates, and connect to a database. It's easier than I thought!"
)

post4_id = database.create_post(
    "Understanding Databases",
    "Databases are essential for storing data in web applications. I've been learning about SQLite, which is great for small projects. It's file-based and doesn't require a separate server. Pretty convenient for development!"
)

post5_id = database.create_post(
    "Testing Your Code",
    "Writing tests is important to make sure your code works correctly. I learned about pytest and how to write unit tests, integration tests, and end-to-end tests. It takes time but it's worth it to catch bugs early."
)

print("Posts created successfully!")

# Get all posts to add tags
posts = database.get_all_posts()

# Add tags to posts
print("Adding tags to posts...")

# Post 1 tags
database.add_tag_to_post(posts[4]['id'], "introduction")
database.add_tag_to_post(posts[4]['id'], "personal")

# Post 2 tags
database.add_tag_to_post(posts[3]['id'], "python")
database.add_tag_to_post(posts[3]['id'], "tutorial")
database.add_tag_to_post(posts[3]['id'], "beginner")

# Post 3 tags
database.add_tag_to_post(posts[2]['id'], "flask")
database.add_tag_to_post(posts[2]['id'], "python")
database.add_tag_to_post(posts[2]['id'], "web-development")

# Post 4 tags
database.add_tag_to_post(posts[1]['id'], "database")
database.add_tag_to_post(posts[1]['id'], "sqlite")
database.add_tag_to_post(posts[1]['id'], "tutorial")

# Post 5 tags
database.add_tag_to_post(posts[0]['id'], "testing")
database.add_tag_to_post(posts[0]['id'], "pytest")
database.add_tag_to_post(posts[0]['id'], "python")

print("Tags added successfully!")

# Add some sample comments
print("Adding sample comments...")

database.create_comment(posts[4]['id'], "John", "Great start!", "Welcome to the blogging world! Looking forward to more posts.")
database.create_comment(posts[3]['id'], "Sarah", "Very helpful", "Thanks for sharing these Python tips. Really helpful for beginners like me!")
database.create_comment(posts[2]['id'], "Mike", "Flask is awesome", "I agree, Flask makes web development so much easier. Great post!")

print("Comments added successfully!")
print("\nSample data has been added to the database!")
print("You can now run the app with: python app.py")
