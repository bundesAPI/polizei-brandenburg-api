"""
    Polizei Brandenburg API

    Nachrichten, Hochwasser-, Verkehrs- und Waldbrandwarnungen der Polizei Brandenburg  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.polizei_brandenburg.model.verkehr_data_inner import VerkehrDataInner

from deutschland import polizei_brandenburg

globals()["VerkehrDataInner"] = VerkehrDataInner
from deutschland.polizei_brandenburg.model.verkehr import Verkehr


class TestVerkehr(unittest.TestCase):
    """Verkehr unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVerkehr(self):
        """Test Verkehr"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Verkehr()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
