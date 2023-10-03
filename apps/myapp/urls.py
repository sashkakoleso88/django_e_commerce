from django.urls import path
from .views import contacts

app_name = "myapp"

urlpatterns = [
    # 127.0.0.1:8000/myapp/contacts/
    path("contacts/", contacts),
]
