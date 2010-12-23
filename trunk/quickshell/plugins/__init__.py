#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010, Florent Thiery, UbiCast

from plugin import scan_directory_for_plugins

__all__ = scan_directory_for_plugins(__path__[0])

