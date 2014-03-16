from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from dom4gameserver.models import Request, Game

# Create your views here.

def index(request):
    return render(request, 'dom4gameserver/index.html', 
            { 'reqs'  : Request.REQUEST_COMMANDS,
              'games' : Game.objects.filter(status__in = ['PRETENDER','RUNNING']),
              'vreqs' : Request.objects.filter(status__in = ['NEW','APPROVED','PROCESSED','DECLINED'])
              
    })

def newrequest(request):

    game = Game.objects.get(pk = request.POST['game'])
    cmd = request.POST['command']

    req = Request()
    req.command = cmd
    req.game = game
    req.status = 'NEW'
    req.save()
    
    return HttpResponseRedirect(reverse('dom4gameserver:index'))



def approve(request, req_id):
    if(not request.user.is_authenticated or not request.user.is_staff):
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

