from allauth.account.forms import SignupForm as AllauthSignupForm
from allauth.socialaccount.forms import SignupForm
from django.contrib.auth.models import Group


class CustomSignupForm(AllauthSignupForm):
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class CustomSocialSignupForm(SignupForm):
    
    def __init__(self, sociallogin=None, *args, **kwargs):
    super().__init__(*args, **kwargs)

    
    def save(self, request):
        user = super(CustomSocialSignupForm, self).save(request)
        print('Is saving user...')
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
