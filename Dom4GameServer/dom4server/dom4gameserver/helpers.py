from subprocess import check_output, call
from django.template.loader import render_to_string
import re, os
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

def setperm(fname):
    call(['sudo','-u',settings.DOM4_USER,'chown','%s:%s' % (settings.DOM4_USER,settings.DOM4_USER), fname])


def makegamedir(game):
    fname = os.path.join(settings.DOM4SAVEGAME_DIR,game.servername)
    call(["mkdir", fname])
    setperm(fname)

def writegamefile(game):
    fname = os.path.join(settings.DOM4GAME_DIR,game.servername)
    ff = open(fname,"w")
    ff.write(render_to_string('dom4gameserver/gamefile',{'game':game}))
    ff.close()
    call(['chmod','+x',fname])
    setperm(fname)

def writegameprescript(game):
    fname = os.path.join(settings.DOM4SAVEGAME_DIR,game.servername,'pre.sh')
    ff = open(fname,"w")
    ff.write(render_to_string('dom4gameserver/pre.sh',{'game':game}))
    ff.close()
    call(['chmod','+x',fname])
    setperm(fname)

def writegamepostscript(game):
    fname = os.path.join(settings.DOM4SAVEGAME_DIR,game.servername,'post.sh')
    ff = open(fname,"w")
    ff.write(render_to_string('dom4gameserver/post.sh',{'game':game}))
    ff.close()
    call(['chmod','+x',fname])
    setperm(fname)





