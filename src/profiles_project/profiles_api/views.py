from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status, viewsets

# Create your views here.

class HelloApiView(APIView):

    """  

    Test API View.

    """
    
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        """ Returns a list of APIView features. """

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLS',

        ]


        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):

        """ Create hello message with my name. """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')

            message = 'Hello {0}'.format(name)

            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """ Handles updating an object """

        return Response({'method ': 'put'})


    def patch(self, request, pk=None):
        """ Handles updating an object partially """

        return Response({'method ': 'patch'})


    def delete(self, request, pk=None):
        """ Handles deleting an object """

        return Response({'method ': 'delete'})



class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet. """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message. """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update).',
            'Automatically maps to URLS using Routers.',
            'Provides more functionality with less code.',
        ]

        return Response({'message ': 'Hello!', 'a_viewset ': a_viewset})

    

    def create(self, request):
        """ Create a new hello message """

        serializer = serializers.HelloSerializer(data=request.data) # Passes the data from the request to the serializer

        if serializer.is_valid():
            # if the serializer is valid
            name = serializer.data.get('name') # Gets the name from the serializer data
            message = 'Hello {}'.format(name)
            return Response({ 'message': message })

        else:
            # if the serializer is not valid return STATUS 400 and the ERROR
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # Retrieve uses the primary key to find the object or objects in the database that we are searching for
    def retrieve(self, request, pk=None):
        """ Handles getting an object by its ID """

        return Response({ 'http_method': 'GET' })


    def update(self, request, pk=None):
        """ Handles the updates of an object in the database by primary key index """

        return Response({ 'http_method': 'PUT' })

    
    def partial_update(self, request, pk=None):
        """ Handles the partial updates of an object in the database by primary key index """

        return Response({ 'http_method': 'PATCH' })


    def destroy(self, request, pk=None):
        """ Handles the removal of an object in the database by primary key index """

        return Response({ 'http_method': 'DELETE' })
