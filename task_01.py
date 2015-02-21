#!usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a color comparison"""

BASE = raw_input('HChoose base: Seattle Grey or Manatee: ')
ACCENT = raw_input('''Choose accent: Ceramic Glaze, Culumbus Nimbus,
Platnium Mist, or Spartan Sage: ''')
HIGHLIGHT = raw_input('''Choose highlight: Bascally White, White, Off-White,
Paper White, Bone White, Just White, Fractal White, Not White: ''')

CHOICES = 'Base: {}, Accent: {}, Highlight: {}'
SELECTIONS = raw_input('Your selected choices are: ')

print SELECTIONS.format(BASE, ACCENT, HIGHLIGHT)
