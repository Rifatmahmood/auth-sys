from django.urls import path
from .views import signup, profile, user_login, user_logout, password_change, password_change_simple
urlpatterns = [

    path('signup/', signup, name='signup'), 
    path('login/', user_login, name='login'), 
    path('profile/', profile, name='profile'), 
    path('logout/', user_logout, name='logout'), 
    path('password_change/', password_change, name='password_change'),
    path('password_change_simple/', password_change_simple, name='password_change_simple')
    
]
