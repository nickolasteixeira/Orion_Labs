# -*- coding: utf-8 -*-

import unittest

from .. import Vator

class TestVator(unittest.TestCase):

    def test_floor_count(self):
        v = Vator(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], 3)
        self.assertEqual(10, v.floor_count())
