from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from dom4gameserver.models import Request, Game
from dom4gameserver.forms import GameForm, OtherGameForm

# Create your views here.

def index(request):
    return render(request, 'dom4gameserver/index.html',
            { 'reqs'  : Request.REQUEST_COMMANDS,
              'games' : Game.objects.filter(status__in = ['PRETENDER','RUNNING']),
              'vreqs' : Request.objects.filter(status__in = ['NEW','APPROVED','PROCESSED','DECLINED'])

    })


def newgame(request):
    if request.method == "GET":
        form = GameForm()
        return render(request, 'dom4gameserver/newgame.html',
            {
           'form' : form
           })
    elif request.method == "POST":
        f = GameForm(request.POST)
        ng = f.save(commit=False)
        ng.port = 1224
        ng.status = "NEW"
        ng.save()
        re = Request()
        re.game = ng
        re.status = "NEW"
        re.command = "NEWGAME"
        re.save()


    return HttpResponseRedirect(reverse('dom4gameserver:index'))


def viewgame(request, gameid):
    gg = get_object_or_404(Game, pk=gameid)
    form = GameForm(instance=gg)
    oform = OtherGameForm(instance=gg)
    return render(request, 'dom4gameserver/viewgame.html',
        {
       'form' : form,
       'otherform': oform
       })


def newrequest(request):

    game = Game.objects.get(pk = request.POST['game'])
    cmd = request.POST['command']

    req = Request()
    req.command = cmd
    req.game = game
    req.status = 'NEW'
    #req.command = "NEWGAME"
    req.save()

    return HttpResponseRedirect(reverse('dom4gameserver:index'))



def approve(request, req_id):
    if(not request.user.is_authenticated or not request.user.has_perm('approve_requests')):
        return HttpResponseRedirect(reverse('dom4gameserver:index'))
    req = get_object_or_404(Request, pk=req_id)
    req.status = "APPROVED"
    req.save()

    return  HttpResponseRedirect(reverse('dom4gameserver:index'))

def close(request, req_id):
    if(not request.user.is_authenticated or not request.user.is_staff):
        return HttpResponseRedirect(reverse('dom4gameserver:index'))
    req = get_object_or_404(Request, pk=req_id)
    req.status = "CLOSED"
    req.save()

    return  HttpResponseRedirect(reverse('dom4gameserver:index'))

