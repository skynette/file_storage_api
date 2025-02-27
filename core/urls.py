from django.urls import path
from core.api import ListCreateFileAPI, GetUpdateDeleteFileAPI


app_name = "core"

urlpatterns = [
    path("files/", ListCreateFileAPI.as_view(), name="list-create-file"),
    path(
        "files/<slug:slug>/",
        GetUpdateDeleteFileAPI.as_view(),
        name="get-update-delete-file",
    ),
]
