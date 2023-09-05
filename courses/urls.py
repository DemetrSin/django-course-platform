from django.urls import path
from . import views

urlpatterns = [
    path('add-course', views.AddCourse.as_view(), name='add-course'),
    path('course/<int:course_id>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('', views.HomePage.as_view(), name='home'),
    path('tariffs', views.tariffsPage, name='tariffs'),
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course-detail'),
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail'),
]
