from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name="index"),
    path('profile/<str:pk>', views.contactProfile, name="profile"),
    # path('edit/', views.edit, name="edit"),
    # path('edit/<int:users_id>/', edit, name='edit'),
    # path('delete/<user_id>', views.delete, name="delete"),  # Add new delete (problem)
    # path('edit/<user_id>', views.edit, name="users"),  # Add new edit (problem)
)
