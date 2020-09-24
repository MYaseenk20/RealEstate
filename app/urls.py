from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about, name='about'),
    path('listings/', views.listings, name='listings'),
    path('listing/<str:pk>/', views.listing, name='listing'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='app/reset_password.html'),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='app/reset_password_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='app/reset_password_complete.html'),
         name='password_reset_complete'
         )

]