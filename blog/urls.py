from django.urls import path
from . import views


urlpatterns = [  # IP주소/blog/

    path('category/<str:slug>/',views.category_page),
    path('', views.PostList.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()), # IP주소/blog/category/slug/
    path('<int:pk>/new_comment/', views.new_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>/',views.delete_comment),
    path('update_post/<int:pk>/',views.PostUpdate.as_view()), #IP주소/blog/update_post/slug/
    path('tag/<str:slug>/',views.tag_page),# IP주소/blog/tag/slug
    path('search/<str:q>/', views.PostSearch.as_view()), #
    path('Produce/<str:slug>/', views.produce_page),  # IP주소/blog/produce_slag/
    path('OptionColors/<str:slug>/', views.optioncolors_page), #IP주소/blog/produce_slag/
    path('me/', views.ME.as_view()),



]