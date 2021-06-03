from django import forms
from login.models import *

class userForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'account_type',
            'email',
            'password',
            'name',
            'surname',
            'user_type',
            'isVerified',
            'companyName',
            'industry',
            'region',
            'province',
            'city',
            'age',
        ]

class postsForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = [
            'yearsOfExperience',
            'industry',
            'region',
            'province',
            'city',
            'age',
            'dateadded',
            'email',
            'isAgeViewable'
        ]