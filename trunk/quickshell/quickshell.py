#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery, UbiCast

import os, sys
import urwid

debug = True
debug = False

from plugin import get_commands
commands = get_commands()

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
        self.header = show_key = urwid.Text("QuickShell command launcher", wrap='clip')
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
            self.run_command('clear')
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
