from django.urls import path
from .views import JobPostList, JobPostRetrieveUpdateDestroy, CreateLike

app_name = 'job_post'

urlpatterns = [
    path('', JobPostList.as_view()),
    path('<int:pk>', JobPostRetrieveUpdateDestroy.as_view()),
    path('<int:pk>/like', CreateLike.as_view()),
]