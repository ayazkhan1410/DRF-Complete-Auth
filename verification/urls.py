from django.urls import path, include
from verification import views

urlpatterns = [
   path('register/', views.RegistrationFormView.as_view(), name='register/'),
   path('login/', views.LoginFormView.as_view(), name='login/'),
   path('profile/', views.ProfileView.as_view(), name='profile/'),
   path('change-password/', views.ChangePasswordView.as_view(), name='change-password/'),
   path('rest-password/', views.RestPasswordView.as_view(), name='rest-password/'),
   path('password-rest/<str:uid>/<str:token>/', views.PasswordRestView.as_view(), name="password-rest/"),
   # path('password-rest/<str:<uid/>/<str:<token>/', views.PasswordRestView.as_view(), name="password-rest/")
]
