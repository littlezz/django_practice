from django.db import models

# Create your models here.

from django.forms import ModelForm,Textarea,TextInput,Select
from captcha.fields import CaptchaField

SEX_CHOICE=(
    ('women','Girl'),
    ('man','Boy'),
    ('both','Double sex'),
    )

class registerModel(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(max_length=6,help_text='your name!baby!',)
    sex=models.CharField(max_length=20,choices=SEX_CHOICE)
    reason=models.CharField(max_length=200)
    

class registerForm(ModelForm):

    captcha=CaptchaField()

    class Meta:
        model=registerModel
        fields=('name','sex','reason')
        widgets={
            'reason':Textarea(attrs={'cols':80,'rows':5,'class':'form-control'}),
            'name':TextInput(attrs={'class':'form-control'}),
            'sex':Select(attrs={'class':'form-control'})
        }
        #labels={'name':('中文'),}
        
        


























"""
from django import forms

class RegisterForm(forms.Form):
    sex_choice=(('man','Man'),
                ('women','Women'),
                )
    name= forms.CharField(max_length=100)
    show_yourself=forms.CharField(label='why you come',help_text='heihei~')
    sex=forms.ChoiceField(choices=sex_choice)
"""

