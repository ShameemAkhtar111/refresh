from django.urls import path
from . import views

app_name="process"

urlpatterns = [
    path("", views.index, name="index"),
    path("addgroup/", views.add_group, name="add_group"),
    path("success/", views.success_form_submit, name="successf"),
    path("addprocess/<str:group_name>", views.add_process, name="add_process"),
    path("login/", views.login, name='login')
]