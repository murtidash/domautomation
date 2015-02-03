from django.forms import ModelForm, Textarea, CheckboxInput
from dom4gameserver.models import Game

from django.utils.translation import ugettext_lazy as _


class GameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ['paused','status','port']
        labels = {
            'timer': _('Default Timer'),
        }
        widgets = {
            'notes': Textarea(attrs={'cols': 50, 'rows': 10}),
            'thrones': CheckboxInput(attrs={'id':'thrones_id','onclick':"showThrones();"}),
        }

class OtherGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['paused','status','port']





