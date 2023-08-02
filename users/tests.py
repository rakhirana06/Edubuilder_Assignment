from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser1",
            email="testuser1@example.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser1")
        self.assertEqual(user.email, "testuser1@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testadmin",
            email="testadmin@example.com",
            password="testadminpass123",
        )
        self.assertEqual(admin_user.username, "testadmin")
        self.assertEqual(admin_user.email, "testadmin@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

