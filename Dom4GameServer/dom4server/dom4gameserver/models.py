from django.db import models


class Game(models.Model):
    GAME_STATUSES = [
        ('NEW','New Game'),
        ('PRETENDER','Game Accepting Pretenders'),
        ('RUNNING','Game Running'),
        ('STOPPED','Game Stopped'),
        ('COMPLETE','Game Complete')
    ]

    AGES = [
        (1 , 'Early Age'),
        (2 , 'Middle Age'),
        (3 , 'Late Age')
    ]

    MAP_TYPES = [
        (1 , 'Random Map'),
        (2 , 'Pregenerated Map'),
    ]

    name = models.CharField(max_length=500)
    servername = models.CharField(max_length=64)
    status = models.CharField(max_length=15, choices=GAME_STATUSES)
    timer = models.IntegerField(blank=True)
    paused = models.BooleanField(default=False)
    port = models.IntegerField(blank=True)
    age = models.IntegerField(choices=AGES)
    thrones = models.BooleanField(default=False)
    throne1 = models.IntegerField(blank=True)
    throne2 = models.IntegerField(blank=True)
    throne3 = models.IntegerField(blank=True)
    thronewin = models.IntegerField(blank=True)
    maptype = models.IntegerField(choices=MAP_TYPES)
    randmap = models.IntegerField(blank=True, default=15)
    mapfile = models.CharField(max_length=64, blank=True)
    masterpass = models.CharField(max_length=24)

    notes = models.CharField(max_length=3000, blank=True, null=True)
    extraswitches = models.CharField(max_length=3000, blank=True, null=True)




    def __unicode__(self):
        return self.name

class ServerCommand(models.Model):
    SERVER_COMMANDS = [
        ('RESET','Reset Timer'),
        ('STOP','Stop Game'),
        ('START','Start (or Restart) Game'),
        ('SETTIMER','Set a Games Timer'),
        ('CREATEGAME','Create the Game Script')
    ]
    COMMAND_STATUS = [
        ('NEW','New Command'),
        ('EXECUTING','Command being processed'),
        ('EXECUTED','Command complete')
    ]
    command = models.CharField(max_length=15, choices=SERVER_COMMANDS)
    arg1 = models.CharField(max_length=25, blank=True)
    status = models.CharField(max_length=15, choices=COMMAND_STATUS)
    game = models.ForeignKey(Game)

    def __unicode__(self):
        return self.game.name + " " + self.command + " " + self.arg1

class Request(models.Model):
    class Meta:
        permissions = (
            ('approve_requests','Can Approve Requests'),
        )
    REQUEST_STATUS = [
            ('NEW','New Request'),
            ('APPROVED', 'Request Approved'),
            ('PROCESSED', 'Request Processed'),
            ('DECLINED', 'Request Declined'),
            ('CLOSED', 'Request Closed')
            ]
    REQUEST_COMMANDS = [
            ('RESET','Timer Reset'),
            ('SETTIMER', 'Set Game Timer'),
            ('PAUSE', 'Pause Game Timer'),
            ('UNPAUSE', 'Restore Game Timer'),
            ('NEWGAME', 'Request New Game')
            ]

    command = models.CharField(max_length=15, choices=REQUEST_COMMANDS)
    arg1 = models.CharField(max_length=25, blank=True)
    status = models.CharField(max_length=15, choices=REQUEST_STATUS, default='NEW')
    game = models.ForeignKey(Game)
    serverCommand = models.ForeignKey(ServerCommand, blank=True, null=True)
    requestDate = models.DateTimeField(auto_now_add = True)
    approvedDate = models.DateTimeField(editable=False, null=True)

    def __unicode__(self):
        return self.game.name + " " + self.command + " " + self.arg1


