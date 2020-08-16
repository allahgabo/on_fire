from django.urls import path
from . import views 
from course.views import BlogHome ,BlogDetail ,AddPostView,UpdatePostView ,DeletePostView,LikeView,AddCategeroyView,CatergoryView

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategeroyView.as_view(),name='add_category'),
    path('course-details/',views.course_details,name='course-details'),
    path('blog-home/',BlogHome.as_view(),name='blog-home'),
    path('detail/<int:pk>/',BlogDetail.as_view(),name='detail'),
    path('detail/edit/<int:pk>/',UpdatePostView.as_view(),name='update_post'),
    path('detail/<int:pk>/remove/',DeletePostView.as_view(),name='delete_post'),
   	path('contacts/',views.contacts,name='contacts'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('catergory/<str:cats>/',CatergoryView,name='catergory'),
]
