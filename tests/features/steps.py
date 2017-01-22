# Author: Michael Hawes
# Coconut Karaoke
# Integration Testing
# steps.py

"""
Integration test: Test communication paths between
different parts of the module done by the test department
or by developers to show that all modules work correctly together.
"""

from lettuce import *

@step('I am on the (\d+)')
def homepage(step, ):
    world.number = int(number)
