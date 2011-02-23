#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from distutils.core import setup
from quickshell import VERSION

if 'install' in sys.argv:
    install_scripts = False
    for arg in sys.argv:
        if arg.startswith('--install-scripts'):
            install_scripts = True
            break
    if not install_scripts:
        sys.argv.append('--install-scripts=/usr/local/bin')

setup(
    name="quickshell",
    version=VERSION,
    description="Simple urwid-based command launcher for common admin operations",
    author="Florent Thiery",
    author_email="fthiery@gmail.com",
    url="http://code.google.com/p/quickshell",
    license="LGPL",
    packages=['quickshell', 'quickshell/plugins'],
    scripts=['scripts/qs']
)

