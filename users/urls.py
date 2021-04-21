from django.urls import path
from . import views
# Create your models here.
app_name = 'users'
urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('signup_user/', views.signup_user, name="signup_user"),
    path('logout/', views.logout_user, name="logout_user"),
    path('update/', views.update_info, name="update_info"),
    path('delete/', views.delete_user, name="delete_user"),
    path('test/', views.test, name="test"),
]
