from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PlayerViewSet, MatchViewSet, PlayerVoteViewSet, UserViewSet


app_name = 'mainapp'


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('players', PlayerViewSet)
router.register('matches', MatchViewSet)
router.register('player_votes', PlayerVoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
