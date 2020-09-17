from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('signup/', views.login, name='signup'),
    path('login/', views.login, name='login'),
]
