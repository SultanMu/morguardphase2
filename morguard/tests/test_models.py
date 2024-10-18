from django.test import TestCase
from API.models import User, Company
from datetime import datetime


class UserModelTest(TestCase):
    def setUp(self):
        # Create a sample user
        self.user = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            password="supersecretpassword"
        )

    def test_user_creation(self):
        # Test user is created properly
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "johndoe@example.com")

    def test_unique_email(self):
        # Test email uniqueness
        with self.assertRaises(Exception):
            User.objects.create(
                name="Jane Doe",
                email="johndoe@example.com",
                password="anothersecretpassword"
            )


class CompanyModelTest(TestCase):
    def setUp(self):
        # Create a sample company
        self.company = Company.objects.create(
            type="IAQ Audit",
            title="Audit Report",
            created_date="2023-01-01",
            next_asses_date="2024-01-01",
            company="Acme Corp",
            author="John Author",
            summary="This is a summary of the report",
            file_name="report.pdf",
            flag=True
        )

    def test_company_creation(self):
        # Test company is created properly
        self.assertEqual(self.company.type, "IAQ Audit")
        self.assertEqual(self.company.title, "Audit Report")
        self.assertEqual(self.company.company, "Acme Corp")

    def test_default_values(self):
        # Test default values are set correctly
        new_company = Company.objects.create(
            type="Waste Audit",
            flag=False
        )
        self.assertEqual(new_company.title, "0")
        self.assertEqual(new_company.created_date, "NA")
        self.assertEqual(new_company.date_processed, str(datetime.date(datetime.now())))

    def test_flag_value(self):
        # Test the flag field works correctly
        self.assertTrue(self.company.flag)


