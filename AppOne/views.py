from django.http import JsonResponse
from . models import Books
from . serializers import BooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def books_list (request):

    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many= True) 
        return Response(serializer.data)    
    
    if request.method == 'POST':
        serializer = BooksSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def books_detail(request, id):
    
    try:
        books = Books.objects.get(pk=id)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
       serializer = BooksSerializer(books)
       return Response(serializer.data, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = BooksSerializer(books, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        books.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)