from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player')

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Match(models.Model):
    HOME_OR_AWAY_CHOICES = [
        ('H', 'Home'),
        ('A', 'Away')
    ]
    date = models.DateField()
    opposition = models.CharField(max_length=32)
    players = models.ManyToManyField(Player, related_name='matches')
    home_or_away = models.CharField(max_length=1, choices=HOME_OR_AWAY_CHOICES, default='H')

    def __str__(self):
        return "%s-%s-%s" % (self.opposition, self.date, self.home_or_away)


class PlayerVote(models.Model):
    player_voted_for = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='votes_for_player')
    player_voted_by = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='votes_by_player')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_votes')
    class Meta:
        unique_together = (('player_voted_by', 'match'),)
        index_together = (('player_voted_by', 'match'),)

    def save(self, *args, **kwargs):
        if self.player_voted_by == self.player_voted_for:
            raise Exception('not allowed to vote for yourself, cheeky bastard')
        super(PlayerVote, self).save(*args, **kwargs)

    def __str__(self):
        return "Vote for %s by %s in %s" % (str(self.player_voted_for), str(self.player_voted_by), str(self.match))


