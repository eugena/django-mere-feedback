# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Default message subjects
default_subjects = (
    ('suggestion', _('Suggestion')),
    ('error', _('Error')),
)

# Default message states
default_states = (
    ('new', _('New')),
    ('read', _('Read')),
    ('trash', _('Trash')),
)


def get_default_subject():
    """
    Defining of message default subject
    """
    if hasattr(settings, 'FEEDBACK_DEFAULT_SUBJECT'):
        subject = settings.FEEDBACK_DEFAULT_SUBJECT
    else:
        try:
            subject = get_subjects()[0][0]
        except IndexError:
            subject = None
    return subject


def get_subjects():
    """
    Defining of message subjects
    """
    if hasattr(settings, 'FEEDBACK_SUBJECTS'):
        subjects = settings.FEEDBACK_SUBJECTS
    else:
        subjects = default_subjects
    return subjects


def get_default_state():
    """
    Defining of message default subject
    """
    if hasattr(settings, 'FEEDBACK_DEFAULT_STATE'):
        state = settings.FEEDBACK_DEFAULT_STATE
    else:
        try:
            state = get_states()[0][0]
        except IndexError:
            state = None
    return state


def get_states():
    """
    Defining of message states
    """
    if hasattr(settings, 'FEEDBACK_STATES'):
        states = settings.FEEDBACK_STATES
    else:
        states = default_states
    return states


class Message(models.Model):
    """
    Feedback model
    """
    user = models.ForeignKey(User, null=True, blank=True, verbose_name=_(u'User'))
    user_name = models.CharField(_(u'Your name'), max_length=255, blank=True, null=True)
    site = models.ForeignKey(Site, verbose_name=_(u'Site'), default=Site.objects.get_current())
    url = models.CharField(_(u'Url'), max_length=255, blank=True, null=True)
    subject = models.CharField(_(u'Subject'), max_length=15, blank=True, null=True,
                               choices=get_subjects(), default=get_default_subject())
    email = models.EmailField(_(u'Email'), blank=True, null=True)
    text = models.TextField(_(u'Text'), )
    created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(_(u'State'), max_length=15,
                             choices=get_states(), default=get_default_state())

    def __unicode__(self):
        return u'%s: %s (%s)' % (self.user_name or self.user, self.get_subject_display(), self.created)

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")