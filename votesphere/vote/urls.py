from django.urls import path
from .views import home, vote, login_view,index,manager_login,manager_register,manager_dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('', home, name='home'),
    path('vote/<int:candidate_id>/', vote, name='vote'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('manager/dashboard/', manager_dashboard, name='manager_dashboard'),
    path('manager/register/', manager_register, name='manager_register'),
    path('manager/login/', manager_login, name='manager_login'),
    path('manager/logout/', LogoutView.as_view(), name='manager_logout'),
]
