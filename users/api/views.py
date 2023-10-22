# PYTHON
import jwt
import datetime

# REST_FRAMEWORK
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from test.settings import SECRET_KEY

from users.api.serializers import UsersRegisterSerializer, UsersLoginSerializer, UsersModelSerializer

from users.models import Users


class UsersRegisterAPIView(APIView):
    message = {'message': 'User created succesfully'}

    def post(self, request):
        serializer = UsersRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(self.message, status=status.HTTP_201_CREATED)


class UsersLoginAPIView(APIView):

    def post(self, request):
        serializer = UsersLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        payload_content = {
            "email": request.data["email"],
            "exp": datetime.datetime.now() + datetime.timedelta(days=1),
            "iat": datetime.datetime.now()
        }
        token = jwt.encode(payload_content, SECRET_KEY, algorithm="HS256")
        user_email = request.data["email"]
        response = Response()
        response.set_cookie(key="user_token", value=token, httponly=True)
        response.status_code = status.HTTP_202_ACCEPTED
        response.data = {
            "message": f"Hello {user_email}"
        }
        return response


class UsersAPIView(APIView):
    error_message = {"error": "Must be authenticated"}

    def get(self, request):
        token = request.COOKIES.get("user_token")
        if token is not None:
            users = Users.objects.all()
            serializer = UsersModelSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(self.error_message, status=status.HTTP_400_BAD_REQUEST)


class UsersLogoutAPIView(APIView):
    error_message = {"error": "you are not authenticated"}
    succesfully_message = {"message": "see you next time"}
    token_name = "user_token"

    def post(self, request):
        token = request.COOKIES.get(self.token_name)
        if token is not None:
            response = Response()
            response.delete_cookie(self.token_name)
            response.data = self.succesfully_message
            response.status_code = status.HTTP_200_OK
            return response
        return Response(self.error_message, status=status.HTTP_400_BAD_REQUEST)
