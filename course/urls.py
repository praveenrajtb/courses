from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course'),
    path('create', views.CourseCreateView.as_view(), name='course-create'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]
