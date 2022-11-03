from rest_framework.exceptions import APIException
from rest_framework.views import status



class AlreadyExist(APIException): 
    status_code = status.HTTP_400_BAD_REQUEST


    def get_full_details(self):
        return self