# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from anchio.models.default_schema import DefaultSchema

class TestDefaultSchema(unittest.TestCase):
    """DefaultSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DefaultSchema:
        """Test DefaultSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DefaultSchema`
        """
        model = DefaultSchema()
        if include_optional:
            return DefaultSchema(
                detail = '',
                code = ''
            )
        else:
            return DefaultSchema(
                detail = '',
                code = '',
        )
        """

    def testDefaultSchema(self):
        """Test DefaultSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
