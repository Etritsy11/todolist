"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signupuser/', views.sign_up_user, name="signupuser"),
    path('loginuser/', views.login_user, name="loginuser"),
    path('logoutuser/', views.logout_user, name="logoutuser"),
    # Todos

    path('', views.home, name="home"),
    path('create/', views.create_to_do, name="createtodo"),
    path('current/', views.current_to_dos, name="currenttodos"),
    path('completed/', views.completed_to_dos, name="completedtodos"),
    path('todo/<int:todo_pk>/', views.view_todo, name="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name="completetodo"),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name="deletetodo"),

    # API
    path('api/', include('api.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
