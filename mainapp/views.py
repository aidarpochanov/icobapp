from django.shortcuts import render
from rest_framework import viewsets, response, status, decorators
from .models import Player, Match, PlayerVote
from .serializers import PlayerSerializer, MatchSerializer, PlayerVoteSerializer, UserSerializer
from django.views import generic
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from pprint import pprint as pp
from django.contrib.auth.models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    @decorators.action(detail=True, methods=['POST'])
    def vote(self, request, pk=None):
        match = Match.objects.get(id=pk)
        player_voted_for = Player.objects.get(id=request.data['player_voted_for'])
        player_voted_by = Player.objects.get(id=request.data['player_voted_by'])
        PlayerVote.objects.create(player_voted_by=player_voted_by, player_voted_for=player_voted_for, match=match)
        r = {'message': 'vote saved', 'player_for': str(player_voted_for), 'player_by': str(player_voted_by)}
        return response.Response(r, status=status.HTTP_200_OK)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

class PlayerVoteViewSet(viewsets.ModelViewSet):
    queryset = PlayerVote.objects.all()
    serializer_class = PlayerVoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AllMatchView(generic.ListView):
    template_name = 'mainapp/all_matches.html'
    context_object_name = 'list_of_matches'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Match.objects.all()


class MatchView(generic.DetailView):
    model = Match
    template_name = 'mainapp/match_view.html'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

