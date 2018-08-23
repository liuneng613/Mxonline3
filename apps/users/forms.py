__author__ = 'ratel'
__date__ = '2018/8/23 9:49'

from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)