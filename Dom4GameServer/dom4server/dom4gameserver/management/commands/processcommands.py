from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from subprocess import check_output, call
from optparse import make_option
import re

from dom4gameserver.models import Game, ServerCommand
from dom4gameserver.helpers import killgame



class Command(BaseCommand):

    def handle(self, *args, **kargs):
        for cmd in ServerCommand.objects.filter(status__exact = "NEW"):
            if cmd.command == 'RESET':
                killgame(cmd.game)
                cmd.status = 'EXECUTED'
                cmd.save()






