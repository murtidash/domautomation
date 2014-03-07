from django.db import models


class Game(models.Model):
	GAME_STATUSES [
		('NEW','New Game'),
		('PRETENDER','Game Accepting Pretenders'),
		('RUNNING','Game Running'),
		('STOPPED','Game Stopped'),
		('COMPLETE','Game Complete')
	]

	name = models.CharField(max_length=500)
	servername = models.CharFiels(max_length=64)
	status = models.CharFiels(choices=GAME_STATUSES)

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
	command = models.CharField(choices=SERVER_COMMANDS)
	arg1 = models.CharField()
	status = models.CharField(choices=COMMAND_STATUS)
	game = ForeignKey(Game)
	

