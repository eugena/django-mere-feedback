=============================
django-mere-feedback
=============================

.. image:: https://badge.fury.io/py/django-mere-feedback.png
    :target: https://badge.fury.io/py/django-mere-feedback

.. image:: https://coveralls.io/repos/eugena/django-mere-feedback/badge.png
    :target: https://coveralls.io/r/eugena/django-mere-feedback?branch=master

.. image:: https://travis-ci.org/eugena/django-mere-feedback.png?branch=master
    :target: https://travis-ci.org/eugena/django-mere-feedback

.. image:: https://requires.io/github/eugena/django-mere-feedback/requirements.svg?branch=master
     :target: https://requires.io/github/eugena/django-mere-feedback/requirements/?branch=master
     :alt: Requirements Status

Django feedback

Documentation
-------------

The full documentation is at https://django-mere-feedback.readthedocs.org.

Quickstart
----------

Install django-mere-feedback::

    pip install django_mere_feedback

Then use it in a project::

    import feedback

Features
--------

## Available Settings
Required:
```python
FEEDBACK_EMAIL
```

Optional:
```python
FEEDBACK_SUBJECTS
FEEDBACK_DEFAULT_SUBJECT
FEEDBACK_STATES
FEEDBACK_DEFAULT_STATE
FEEDBACK_FORM_TEXT
FEEDBACK_FORM_SUCCESS_TEXT
FEEDBACK_FORM_URL
```
## Available Fields
```python

    user # Django User

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


Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
