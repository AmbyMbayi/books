from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'Amby',
            email= 'ambymbayi54@gmail.com',
            password= 'maynov54'
        )

        self.assertEqual(user.username,'Amby')
        self.assertEqual(user.email, 'ambymbayi54@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username = 'Amby',
            email='ambymbayi54@gmail.com',
            password = 'maynov54'
        )

        self.assertEqual(admin_user.username, 'Amby')
        self.assertEqual(admin_user.email, 'ambymbayi54@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
