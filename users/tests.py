from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserRegistion(APITestCase):
    def Test(self):
        url = reverse("user_view") 
        user_data = {
            "username" : "test",
            "fullname" : "tester",
            "email" :  "cjstmdgusqw@naver.com",
            "password" : "password"
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data["message"], "가입 완료!!")
