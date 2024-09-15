from django.urls import path, include
from.views import SignUpView, TemplateView, LoginView

urlpatterns = [
    ...,

    path('/', include('django.contrib.auth.urls')),
    path('accounts/profile/',
             TemplateView.as_view(template_name='profile.html'),
             name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
    path("login/", LoginView.as_view(), name="templates/registration/login"),
        ...
]