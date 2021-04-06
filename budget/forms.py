from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from budget.models import expense,category
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class userregistrationform(UserCreationForm):
    class Meta():
        model=User         #builtin model
        fields=['username','first_name','last_name','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

class createexpenseform(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget())
    class Meta():
        model=expense
        fields='__all__'
        widgets={
                'notes':forms.TextInput(attrs={'class':'form-control'}),
                'amount': forms.TextInput(attrs={'class': 'form-control'}),
                'user': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'})
        }
    def clean(self):
        cleaned_data=super().clean()
        amount=cleaned_data.get('amount')
        if amount<50:
            msg='invalid amount'
            self.add_error('amount',msg)
class createcategoryform(ModelForm):
    class Meta():
        model=category
        fields='__all__'

class datesearchform(forms.Form):
    date=forms.DateField(widget=forms.SelectDateWidget())

class review_expenseform(forms.Form):
    from_date=forms.DateField(widget=forms.SelectDateWidget())
    to_date = forms.DateField(widget=forms.SelectDateWidget())