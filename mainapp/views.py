from django.shortcuts import render
from rest_framework import viewsets, response, status, decorators
from .models import Player, Match, PlayerVote
from .serializers import PlayerSerializer, MatchSerializer, PlayerVoteSerializer
from django.views import generic
from pprint import pprint as pp
from django.contrib.auth.models import User
# Create your views here.


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    @decorators.action(detail=True, methods=['GET'])
    def get_man_of_the_match(self, request, pk=None):
        player_to_number_of_votes = {}
        match = Match.objects.get(id=pk)
        players = match.players.get_queryset()
        for player in players:
            player_to_number_of_votes[player] = player.votes_for_player_in_match(match_id=pk)



class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerVoteViewSet(viewsets.ModelViewSet):
    queryset = PlayerVote.objects.all()
    serializer_class = PlayerVoteSerializer


class AllMatchView(generic.ListView):
    template_name = 'mainapp/all_matches.html'
    context_object_name = 'list_of_matches'

    def get_queryset(self):
        return Match.objects.all()

class MatchView(generic.DetailView):
    model = Match
    template_name = 'mainapp/match_view.html'
