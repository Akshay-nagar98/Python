#What is a QuerySet?Write program to create a new Post object in database:


'''
In Django, a QuerySet is a collection of database queries that can be used to retrieve
data from your database. It acts as an intermediary between the models (database tables)
and the database itself. QuerySets allow you to filter, order, and manipulate data before it
is retrieved from the database.
'''

#Creating a New Post Object in the Database

'''To create a new Post object in the database using Django, you typically follow these steps:

Define the Model: First, you define a Django model that represents your Post object. This is typically done in models.py of your Django app.'''

# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
'''This Post model defines fields like title, content, author, and created_at.'''
#Make Migrations: After defining the model, you need to create database tables and schema migrations for it.

python manage.py makemigrations
python manage.py migrate

#Create a Post Object: Now, you can write Python code (e.g., in a script, Django shell, or view) to create a new Post object and save it to the database.


# Example script to create a new Post object
from myapp.models import Post  # Replace 'myapp' with your app name

def create_post():
    # Create a new Post object
    new_post = Post.objects.create(
        title='First Post',
        content='This is the content of my first post.',
        author='John Doe'
    )
    # Optionally, you can save the object explicitly
    new_post.save()
    
    # Print the newly created post's title
    print(f"Created new post: {new_post.title}")

# Call the function to create a new Post object
create_post()

#Run the Script: You can run the script from the Django project directory using Python:
python my_script.py

