from subprocess import check_output, call
import re
from django.conf import settings

def findgameprocess(gg):
    processes = check_output(['ps','ax']).splitlines()
    prore = ".*?dom4.*?%s"
    for pro in processes:
        mo = re.search(prore % gg.servername,pro)
        if mo:
            return pro
    return None


def killgame(game):
    processline = findgameprocess(game)
    if not processline:
        return None
    pidre = r"\s*(\d+)\b"
    mo = re.match(pidre, processline)
    if mo == None:
        return None
    call(['kill','%s' % mo.group(1)])

def changetimer(game, duration):
    regex = r"s/hours [0-9]+/hours %d/" % (duration)
    call(["sed", '-ri',regex,'%s/%s' % (settings.DOM4GAME_DIR,game.servername)],cwd=settings.DOM4GAME_DIR)



