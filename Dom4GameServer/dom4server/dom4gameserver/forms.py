from django.forms import ModelForm, Textarea, CheckboxInput, Select
from dom4gameserver.models import Game

from django.utils.translation import ugettext_lazy as _


class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ['paused','status','port','masterpass']
        labels = {
            'timer': _('Default Timer'),
        }
        widgets = {
            'notes': Textarea(attrs={'cols': 50, 'rows': 10}),
            'thrones': CheckboxInput(attrs={'id':'thrones_id','onclick':"showThrones();"}),
            'maptype': Select(attrs={'id':'maptype_id','onchange':'showMap();'}),
        }

class OtherGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['paused','status','port','masterpass','extraswitches']





