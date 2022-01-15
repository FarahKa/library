from django.shortcuts import render
from inventory.models import Author, Book
from inventory.serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

# Create your views here.

#health check
@api_view(('GET',))
def health_check(request):
    return Response(status = 200)

@api_view(http_method_names=['GET'])
def percentage_read(request, pk):
    book = Book.objects.filter(id=pk).first()
    if book:
        try:
            percentage = (book.pages_read / book.number_of_pages) * 100
            return Response({"percentage" : percentage}, status = 200)
        except ZeroDivisionError:
            return Response("Le nombre de pages du livre n'est pas valide.", status = 403)
    return Response(status = 404)

#Using a ModelViewSet
#actions: list, create, retrieve, update, partial_update, destroy
# class BookViewSet(viewsets.ModelViewSet):
#     """A viewset for listing and editing books"""
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()

#Simple class based view
class AuthorList(APIView):
    """A class based view for an author crud"""
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status = 200)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
class AuthorDetail(APIView):
    #permission_classes = (IsAuthenticated,) 
    def get(self, request, pk, format = None):
        author = Author.objects.filter(id=pk).first()
        if author:
            serializer = AuthorSerializer(author)
            return Response(serializer.data, status = 200)
        return Response(status = 404)
    def put(self, request, pk, format=None):
        author = Author.objects.filter(id=pk).first()
        if not author:
            return Response(status= 404)
        serializer = AuthorSerializer(author, data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)
        serializer.save()
        return Response(serializer.data, status = 200)

    def delete(self, request, pk, format = None):
        author = Author.objects.filter(id=pk).first()
        if not author:
            return Response(status=400)
        author.delete()
        return Response(status = 204)


#Simple class based view
class BookList(APIView):
    """A class based view for an author crud"""
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status = 200)

    def post(self, request, format=None):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
class BookDetail(APIView):
    #permission_classes = (IsAuthenticated,) 
    def get(self, request, pk, format = None):
        book = Book.objects.filter(id=pk).first()
        if book:
            serializer = BookSerializer(book)
            return Response(serializer.data, status = 200)
        return Response(status = 404)
    def put(self, request, pk, format=None):
        book = Book.objects.filter(id=pk).first()
        if not book:
            return Response(status= 404)
        serializer = BookSerializer(book, data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)
        serializer.save()
        return Response(serializer.data, status = 200)

    def delete(self, request, pk, format = None):
        book = Book.objects.filter(id=pk).first()
        if not book:
            return Response(status=400)
        book.delete()
        return Response(status = 204)


