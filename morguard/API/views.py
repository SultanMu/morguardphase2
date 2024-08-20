from drf_spectacular.utils import  OpenApiExample,OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from adrf.decorators import api_view
from .extract_data import ExtractData
from .models import User
from .serializers import IndexSerializer,UserSerializer,LoginSerializer
import jwt,datetime,asyncio,os
from . import s3_access as s3
ext = ExtractData()

# Create your views here.
@extend_schema(
    parameters=[OpenApiParameter("bucket_name",type=str,location='query',required=True),        
            OpenApiParameter(
            "jwt",  # Optional cookie parameter
            type=str,
            location="cookie",
            description="cookie for authentication",
            required=True
        )],
                # OpenApiParameter("email",type=str,location='query',required=True)],
    summary="List drives inside the site",
    examples=[OpenApiExample("List of drives with name and id",summary="Json response",value={"Documents":"id"},response_only=True)],
    description='List the drives inside a sharepoint site',
    responses={
        status.HTTP_200_OK: {"description": "Successful response", "content": {"application/json": {}}},
        status.HTTP_404_NOT_FOUND: {"description": "Profile does not exist", "content": {"application/json": {}}},
    })
@api_view(['GET']) 
def list_s3_folders(request):
    if request.method == "GET":
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload = jwt.decode(token,key=os.getenv('jwt_secret'),algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            bucket_name=request.GET.get("bucket_name")
            # email=request.GET.get("email").lower()
            folders = s3.list_folders_in_bucket(bucket_name)
            return Response(data={"S3 folders" : list(folders)},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"exception":str(e)},status.HTTP_404_NOT_FOUND)

@extend_schema(
    parameters=[OpenApiParameter("folder_name",type=str,location='query',required=True),
                OpenApiParameter("bucket_name",type=str,location='query',required=True),
                OpenApiParameter(
            "jwt",  # Optional cookie parameter
            type=str,
            location="cookie",
            description="cookie for authentication",
            required=True
        )],
    summary="expand folder inside S3",
    examples=[OpenApiExample("expand folder with folder name",summary="Json response",value={"file_name":"file-A"},response_only=True)],
    description='List the drives inside a sharepoint site',
    responses={
        status.HTTP_200_OK: {"description": "Successful response", "content": {"application/json": {}}},
        status.HTTP_404_NOT_FOUND: {"description": "Profile does not exist", "content": {"application/json": {}}},
    })
@api_view(['GET']) 
def expand_s3_folder(request):
    if request.method == "GET":
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload = jwt.decode(token,key=os.getenv('jwt_secret'),algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            folder_name=request.GET.get("folder_name")
            bucket_name=request.GET.get("bucket_name")
            files = s3.expand_s3_folder(bucket_name,folder_name)
            return Response(data={"files":files},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"exception":str(e)},status.HTTP_404_NOT_FOUND)

@extend_schema(
    request=IndexSerializer,
    examples=[
                    OpenApiExample(
                        'Selective index',
                        summary='Processes selected files for text extraction and indexing',
                        description='selected files are to be passed as keys and values',
                        value={"files":["file.pdf"],
                               "bucket_name":"bucket_A",
                               "folder_name":"folder_A"},
                    request_only=True)

                ],
    description='Request body to be sent in as a POST request with all as required key-value pairs',
    responses={
        status.HTTP_200_OK: {"description": "Successful response", "content": {"application/json": {}}},
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request", "content": {"application/json": {}}},
    })
@api_view(['POST'])
async def index_files(request):
    if request.method == "POST":
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload = jwt.decode(token,key=os.getenv('jwt_secret'),algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        request_body = request.data
        files = request_body.get("files")
        bucket_name = request_body.get("bucket_name")
        folder_name = request_body.get("folder_name")
        indexes = [ext.index_file(s3.get_s3_file_url(bucket_name,folder_name,file_name), file_name,folder_name) for file_name in files]
        files = await asyncio.gather(*indexes)
        return Response(data=files,status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    serializer_class = UserSerializer
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={200: UserSerializer}
    )
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    serializer_class = LoginSerializer
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: LoginSerializer}
    )
    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found!")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        time_now = datetime.datetime.now(datetime.timezone.utc)
        payload = {'id':user.id,
                   'exp':time_now+datetime.timedelta(minutes=60),
                    'iat':time_now
                   }
        token = jwt.encode(payload,key=os.getenv('jwt_secret'),algorithm='HS256')
        response = Response()
        response.set_cookie(key="jwt",value=token,httponly=True)
        response.data = {
            "jwt":token
        }
        return response
    
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message":"success"
        }
        return response

