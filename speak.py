# Authors: Michael Hawes, Gunther Cox, Kevin Brown, Tony Tran
# 21 Jabuary 2017
# Coconut Karaoke

from subprocess import call

def say(lyrics):
    """
    Speaks the ending result to the user
    """
    call(["espeak", "-v", "mb-us1", answer])
