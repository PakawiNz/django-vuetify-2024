from django.urls import path

from control.views import login_view, logout_view, redirect_view

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('redirect/', redirect_view),
]