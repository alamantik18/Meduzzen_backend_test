from django.contrib import admin
from django.urls import path
from users.views import CustomUsersAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/usersList/', CustomUsersAPIView.as_view()),
    path('api/v1/usersList/<int:pk>/', CustomUsersAPIView.as_view()),
]
