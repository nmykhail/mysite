from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.index_other, name='index'),
    path('choice/', views.ChoiceList.as_view(), name='list'),
    path('choice/<int:choice_id>/', views.ChoiceDetail.as_view(), name='details'),

]
