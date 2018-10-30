from django.urls import path
from django.conf.urls import url, include
from .views import RESTStudentList
from .views import RESTStudentDetail

from . import views
app_name = 'Table'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.students, name='students'),
    path('rest-api/student-list/', RESTStudentList.as_view(), name ='rest_student_list'),
    
    url(r'^rest-api/student-detail/(?P<pk>\d+)/$', RESTStudentDetail.as_view(), name="rest_student_detail"),
]