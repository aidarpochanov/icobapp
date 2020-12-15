from rest_framework import serializers
from .models import Player, Match, PlayerVote


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'date', 'opposition', 'players', 'player_votes')


class PlayerSerializer(serializers.ModelSerializer):
    matches = MatchSerializer(many=True)
    class Meta:
        model = Player
        fields = ('id', 'name', 'surname', 'user', 'votes_for_player', 'votes_by_player', 'matches')


class PlayerVoteSerializer(serializers.ModelSerializer):
    player_voted_by = PlayerSerializer(many=True)
    played_voted_for = PlayerSerializer(many=True)
    class Meta:
        model = PlayerVote
        fields = ('id', 'player_voted_for', 'player_voted_by', 'match')
