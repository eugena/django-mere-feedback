from django import forms
from django.utils.translation import ugettext as _
import models


class FeedbackForm(forms.ModelForm):
    """
    The form shown when giving feedback
    """
    is_right_url = True  # for trap spam bots.

    def __init__(self, user=None, is_right_url=True, prefix='feedback',
                 content_object=None, *args, **kwargs):

        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.is_right_url = is_right_url
        if user.is_authenticated():
            del self.fields['user_name']
            del self.fields['email']
        else:
            self.fields['user_name'].required = True
            self.fields['email'].required = True

    def clean_url(self):
        """
        Checks form referer
        """
        if not self.is_right_url:
            raise forms.ValidationError(_('Wrong form URL'))

    class Meta(object):
        model = models.Message
        exclude = ('site', )
        widgets = {
            'url': forms.HiddenInput(),
            'state': forms.HiddenInput()}
