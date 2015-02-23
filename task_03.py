#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring"""


NAME = raw_input('What is your name? ')
PRIN_BORROW = int(raw_input('How much you borrowing? '))
LOAN_YRS = int(raw_input('How many yrs? '))
P_QUALIFIED = raw_input('Are you pre-qualified? Y/N ')
TOTAL = (PRIN_BORROW / LOAN_YRS)

print TOTAL
