from __future__ import absolute_import

from unittest import TestCase
import tests.util as util

class TestGetDataLocation(TestCase):
    def test_get_data_lcation_for_testing(self):
        parent=util.get_data_lcation_for_testing()
