from django.urls import path
from django.conf.urls import url, include
from .views import RESTStudentList
from .views import RESTStudentDetail

from . import views
app_name = 'Table'
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('rest-api/student-list/', RESTStudentList.as_view(), name ='rest_student_list'), 
    url(r'^rest-api/student-detail/(?P<pk>\d+)/$', RESTStudentDetail.as_view(), name="rest_student_detail"),
]