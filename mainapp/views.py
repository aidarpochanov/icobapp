from django.shortcuts import render
from rest_framework import viewsets, response, status, decorators
from .models import Player, Match, PlayerVote
from .serializers import PlayerSerializer, MatchSerializer, PlayerVoteSerializer, UserSerializer
from django.views import generic
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from pprint import pprint as pp
from django.contrib.auth.models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)

    @decorators.action(methods=['POST'], detail=True)
    def add_player(self, request, pk=None):
        player = Player.objects.get(user=request.user)
        match = Match.objects.get(id=int(pk))
        players_in_match = match.players.all()
        if player not in players_in_match:
            match.players.add(player)
            r = response.Response(data={'response': 'You have made player %s available for this match' %str(player)})
        else:
            r = response.Response(data={'response': 'Player %s already available for this match' %str(player)})
        return r

    @decorators.action(methods=['POST'], detail=True)
    def remove_player(self, request, pk=None):
        player = Player.objects.get(user=request.user)
        match = Match.objects.get(id=int(pk))
        if player in match.players.all():
            match.players.remove(player)
            r = response.Response(data={'response': 'You have removed player %s from available players' % str(player)})
        else:
            r = response.Response(data={'response': 'Player %s has not signed up for this game' % str(player)})
        return r

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )
    permission_classes = (AllowAny,)


class PlayerVoteViewSet(viewsets.ModelViewSet):
    queryset = PlayerVote.objects.all()
    serializer_class = PlayerVoteSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (AllowAny,)


