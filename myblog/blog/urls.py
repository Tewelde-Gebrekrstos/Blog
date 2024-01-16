from django.urls import path
from . import views
urlpatterns=[
    # path('',views.index, name='index'),
    path('home',views.view_news,name='news'),
    path('news',views.view_news,name='news'),
    path('sports',views.view_sports,name='sports'),
    path('bussines',views.view_bussiness,name='bussiness'),
    path('politics',views.view_politics,name='politcs'),
    path('news/detail/<int:id>',views.view_detail),
    # path('/view/edit/<int:id>',views.edit_emp)
]