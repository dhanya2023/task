#!/usr/bin/env python
# coding: utf-8


import unittest
import pep8


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['detail.py', 'detailVol.py','detailTem.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")