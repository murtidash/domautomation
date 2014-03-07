from django.contrib import admin
from dom4gameserver.models import Game, ServerCommand
 

class GameAdmin(admin.ModelAdmin):
	list_display = ('name','status')


admin.site.register(Game, GameAdmin)
admin.site.register(ServerCommand)

