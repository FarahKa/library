from rest_framework import serializers
from django.contrib.auth.models import User, Group
from models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class meta:
        model = Author

class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = Book

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class mera:
        model = Group
        fields = ['id', 'name']