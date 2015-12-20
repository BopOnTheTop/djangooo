__author__ = 'masterbob'
from django import forms
from django.forms import widgets

class QuestForm(forms.Form):
    quest = forms.CharField(label=u"Квест")
    whois = forms.CharField(label=u"Квестодавець")
    given = forms.DateField(label=u"Видано")
    deadline = forms.DateField(label=u"Дедлайн")
    done = forms.BooleanField(widget=widgets.CheckboxInput, label=u"Здано?")
    progress = forms.CharField(label=u"Прогрессс")
    CHOICES = (('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',), ('5', '5',))
    priority = forms.ChoiceField(widget=widgets.Select, label="Пріоритет", choices=CHOICES)
    notes = forms.CharField(widget=forms.Textarea, label=u"Нотатки")


class CostForm(forms.Form):
    credit = forms.IntegerField(label=u"Кредит")
    debit = forms.IntegerField( label=u"Дебет")
    what_for = forms.DateField( label=u"На що")
    notes = forms.CharField(widget=forms.Textarea, label=u"Додаткові нотатки")
    percent = forms.IntegerField( label=u"Проценти")
    date = forms.DateField( label=u"Коли")
    from_who = forms.CharField(max_length=256,  label=u"Від кого")
    who_to = forms.CharField(max_length=256,  label=u"Кому")