from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile

class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Gives you most control over your application logic'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )


    def put(self, request, pk=None):
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides mode functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        return Response({'method':'GET'})
    
    
    def update(self, request, pk=None):
        return Response({'method':'PUT'})


    def partial_update(self, request, pk=None):
        return Response({'method':'PATCH'})


    def destroy(self, request, pk=None):
        return Response({'method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    