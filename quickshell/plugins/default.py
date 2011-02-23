#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery 

import socket

log_viewing_template = 'sudo less +F %s'
default_network = 'eth0'

commands = (
    {'title': 'System Monitoring', 'category': True},
    {'title': 'cpu & mem usage (htop)', 'cmd': 'htop', 'key': 'h'},
    {'title': 'disk activity usage (iotop)', 'cmd': 'iotop', 'key': 'i'},
    {'title': 'disk space', 'cmd': 'watch "df -h"'},
    {'title': 'network usage (nettop)', 'cmd': 'sudo jnettop -i %s' %default_network, 'key': 'n'},
    {'title': 'network sniffing (tcpdump)', 'cmd': 'sudo tcpdump not host %s -i %s -vvv -A' %(socket.gethostname(),default_network)},
    {'title': 'Log viewing', 'category': True},
    {'title': '/var/log/messages', 'cmd': log_viewing_template %'/var/log/messages' , 'key': 'm'},
    {'title': '/var/log/auth', 'cmd': log_viewing_template %'/var/log/auth.log', 'key': 'a'},
)
