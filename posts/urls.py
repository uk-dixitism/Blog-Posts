from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('postDelete/<str:pk>', views.delete, name='postDelete'),
    path('postCreate', views.create, name='postCreate'),
    path('postCreate2', views.create2, name='postCreate2'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('edit2/<str:pk>', views.edit2, name='edit2'),

    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]