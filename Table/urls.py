from django.urls import path

from . import views
app_name = 'Table'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.students, name='students'),
]