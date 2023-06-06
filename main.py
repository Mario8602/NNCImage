# import django

# print(django.VERSION)
from dotenv import load_dotenv
import os

load_dotenv()

DJANGO_ALLOWED_HOSTS=os.getenv("ALLOWED_HOSTS").split(" ")

print(DJANGO_ALLOWED_HOSTS)