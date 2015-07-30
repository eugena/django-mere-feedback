from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

from views import FeedbackFormView

urlpatterns = patterns('',
    url(r'^', FeedbackFormView.as_view(), name='feedback'))
