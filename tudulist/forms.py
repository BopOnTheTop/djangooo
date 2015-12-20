__author__ = 'masterbob'
from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget

class QuestForm(forms.Form):
    quest = forms.CharField(label=u"Квест")
    whois = forms.CharField(label=u"Квестодавець")
    given = forms.DateField(label=u"Видано",required=False,widget=SelectDateWidget)
    deadline = forms.DateField(label=u"Дедлайн",widget=SelectDateWidget)
    done = forms.BooleanField(widget=widgets.CheckboxInput, label=u"Здано?",required=False)
    progress = forms.CharField(label=u"Прогрессс",required=False)
    CHOICES = (('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',), ('5', '5',))
    priority = forms.ChoiceField(widget=widgets.Select, label="Пріоритет", choices=CHOICES)
    notes = forms.CharField(widget=forms.Textarea, label=u"Нотатки",required=False)
