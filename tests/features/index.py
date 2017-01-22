# Author: Michael Hawes
# Coconut Karaoke
# Integration Testing
# steps.py

"""
Integration test: Test communication paths between
different parts of the module done by the test department
or by developers to show that all modules work correctly together.
"""

from behave import *

@given('I am on the homepage')
def step_impl(context):
    context.browser.get('http://localhost:8000/index')


# @when(u'I choose a genre')
# def step_impl(context):
#     pass
