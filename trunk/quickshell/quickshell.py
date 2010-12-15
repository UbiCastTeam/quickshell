#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery, UbiCast

import os, sys, socket
import urwid
from easycast_utils.patterns import DictList

#TODO: 

default_network = 'eth1'
debug = True
debug = False

commands = DictList((
    {'title': 'System Monitoring', 'category': True},
    {'title': 'cpu & mem usage (htop)', 'cmd': 'htop', 'key': 'h'},
    {'title': 'disk activity usage (iotop)', 'cmd': 'iotop', 'key': 'i'},
    {'title': 'network usage (nettop)', 'cmd': 'sudo jnettop -i %s' %default_network, 'key': 'n'},    
    {'title': 'network sniffing (tcpdump)', 'cmd': 'sudo tcpdump not host %s -i %s -vvv -A' %(socket.gethostname(),default_network)},    
    {'title': 'Log viewing', 'category': True},
    {'title': '/var/log/messages', 'cmd': 'sudo tail -f /var/log/messages', 'key': 'm'},
    {'title': '/var/log/auth', 'cmd': 'sudo tail -f /var/log/auth', 'key': 'a'},
    {'title': 'Quit', 'cb': sys.exit, 'category': True, 'key': 'q'},
           ))

palette = [('header', 'white', 'black'),
    ('reveal focus', 'black', 'dark cyan', 'standout'),]


class SimpleLauncher:
    '''
    Simple urwid-based command launcher for common admin operations
    To launch a command, use arrows + enter or the specified hotkey
    '''

    def __init__(self):
        self.build()

    def build(self):
        items = list()
        for item in commands:
            title = ''
            if not item.get('category', False):
                title += '  '
            if item.get('key', False):
                title += '[%s] - ' %item['key']
            title += item['title']
            items.append(urwid.Button(title, on_press=self.on_press, user_data=item))

        content = urwid.SimpleListWalker([urwid.AttrMap(w, None, 'reveal focus') for w in items])
        listbox = urwid.ListBox(content)
        self.header = show_key = urwid.Text("QuickSys command launcher", wrap='clip')
        head = urwid.AttrMap(show_key, 'header')
        self.top = urwid.Frame(listbox, head)

    def debug(self, text):
        self.header.set_text(text)

    def on_press(self, widget, user_data):
        if debug:
            self.debug('%s %s' %(widget, user_data))
        self.process_entry(user_data)

    def process_entry(self, entry):
        if entry.get('cmd', None):
            self.run_command(entry['cmd'])
        elif entry.get('cb', None):
            entry['cb']()

    def run_command(self, command):
        os.system('clear')
        os.system(command)

    def run(self):
        if debug:
            loop = urwid.MainLoop(self.top, palette, input_filter=self.show_all_input, unhandled_input=self.exit_on_cr)
        else:
            loop = urwid.MainLoop(self.top, palette, unhandled_input=self.exit_on_cr)
        loop.run()

    def show_all_input(self, input, raw):
        self.debug("Pressed: " + " ".join([
            unicode(i) for i in input]))
        return input

    def exit_on_cr(self, input):
        if input == 'q':
            raise urwid.ExitMainLoop()
        else:
            entry = commands.get_by_key(input)
            if entry is not None:
                self.process_entry(entry)


if __name__ == '__main__':
    l = SimpleLauncher()
    try:
        l.run()
    except Exception, e:
        l.debug('Error: %s' %e)
