from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
import jwt
from unittest.mock import patch
from API.models import Company, User
from datetime import datetime
import os


class ListS3FoldersTestCase(APITestCase):
    def setUp(self):
        # Setup initial data if needed
        self.url = reverse('list-drive')
        self.valid_token = jwt.encode({'id': 1}, key=os.getenv('jwt_secret'), algorithm='HS256')
        self.invalid_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MX0.invalid_signature'

    @patch('API.s3_access.list_folders_in_bucket')
    def test_list_s3_folders_success(self, mock_list_folders_in_bucket):
        mock_list_folders_in_bucket.return_value = ['folder1', 'folder2']

        response = self.client.get(self.url, {'jwt': self.valid_token, 'bucket_name': 'test_bucket'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('S3 folders', response.data)

    def test_list_s3_folders_missing_token(self):
        response = self.client.get(self.url, {'bucket_name': 'test_bucket'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Unauthenticated!')

    # def test_list_s3_folders_invalid_token(self):
    #     response = self.client.get(self.url, {'jwt': self.invalid_token, 'bucket_name': 'test_bucket'})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertEqual(response.data['detail'], 'Unauthenticated!')


class ExpandS3FolderTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('expand-drive')
        self.valid_token = jwt.encode({'id': 1}, key=os.getenv('jwt_secret'), algorithm='HS256')

    @patch('API.s3_access.expand_s3_folder')
    def test_expand_s3_folder_success(self, mock_expand_s3_folder):
        mock_expand_s3_folder.return_value = ['file1', 'file2']

        response = self.client.get(self.url, {
            'jwt': self.valid_token, 'folder_name': 'test_folder', 'bucket_name': 'test_bucket'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('files', response.data)

    # def test_expand_s3_folder_missing_parameters(self):
    #     # Case 1: Missing 'folder_name'
    #     response = self.client.get(self.url, {'jwt': self.valid_token, 'bucket_name': 'test_bucket'})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #     # Case 2: Missing 'bucket_name'
    #     response = self.client.get(self.url, {'jwt': self.valid_token, 'folder_name': 'test_folder'})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #     # Case 3: Missing both 'folder_name' and 'bucket_name'
    #     response = self.client.get(self.url, {'jwt': self.valid_token})
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #     # Case 4: Missing 'jwt'
    #     response = self.client.get(self.url, {'folder_name': 'test_folder', 'bucket_name': 'test_bucket'})
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class IndexFilesTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('index-files')
        self.valid_token = jwt.encode({'id': 1}, key=os.getenv('jwt_secret'), algorithm='HS256')

    # @patch('API.views.ext.index_file')
    # @patch('API.s3_access.get_s3_file_url')
    # def test_index_files_success(self, mock_get_s3_file_url, mock_index_file):
    #     # Mock the S3 URL and index_file return values
    #     mock_get_s3_file_url.return_value = 'https://s3.amazonaws.com/test/file1.pdf'
    #     mock_index_file.return_value = {
    #         'Report Type': 'Water Audit',
    #         'Report Title': 'Test Report',
    #         'Date Created': '2023-10-18',
    #         'Next Assessment Date': '2024-10-18',
    #         'Company': 'Company X',
    #         'Author': 'Author Y',
    #         'Summary': 'Test summary'
    #     }

    #     # Prepare the request data
    #     data = {
    #         "files": ["file1.pdf"],
    #         "bucket_name": "test_bucket",
    #         "folder_name": "test_folder"
    #     }

    #     # Pass the JWT token in the GET parameters instead of the Authorization header
    #     response = self.client.post(self.url + f"?jwt={self.valid_token}", data)
        
    #     # Validate the response
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('file1.pdf', response.data)  # Check for the file name in the response
    #     file_info = response.data['file1.pdf'][0]  # Assuming the structure of the response
    #     self.assertEqual(file_info['Report Title'], 'Test Report')  # Ensure title is returned correctly
    #     self.assertEqual(file_info['Report Type'], 'Water Audit')  # Ensure report type is correct


class GetFileDataTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('get-files')
        self.valid_token = jwt.encode({'id': 1}, key=os.getenv('jwt_secret'), algorithm='HS256')

    def test_get_file_data_success(self):
        Company.objects.create(type="Waste Audit", title="Report A", flag="False", date_processed=datetime.now())
        response = self.client.get(self.url, {'jwt': self.valid_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_get_file_data_no_token(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'Unauthenticated!')


class UpdateFileDataTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('update-files')
        self.valid_token = jwt.encode({'id': 1}, key=os.getenv('jwt_secret'), algorithm='HS256')
        self.company = Company.objects.create(type="Waste Audit", title="Old Report", flag="True", date_processed=datetime.now())

    # def test_update_file_data_success(self):
    #     update_data = {
    #         "type": "Water Audit",
    #         "title": "New Report",
    #         "pk": self.company.id  # Include pk here if it's part of the update payload
    #     }

    #     response = self.client.patch(
    #         self.url, update_data, HTTP_AUTHORIZATION=f'Bearer {self.valid_token}', format='json'
    #     )
    
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Company.objects.get(id=self.company.id).title, "New Report")

