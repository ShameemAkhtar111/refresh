from django.urls import path
from . import views

app_name="process"

urlpatterns = [
    path("", views.index, name="index"),
    path("formf/", views.form_render, name="form_render"),
    path("success/", views.success_form_submit, name="successf")
]