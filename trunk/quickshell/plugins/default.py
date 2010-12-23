#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery, UbiCast

import socket

default_network = 'eth1'
commands = (
    {'title': 'System Monitoring', 'category': True},
    {'title': 'cpu & mem usage (htop)', 'cmd': 'htop', 'key': 'h'},
    {'title': 'disk activity usage (iotop)', 'cmd': 'iotop', 'key': 'i'},
    {'title': 'network usage (nettop)', 'cmd': 'sudo jnettop -i %s' %default_network, 'key': 'n'},
    {'title': 'network sniffing (tcpdump)', 'cmd': 'sudo tcpdump not host %s -i %s -vvv -A' %(socket.gethostname(),default_network)},
    {'title': 'Log viewing', 'category': True},
    {'title': '/var/log/messages', 'cmd': 'sudo tail -f /var/log/messages', 'key': 'm'},
    {'title': '/var/log/auth', 'cmd': 'sudo tail -f /var/log/auth', 'key': 'a'},
)
