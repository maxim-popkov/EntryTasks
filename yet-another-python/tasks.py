#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
======================================================
Qustions
======================================================
"""
import re

def question_two():
    """
    reference to inner array duplicated 3 times
    
    """
    # [[][][]]
    x = [[]]*3
    #[[a],[a],[a]]
    x[0].append('a')
    #[[a, b],[a, b],[a, b]]
    x[1].append('b')
    #[[a, b, c],[a, b, c],[a, b, c]]
    x[2].append('c')
    #[[d],[a, b, c],[a, b, c]]
    x[0] = ['d']

def email_checker(email):
    """
    Email Valdation
    """
    if not type(email) == str:
        return False

    splited_mail = email.split('@')
    if not len(splited_mail) == 2:
        return False
    
    name, domen = splited_mail
    len_name = len(name)
    len_domen = len(domen)
    if not ( 256 >= len_domen >= 3):
        return False

    if not ( 128 >= len_name > 0):
        return False

    domen_rule = ur'^([a-z0-9_][a-z0-9-_]*)\.([a-z0-9_][a-z0-9-_]*)$'
    matched = re.match(domen_rule, domen)
    if not matched:
        return False
    
    domen_second, domen_first = matched.groups()
    end_checker = lambda x_str: x_str.endswith('-')
    checked_with_dash = map(end_checker, [domen_first, domen_second])
    if any(checked_with_dash):
        return False

    good_name_symbols = '[a-z0-9"!,:\-_]'
    name_dots_rule = ur'^%s*\.\.%s*$'%(good_name_symbols, good_name_symbols)
    matched = re.match(name_dots_rule, name)
    if matched:
        return False

    splited_name = name.split('\"')
    if len(splited_name) % 2 == 0:
        return False

    rule = ur'^%s*$'%good_name_symbols
    for quoted in splited_name[1::2]:
        matched = re.match(rule, quoted)
        if matched: continue
        else: return False

    rule = ur'^[a-z0-9".\-_]*$'
    for unquoted in splited_name[::2]:
        matched = re.match(rule, unquoted)
        if matched: continue
        else: return False
    
    return True