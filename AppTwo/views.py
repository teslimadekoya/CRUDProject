from django.http import JsonResponse
from . models import Author
from . serializers import AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def author_list (request):

    if request.method == 'GET':
        books = Author.objects.all()
        serializer = AuthorSerializer(books, many= True) 
        return Response(serializer.data)    
    
    if request.method == 'POST':
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def author_detail(request, id):
    
    try:
        books = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
    if request.method == 'GET':
       serializer = AuthorSerializer(books)
       return Response(serializer.data, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(books, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        books.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)