from dealerapp import views
from django.urls import path,include
from django.contrib.auth import views as auth


urlpatterns = [
    path('', views.home, name='home'),
    path('dealerregister', views.DealerListView.as_view(), name='dealerregister'),
    path('dealerlist/', views.list_dealer, name='dealerlist'),
    path('success', views.success, name ='success'),
    path('contactus', views.contact, name ='contactus'),
    #path('registration/', views.DealerCreateView.as_view(), name='dealer_add'),
    path('dealer_detail/<int:pk>/', views.Dealer_detail, name='dealer_detail'),
    path('ajax/load-blocks/', views.load_blocks, name='ajax_load_blocks'),
    path('ajax/load-panchayats/', views.load_panchayats, name='ajax_load_panchayats'),
    path('login/', views.login, name ='login'),
    path('logout/', views.login, name ='logout'),
    #path('register/', views.register, name ='register'),
]
