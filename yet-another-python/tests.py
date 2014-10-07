#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
======================================================
Tests
======================================================
"""

import unittest
import string

lower_words_digits = string.lowercase + string.digits

from tasks import *

class TestMail(unittest.TestCase):

    def test_email_name_length(self):
        good_mail = 'n'*128 + '@domen.ru'
        self.assertTrue( email_checker(good_mail), msg='check: %s'%good_mail)

        bad_mail = 'n'*129 + '@domen.ru'
        self.assertFalse( email_checker(bad_mail), msg='check: %s'%bad_mail)


    def test_email_domen_length(self):
        good_mail = [
            'name@a.' + 'm'*254,
            'name@' + 'm'*254 + '.a'
            ]
        bad_mail = [
            'name@a.' + 'm'*255,
            'name@' + 'm'*255 + '.a'
            ]
        for mail in good_mail:
            self.assertTrue( email_checker(mail), msg='check: %s'%mail)

        for mail in bad_mail:
            self.assertFalse( email_checker(mail), msg='check: %s'%mail)

    def test_dots_in_mail_name(self):
        good_mail = 'n.ame@domen.ru'
        self.assertTrue( email_checker(good_mail), msg='check: %s'%good_mail)

        bad_mail = 'na..me@domen.ru'
        self.assertFalse( email_checker(bad_mail), msg='check: %s'%bad_mail)

    def test_quotes_in_mail_name(self):
        good_mail = 'first"and"second@domen.ru'
        self.assertTrue( email_checker(good_mail), msg='check: %s'%good_mail)

        bad_mail = 'n"am"e"@domen.ru'
        self.assertFalse( email_checker(bad_mail), msg='check: %s'%bad_mail)


    def test_emaeil_checker(self):
        
        bad_strings_domen = [
            '@domen.ru',
            'namedomen.ru',
            'name@tw',
            'name@a.' + 'b'*255,
            'name@Domen.Ru-'
            'name@do%men.ru-'
            'name@-domen.ru',
            'name@domen-.ru',
            'name@domen.-ru',
            'name@domen.ru-',
        ]

        bas_strings_name = [
            'n'*129 + '@a.' + 'm'*254,
            'name@domen..ru',
            '@domen.ru',
            'name"name@domen.ru',
            'na!me""name@domen.ru',
            'na"me""name@domen.ru',
            # 'name@domen.ru',
            # 'name@domen.ru',
        ]
        good_string_name = [
            lower_words_digits + '@domen.ru',
            'aaaaa"qqqqqq"aaaaa' + '@domen.ru',
            'aa"ab"ad"!!,:fd"aaaaa' + '@domen.ru',
        ]

        for good_mail in good_string_name:
            self.assertTrue( email_checker(good_mail),  msg='check: %s'%good_mail )            

        for bad_mail in bad_strings_domen + bas_strings_name:
            self.assertFalse( email_checker(bad_mail), msg='check: %s'%bad_mail )

if __name__ == "__main__":
    unittest.main()