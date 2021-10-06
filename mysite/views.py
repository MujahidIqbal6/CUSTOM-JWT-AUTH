
from .serializers import TokenSerializer,CustomizeErrorClass
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import TokenError,InvalidToken




    


class ListChat(APIView):
    """
    Sample Test Method
    """
    authentication_classes=[CustomizeErrorClass]
  

    def get(self, request, format=None):
        print('got it')
        d={'ds':'ds'}
        return Response(d)






class TokenGenerate(TokenObtainPairView):

    serializer_class = TokenSerializer
     
           


