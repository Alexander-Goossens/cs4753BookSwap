from django import forms
from django.contrib.auth.models import User
from home.models import Book
from django.forms.extras.widgets import SelectDateWidget

YEAR_CHOICES = ('2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username','email','password')

class BookForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES))
    class Meta:
        model = Book
        exclude = ('booker',)