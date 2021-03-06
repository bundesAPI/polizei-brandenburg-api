"""
    Polizei Brandenburg API

    Nachrichten, Hochwasser-, Verkehrs- und Waldbrandwarnungen der Polizei Brandenburg  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.polizei_brandenburg.api.default_api import DefaultApi  # noqa: E501

from deutschland import polizei_brandenburg


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_news_version1_get(self):
        """Test case for news_version1_get

        Nachrichten, Suchmeldungen der Polzei Brandenburg  # noqa: E501
        """
        pass

    def test_pegel_version1_get(self):
        """Test case for pegel_version1_get

        Pegelstände  # noqa: E501
        """
        pass

    def test_reviere_version1_get(self):
        """Test case for reviere_version1_get

        Liste aller Reviere der Polzei Brandenburg  # noqa: E501
        """
        pass

    def test_vwd_version1_get(self):
        """Test case for vwd_version1_get

        Verkehrswarnungen der Polzei Brandenburg  # noqa: E501
        """
        pass

    def test_waldbrand_version1_get(self):
        """Test case for waldbrand_version1_get

        Waldbrandwarnungen Brandenburg  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
