from django.contrib import admin
from dom4gameserver.models import Game, ServerCommand
 

class GameAdmin(admin.PollAdmin):
	list_display = ('name','status')


admin.site.register(Game)
admin.site.register(ServerCommand)

