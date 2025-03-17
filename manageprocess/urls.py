from django.urls import path
from . import views

app_name="process"

urlpatterns = [
    path("", views.index, name="index"),
    path("formf/", views.add_group, name="add_group"),
    path("success/", views.success_form_submit, name="successf"),
    path("login/", views.login, name='login')
]