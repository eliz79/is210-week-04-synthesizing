#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A ternary expression"""

ALARM = True

DAY = raw_input('Please enter day in CAPS? ')
TIME_PLS = int(raw_input('Please enter time in military time? '))
HOUR = 0600
BEEP = 'Beep! ' * 5
GOODBYE = ' '
SNOOZE = BEEP if TIME_PLS < HOUR else GOODBYE
print SNOOZE
