import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'component_site.settings')
import sys
sys.path.insert(0, 'c:\\Users\\Amritanshu\\OneDrive\\Desktop\\Level3_Integrated_Django_Frontend_Backend\\component_site')
django.setup()

from django.contrib.auth.models import User
from core.models import Post

# Get the first user (assuming one exists)
user = User.objects.first()

if user:
    # Create sample posts
    Post.objects.create(
        title='Welcome to Our Blog',
        content='This is the first post in our new blog application. Welcome everyone! We are excited to share our thoughts, ideas, and experiences with you.',
        author=user
    )
    
    Post.objects.create(
        title='Getting Started with Django',
        content='Django is a powerful web framework for Python. In this post, we explore the basics of Django and how it can help you build amazing web applications quickly and efficiently.',
        author=user
    )
    
    Post.objects.create(
        title='Best Practices for Web Development',
        content='When developing web applications, it is important to follow best practices. This includes writing clean code, using proper security measures, testing your code, and maintaining good documentation.',
        author=user
    )
    
    Post.objects.create(
        title='Understanding REST APIs',
        content='REST APIs are a fundamental part of modern web development. Learn how to design, build, and consume REST APIs effectively.',
        author=user
    )
    
    Post.objects.create(
        title='Frontend and Backend Integration',
        content='Integrating frontend and backend is crucial for modern web applications. This post covers best practices for seamless integration.',
        author=user
    )
    
    print('✓ 5 sample posts created successfully!')
else:
    print('No user found. Please create a user first.')
