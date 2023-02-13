from django.urls import path

from .import views


urlpatterns = [
    path("register", views.register_request, name="register"),

    path('', views.index, name='index'),

    path('<int:task_id>/', views.detail, name='detail'),
]
