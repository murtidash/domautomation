from django.db import models


class Game(models.Model):
    GAME_STATUSES = [
        ('NEW','New Game'),
        ('PRETENDER','Game Accepting Pretenders'),
        ('RUNNING','Game Running'),
        ('STOPPED','Game Stopped'),
        ('COMPLETE','Game Complete')
    ]

    name = models.CharField(max_length=500)
    servername = models.CharField(max_length=64)
    status = models.CharField(max_length=15, choices=GAME_STATUSES)

    def __unicode__(self):
        return self.name

class ServerCommand(models.Model):
    SERVER_COMMANDS = [
        ('RESET','Reset Timer'),
        ('STOP','Stop Game'),
        ('START','Start (or Restart) Game'),
        ('SETTIMER','Set a Games Timer')
    ]
    COMMAND_STATUS = [
        ('NEW','New Command'),
        ('EXECUTING','Command being processed'),
        ('EXECUTED','Command complete')
    ]
    command = models.CharField(max_length=15, choices=SERVER_COMMANDS)
    arg1 = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=COMMAND_STATUS)
    game = models.ForeignKey(Game)

    def __unicode__(self):
        return self.game.name + " " + self.command + " " + self.arg1



