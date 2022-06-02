from django.urls import path
from base.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
          path('login/', CustomLoginView.as_view(), name='login'),
          path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
          path('register/', RegisterPage.as_view(), name='register'),

          path('',home,name="home"),
          path('hospital_card/',Hospital_card.as_view(), name='hospital_card'),
          path('complaint/',Complaint.as_view(),name='complaint'),

]