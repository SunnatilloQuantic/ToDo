from django.conf.urls import url
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    url(r'^signup/', UserRegistrationView.as_view(), name = 'Sign Up'),
    url(r'^signin/', UserLoginView.as_view(), name = 'Sign In'),
]