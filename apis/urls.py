from django.urls import path
from .views import get_user, create_user, update_user, delete_user, test_celery

urlpatterns = [
    # Endpoint for retrieving user data
    path('api/user/', get_user, name='get_user'),

    # Endpoint for creating a new user
    path('api/user/create', create_user, name='create_user'),

    # Endpoint for updating user data
    path('api/user/<int:user_id>/update/', update_user, name='update_user'),

    # Endpoint for deleting a user
    path('api/user/<int:user_id>/delete/', delete_user, name='delete_user'),

    path('api/user/celery', test_celery, name='test_celery'),
]