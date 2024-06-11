from django.urls import path
from .views import EventDetail, EventListCreate, CategoryDetail, CategoryListCreate


urlpatterns = [
    path('events/', EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),


    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),


]
