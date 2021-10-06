
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework import exceptions
from rest_framework_simplejwt.exceptions import TokenError,InvalidToken

class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)    
    
        result={'refresh':data['refresh'],'access':data['access']}
        data.clear()
        data['data'] = result
        data['status']=True

        return data
   
class CustomDetailDictMixin:
       '''
       Customized class for class 'DetailDictMixin' 
       '''

       def __init__(self, detail=None, code=None):
        '''
        Customize __init__ method
        '''


        detail_dict = {}
        if isinstance(detail, dict):
            detail_dict.update(detail)
        
        #setting custome values
        detail_dict['message']='Unauthorized user'
        detail_dict['status']='False'

        super().__init__(detail_dict)

class CustomInvalidToken(CustomDetailDictMixin,exceptions.AuthenticationFailed):   
    '''
    Customized class for class 'InvalidToken' 
    '''
    pass


class CustomizeErrorClass(JWTAuthentication):
     def get_validated_token(self, raw_token):
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                return AuthToken(raw_token)
            except TokenError as e:
                pass
        raise CustomInvalidToken()
        