from django.urls import path

from labels import views


app_name = 'labels'
urlpatterns = [
    path('', views.LabelListView.as_view(), name='index'),
    path('create/', views.LabelCreateView.as_view(), name='create'),
]
