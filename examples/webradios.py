#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery, UbiCast

gst_launch_template = 'gst-launch souphttpsrc location=%s ! queue2 ! mad ! autoaudiosink -m'

commands = (
    {'title': 'Webradios', 'category': True},
    {'title': 'Prun.net', 'cmd': gst_launch_template %'http://partage.legram.fr:8000/prun'},
)
