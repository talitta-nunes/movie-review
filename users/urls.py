from django.urls import path

from .views import LoginView, UserDetailView, UserListView

urlpatterns = [
    path("users/register/", UserListView.as_view()),
    path("users/login/", LoginView.as_view()),  # rota que devolve o token
    path("users/", UserListView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
]
