from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from views import FeedbackFormView

urlpatterns = [
    url(r'^', FeedbackFormView.as_view(), name='feedback')]
