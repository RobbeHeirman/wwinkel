from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from .models import User, OrganisationUser, Organisation, Address
from django import forms
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('email', 'telephone', 'gsm')



class UserChangeForm(BaseUserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = '__all__'


class OrganisationUserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = OrganisationUser
        fields = ['organisation','email','first_name','last_name','telephone']



class OrganisationUserChangeForm(BaseUserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = OrganisationUser
        fields = '__all__'


class ManagerUserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = OrganisationUser
        fields = '__all__'
        # fields = ('email', 'telephone', )


class ManagerUserChangeForm(BaseUserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = OrganisationUser
        fields = '__all__'

class PasswordField(forms.CharField):
    widget = forms.PasswordInput

class LoginForm(forms.Form):
    e_mail = forms.EmailField()
    password = PasswordField()


class OrganisationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = ['name', 'recognised_abbreviation', 'legal_entity', 'type', 'telephone','website', 'goal','how_know_ww', 'remarks']

        labels = {
            'name': '*Naam Organisatie',
            'recognised_abbreviation': 'Afkorting Organisatie',
            'legal_entity': '*Juridische entiteit',
            'telephone': 'Telefoon',
            'website': 'website',
            'goal': '*Doel organisatie',
            'remarks': 'Opmerkingen'

        }
        help_texts = {
            'telephone': _('Nummer waarop we het bedrijf kunnen contacteren')
        }


class AdressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'

        labels = {
            'province': '*Provincie',
            'city': '*Stad',
            'postal_code': '*Postcode',
            'street_name': '*Straat naam',
            'street_number': '*PostNummer'
        }

class BaseOrganisationUserForm(OrganisationUserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = OrganisationUser
        fields = ['email', 'first_name', 'last_name', 'telephone']
        labels = {'telephone': 'Telefoon'}
