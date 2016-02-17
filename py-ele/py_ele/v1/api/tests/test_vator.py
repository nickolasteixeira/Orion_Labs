# -*- coding: utf-8 -*-

import unittest

from .. import Vator

class TestVator(unittest.TestCase):

    def test_floor_count(self):
        v = Vator()
        self.assertEqual(10, v.floor_count())
