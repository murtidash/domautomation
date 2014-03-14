from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from subprocess import check_output, call
from optparse import make_option
import re

from dom4gameserver.models import Game
from dom4gameserver.helpers import findgameprocess



class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-g', '--game',
            dest='gamename',
            action='store',
            default='all',
            metavar='GAME',
            help='Game name to check'),
        )

    def handle(self, *args, **options):
        if options['gamename'] != 'all':
            self.stdout.write('Unimplemented Feature.')
        else:
            for gg in Game.objects.filter(status__in = ['PRETENDER','RUNNING']):
                if not findgameprocess(gg):
                    self.stdout.write("I didn't find game: %s.   Attempting to Restart..." % gg.name)
                    call(["sudo", '-u',settings.DOM4_USER,'%s' % gg.servername],cwd=settings.DOM4GAME_DIR)



