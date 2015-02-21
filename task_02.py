#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A ternary expression"""

ALARM = True

DAY = raw_input('Please enter day in CAPS? ').upper()

TIME_PLS = int(raw_input('Please enter time in military time? '))
BEEP = 'Beep! ' * 5
#SNOOZE = BEEP if ALARM > int(600) else '{}'.format(BEEP)

if ALARM > 600:
    print ' '
    
else:
    print BEEP.format(BEEP)

