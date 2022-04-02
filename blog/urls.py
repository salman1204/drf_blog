from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.blog_list),
    path('blog/<int:pk>/', views.blog_details)
]
