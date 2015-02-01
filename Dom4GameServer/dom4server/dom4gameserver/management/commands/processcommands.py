from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from subprocess import check_output, call
from optparse import make_option
import re

from dom4gameserver.models import Game, ServerCommand, Request
from dom4gameserver.helpers import killgame, changetimer



class Command(BaseCommand):

    def handle(self, *args, **kargs):
        for cmd in ServerCommand.objects.filter(status__exact = "NEW"):
            executed = False
            if cmd.command == 'RESET':
                killgame(cmd.game)
                executed = True
            if cmd.command == 'STOP':
                cmd.game.status = 'STOPPED'
                cmd.game.save()
                killgame(cmd.game)
                executed = True
            if cmd.command == 'SETTIMER':
                changetimer(cmd.game,int(cmd.arg1));
                killgame(cmd.game)
                executed = True
            if executed:
                cmd.status = 'EXECUTED'
                cmd.save()

        for req in Request.objects.filter(status__exact = "APPROVED"):
            processed = False
            if req.command == 'RESET':
                newc = ServerCommand()
                newc.command = 'RESET'
                newc.game = req.game
                newc.status = "NEW"
                newc.save()
                processed = True
            if req.command == 'PAUSE':
                newc = ServerCommand()
                newc.command = 'SETTIMER'
                newc.game = req.game
                newc.arg1 = '300'
                newc.status = "NEW"
                req.game.paused = True
                req.game.save()
                newc.save()
                processed = True
            if req.command == 'UNPAUSE':
                newc = ServerCommand()
                newc.command = 'SETTIMER'
                newc.game = req.game
                newc.arg1 = str(req.game.timer)
                newc.status = "NEW"
                req.game.paused = False
                req.game.save()
                newc.save()
                processed = True
            if processed:
                req.status = "PROCESSED"
                req.save()
        for req in Request.objects.filter(status__exact = "CLOSED"):
            req.delete()







