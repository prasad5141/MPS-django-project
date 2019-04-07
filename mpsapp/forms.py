from django import forms
from . models import *




class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ShopkeeperForm(forms.ModelForm):
    class Meta:
        model = Shopkeeper
        fields = '__all__'


class ShopkeeperLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)



class ItemPostForm(forms.ModelForm):
    class Meta:
        model = ItemPost
        fields = '__all__'

class Payment_mode(forms.Form):
    select_choices =(('Net Banking','Net Banking'),
                   ('Debit Card','Debit Card'),
                   ('Credit card','Credit card')
                   )
    payment_mode = forms.ChoiceField(choices = select_choices)


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = '__all__'
