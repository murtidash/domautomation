from django.core.management.base import BaseCommand, CommandError
from dom4gameserver.models import Game
from subprocess import check_output, call
from optparse import make_option
import re


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
            processes = check_output(['ps','ax']).splitlines()
            prore = ".*?dom4.*?%s"


            for gg in Game.objects.filter(status__in = ['PRETENDER','RUNNING']):
                found = False
                for pro in processes:
                    mo = re.search(prore % gg.servername,pro)
                    if mo:
                        found = True
                        self.stdout.write("Game: %s found in line: %s" % (gg.name, pro))
                if not found:
                    self.stdout.write("I didn't find game: %s.   Attempting to Restart..." % gg.name)
                    call("./%s" % gg.servername,cwd="/var/dom4/games/")



