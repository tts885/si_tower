from email import message
from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):

        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        user.Invitation_code = form.cleaned_data.get('Invitation_code')
        # if form.cleaned_data.get('Invitation_code') not in ('9000'):
        #     return message 

        user.save()