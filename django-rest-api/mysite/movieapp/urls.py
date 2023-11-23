
from django.urls import path
from .views import MovieApiView, MovieDetailApiView

urlpatterns = [
                  path('', MovieApiView.as_view()),
                  path('<int:pk>/', MovieDetailApiView.as_view()),
              ]
