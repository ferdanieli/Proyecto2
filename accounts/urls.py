from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import login_request

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
]