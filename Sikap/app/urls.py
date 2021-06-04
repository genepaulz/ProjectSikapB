from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('',views.LandingView.as_view(),name="landing_view"),
    path('login/',views.LoginView.as_view(),name="login_view"),
    path('register/a',views.RegisterViewA.as_view(),name="registera_view"),
    path('register/e',views.RegisterViewE.as_view(),name="registere_view"),
    path('view/a',views.ViewAsAView.as_view(),name="viewasa_view"),
    path('view/e',views.ViewAsEView.as_view(),name="viewase_view"),
    path('posts/',views.PostsView.as_view(),name="posts_view"),
    path('view/get/ajax/friend', views.LiveSearch , name="LiveSearch"),
]