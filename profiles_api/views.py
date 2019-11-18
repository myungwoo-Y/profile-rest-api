from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    
    def get(self, request, format=None):
        """Returns a list ofAPIView freatures"""
        an_apiview = [
            'User HTTP methods as function (get, post, put, delete...)',
            'Is similar to a traditional Django view',
            'Give you the most control over you application logic',
        ]

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})

