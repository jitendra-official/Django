from django import forms
from m1.models import emp


class creat_form(forms.ModelForm):
    class Meta:
        model = emp
        fields = "__all__"