from django import forms
from login.models import *

class userForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'firstname',
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
            'email',
            'firstname',
            'surname',
            'position',
            'yearsOfExperience',
            'industry',
            'region',
            'province',
            'city',
            'age',
            'dateadded',
            'isAgeViewable'
        ]