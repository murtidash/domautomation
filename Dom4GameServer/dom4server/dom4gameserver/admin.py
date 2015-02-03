from django.contrib import admin
from dom4gameserver.models import Game, ServerCommand, Request


class GameAdmin(admin.ModelAdmin):
    list_display = ('name','status','timer','paused')

class RequestAdmin(admin.ModelAdmin):
    fields = ( 'command', 'arg1', 'status', 'game' ,'serverCommand', 'requestDate', 'approvedDate' )



admin.site.register(Game, GameAdmin)
admin.site.register(ServerCommand)
admin.site.register(Request) #, RequestAdmin)
