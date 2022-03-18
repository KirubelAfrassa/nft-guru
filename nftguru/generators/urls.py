from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "generators"
urlpatterns = [
    path("images", views.LayerImageList.as_view()),
    path("images/<int:pk>", views.ImageDetail.as_view()),
    path("preview", views.Preview.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
