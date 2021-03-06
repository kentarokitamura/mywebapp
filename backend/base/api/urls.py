from django.urls import path
from . import views
from .views import MyTokenObtainPairView, buyTicket
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    path('events/',views.getEvents),
    path('events/<str:pk>',views.getEvent),
    path('seat/<str:pk>',views.getSeat),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',views.registerUser),
    path('create/',views.createEvent),
    path('update/<str:pk>',views.updateEvent),
    path('user/',views.getUserEvent),
    path('buy/<str:pk>',views.buyTicket),


]
