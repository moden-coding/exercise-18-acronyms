#!/usr/bin/env python3
"""Tests for the Acronyms assignment."""

import unittest

from src.acronyms import acronyms


class TestAcronyms(unittest.TestCase):
    """acronyms(s) -> list of the acronym-like tokens found in s, in order."""

    def test_worked_example(self):
        text = (
            "For the purposes of the EU General Data Protection Regulation "
            "(GDPR), the controller of your personal information is "
            "International Business Machines Corporation (IBM Corp.), 1 New "
            "Orchard Road, Armonk, New York, United States, unless indicated "
            "otherwise. Where IBM Corp. or a subsidiary it controls (not "
            "established in the European Economic Area (EEA)) is required "
            "to appoint a legal representative in the EEA, the "
            "representative for all such cases is IBM United Kingdom "
            "Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, "
            "United Kingdom PO6 3AU."
        )
        result = acronyms(text)
        self.assertIsInstance(
            result,
            list,
            msg="acronyms should return a list. Got %s." % (type(result),),
        )
        self.assertEqual(
            result,
            ['EU', 'GDPR', 'IBM', 'IBM', 'EEA', 'EEA', 'IBM', 'PO', 'PO6',
             '3AU'],
            msg="acronyms(...) did not return the expected list of "
            "acronym-like tokens, in the order they appear in the text.",
        )

    def test_empty_string_gives_an_empty_list(self):
        result = acronyms("")
        self.assertIsInstance(
            result,
            list,
            msg="acronyms should return a list. Got %s." % (type(result),),
        )
        self.assertEqual(
            result,
            [],
            msg="Empty list expected for empty input string!",
        )

    def test_text_with_no_acronyms_gives_an_empty_list(self):
        result = acronyms("just some plain lowercase words here")
        self.assertEqual(
            result,
            [],
            msg="acronyms('just some plain lowercase words here') should be "
            "[]: no token is an all-caps acronym-like word.",
        )

    def test_a_single_acronym_is_found(self):
        result = acronyms("The FBI arrived at noon")
        self.assertEqual(
            result,
            ['FBI'],
            msg="acronyms('The FBI arrived at noon') should be ['FBI']: "
            "'The', 'arrived', 'at' and 'noon' are not acronyms, only 'FBI' "
            "is.",
        )


if __name__ == '__main__':
    unittest.main()
