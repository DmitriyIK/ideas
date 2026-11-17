from django.urls import path

from . import views

urlpatterns = [
    path("", views.submit_idea, name="submit"),
    path("thanks/", views.thanks, name="thanks"),
    path("ideas/", views.published_ideas, name="published"),
    path("stats/", views.stats, name="stats"),
]
