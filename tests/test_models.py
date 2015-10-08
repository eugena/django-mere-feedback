#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_mere_feedback
------------

Tests for `django_mere_feedback` models module.
"""

from django.test import TestCase

from feedback import models


class TestFeedback(TestCase):

    def setUp(self):
        pass

    def test_model(self):
        self.assertTrue(models.Message.objects.create(
            text='foo'))

    def tearDown(self):
        pass
