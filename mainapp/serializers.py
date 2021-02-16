from rest_framework import serializers
from .models import Player, Match, PlayerVote
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'surname', 'matches')
        depth = 1


class PlayerVoteSerializer(serializers.ModelSerializer):
    player_voted_by = PlayerSerializer(many=False)
    player_voted_for = PlayerSerializer(many=False)
    class Meta:
        model = PlayerVote
        fields = ('id', 'player_voted_for', 'player_voted_by', 'match')


class MatchSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True)
    class Meta:
        model = Match
        fields = ('id', 'date', 'opposition', 'players', 'player_votes')
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True}
                        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        Player.objects.create(name=validated_data['first_name'], surname=validated_data['last_name'], user=user)
        return user
