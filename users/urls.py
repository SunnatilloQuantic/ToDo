from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/list/', views.userList, name='Users list'),
]
