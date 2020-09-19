from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
<<<<<<< HEAD
    path('comment/update/<int:pk>', views.comment_update, name='comment_update'),
    path('comment/delete/<int:pk>', views.comment_delete, name='comment_delete'),
    path('home/', views.home, name='home'),
=======
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('home/', views.home, name="home"),
>>>>>>> c57f0f6268b34ad3ca6bb235a2c0d03cdf8d06ff
]
