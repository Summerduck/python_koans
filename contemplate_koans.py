#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Acknowledgment:
#
# Python Koans is a port of Ruby Koans originally written by Jim Weirich
# and Joe O'brien of Edgecase. There are some differences and tweaks specific
# to the Python language, but a great deal of it has been copied wholesale.
# So thanks guys!
#

import sys
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    if sys.version_info < (3, 0):
        print(
            "\nThis is the Python 3 version of Python Koans, but you are "
            + "running it with Python 2!\n\n"
            "Did you accidentally use the wrong python script? \nTry:\n\n"
            + "    python3 contemplate_koans.py\n"
        )
    else:
        if sys.version_info < (3, 3):
            print(
                "\n"
                + "********************************************************\n"
                + "WARNING:\n"
                + "This version of Python Koans was designed for "
                + "Python 3.3 or greater.\n"
                + "Your version of Python is older, so you may run into "
                + "problems!\n\n"
                + "But lets see how far we get...\n"
                + "********************************************************\n"
            )

        from runner.mountain import Mountain

        load_dotenv()
        Mountain(os.getenv("USERNAME")).walk_the_path(sys.argv)
