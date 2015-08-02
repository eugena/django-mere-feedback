import json
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.utils.translation import ugettext as _
import forms


class FeedbackFormView(CreateView):
    """
    View for creating a new feedback
    """
    template_name = "feedback/feedback.html"
    form_class = forms.FeedbackForm

    def get_form_kwargs(self):
        """
        Returns the keyword arguments for instantiating the form.
        """
        kwargs = super(FeedbackFormView, self).get_form_kwargs()
        if isinstance(self.request.user, object):
            kwargs['user'] = self.request.user

        if 'data' in kwargs.keys():
            post = kwargs['data'].copy()
            if isinstance(self.request.user, User):
                post['user'] = self.request.user.pk
            post['url'] = self.request.get_full_path()
            kwargs['data'] = post

        if hasattr(settings, 'FEEDBACK_FORM_URL') and settings.FEEDBACK_FORM_URL:
            path = settings.FEEDBACK_FORM_URL
        else:
            path = self.request.get_full_path()
        if self.request.META['HTTP_REFERER'] != '%s://%s%s' % (
                self.request.is_secure() and 'https' or 'http',
                Site.objects.get_current().domain,
                path):
            kwargs['is_right_url'] = False
        return kwargs

    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        return self.request.get_full_path()

    def form_valid(self, form):
        """
        If the form is valid, save the model.
        """
        def send_notification():
            """
            Sends feedback notification email
            """
            result = {}
            data = form.cleaned_data
            try:
                send_mail(
                    'Feedback received: {}'.format(data['subject']),
                    'email: {} \n\n {}'.format(data['email'], data['text']),
                    settings.SERVER_EMAIL,
                    [settings.FEEDBACK_EMAIL],
                    fail_silently=False, )
            except:
                result = {'error': _('Failed to send email')}
            return result
        super(FeedbackFormView, self).form_valid(form)
        result = {}
        if hasattr(settings, 'FEEDBACK_EMAIL'):
            result = send_notification()

        if self.request.is_ajax():
            response = HttpResponse(json.dumps(result))
        else:
            response = self.render_to_response(result)
        return response

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        if self.request.is_ajax():
            response = HttpResponse(json.dumps({'errors': form.errors}))
        else:
            response = super(FeedbackFormView, self).form_invalid(form)
        return response