from drf_spectacular.utils import  OpenApiExample,OpenApiParameter
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from adrf.decorators import api_view
from django.core import serializers
from asgiref.sync import sync_to_async
from datetime import timedelta,datetime,timezone
from .extract_data import ExtractData
from .models import User
from .serializers import IndexSerializer,UserSerializer,LoginSerializer,ReportSerializer
import jwt,asyncio,os
from . import s3_access as s3
from .models import Company
ext = ExtractData()

# Create your views here.
@extend_schema(
    parameters=[OpenApiParameter("bucket_name",type=str,location='query',required=True),        
            OpenApiParameter(
            "jwt",  # Optional cookie parameter
            type=str,
            location="query",
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
        token = request.GET.get("jwt")
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
            location="query",
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
        token = request.GET.get("jwt")
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
        parameters=[
        OpenApiParameter(
            "jwt",  # Optional cookie parameter
            type=str,
            location="query",
            description="cookie for authentication",
            required=True
        )],
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
        token = request.GET.get("jwt")
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
        files_data = [
            {
                'type': file_info_dict.get('Report Type'),  # No quotes around the key name
                'title': file_info_dict.get('Report Title', "0"),
                'created_date': file_info_dict.get('Date Created'),
                'next_asses_date': file_info_dict.get('Next Assessment Date', "NA"),
                'company': file_info_dict.get('Company', "NA"),
                'author': file_info_dict.get('Author', "NA"),
                'summary': file_info_dict.get('Summary'),
                'file_name': file_name,
                'flag': True if "Not Available" in file_info_dict.values() else False
            }
            for file_data in files for file_name, file_info_dict in file_data.items()
        ]
        await sync_to_async(Company.objects.bulk_create)([Company(**data) for data in files_data])
        return Response(data=files, status=status.HTTP_200_OK)

    
@extend_schema(
    parameters=[OpenApiParameter("file_name",type=str,location='query',required=True),
                OpenApiParameter(
            "jwt",  # Optional cookie parameter
            type=str,
            location="query",
            description="cookie for authentication",
            required=True
        )],
    summary="Get the file data",
    examples=[OpenApiExample("get the file data from the database",summary="Json response",value={"file_name":"file-A"},response_only=True)],
    description='get the file data',
    responses={
        status.HTTP_200_OK: {"description": "Successful response", "content": {"application/json": {}}},
        status.HTTP_404_NOT_FOUND: {"description": "Profile does not exist", "content": {"application/json": {}}},
    })
@api_view(['GET'])
def get_file_data(request):
    token = request.GET.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token,key=os.getenv('jwt_secret'),algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")
    one_month_ago = datetime.now() - timedelta(days=30)
    records = Company.objects.filter(date_processed__gte=one_month_ago)
    json_data = serializers.serialize('json', records)
    # resp_data =[val.get("fields") for val in eval(json_data.replace("false","False"))]
    return Response(eval(json_data.replace("false","False")))  

@extend_schema(
    parameters=[
        OpenApiParameter("pk", type=str, location='query', required=True),
        OpenApiParameter("jwt", type=str, location="query", description="Authentication token", required=True),
    ],
    summary="Update company data",
    request=ReportSerializer,
    examples=[
        OpenApiExample(
            "Update file data in the database",
            summary="Update example",
            value={
                "file_name": "file-A", 
                "type" : "New type",
                "author": "New Author", 
                "company": "Updated Company", 
                "title": "New Report Title",
                "created_date": "2024-10-08",
                "next_asses_date": "2025-01-01",
                "summary" : "New summary",
                "flag" : True
            },
            response_only=False
        )
    ],
    description='Update the company file data in the Company model',
    responses={
        status.HTTP_200_OK: {"description": "Successful update", "content": {"application/json": {}}},
        status.HTTP_404_NOT_FOUND: {"description": "File not found", "content": {"application/json": {}}},
    }
)
@api_view(['PATCH']) 
def update_file_data(request):
    token = request.GET.get("jwt")
    if not token:
        raise AuthenticationFailed("Unauthenticated!")

    try:
        payload = jwt.decode(token, key=os.getenv('jwt_secret'), algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")

    pk = request.GET.get("pk")
    if not pk:
        return Response({"error": "pk is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        company_record = Company.objects.get(id=pk)
    except Company.DoesNotExist:
        return Response({"error": "File not found"}, status=status.HTTP_404_NOT_FOUND)

    data = request.data
    fields_to_update = {}
    if 'type' in data:
        fields_to_update['type'] = data['type']
    if 'title' in data:
        fields_to_update['title'] = data['title']
    if 'created_date' in data:
        fields_to_update['created_date'] = data['created_date']
    if 'next_asses_date' in data:
        fields_to_update['next_asses_date'] = data['next_asses_date']
    if 'company' in data:
        fields_to_update['company'] = data['company']
    if 'author' in data:
        fields_to_update['author'] = data['author']
    if 'summary' in data:
        fields_to_update['summary'] = data['summary']
    if 'flag' in data:
        fields_to_update['flag'] = data['flag']

    for field, value in fields_to_update.items():
        setattr(company_record, field, value)
    
    company_record.save()

    return Response({"message": "File updated successfully"}, status=status.HTTP_200_OK)

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
        time_now = datetime.now(timezone.utc)
        payload = {'id':user.id,
                   'exp':time_now+timedelta(minutes=60),
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

