from rest_framework.views import APIView
from rest_framework.response import Response

# http status를 나타낸다.
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list ofAPIView freatures"""
        an_apiview = [
            'User HTTP methods as function (get, post, put, delete...)',
            'Is similar to a traditional Django view',
            'Give you the most control over you application logic',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # 들어오는 값을 알맞게 변화시킨다.
        # input 값을 validate 한다.
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' :'PUT'})

    def patch(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' :'PATCH'})
    
    def delete(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' :'DELETE'})

        

