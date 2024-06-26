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

from anchio.models.key_schema import KeySchema

class TestKeySchema(unittest.TestCase):
    """KeySchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeySchema:
        """Test KeySchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeySchema`
        """
        model = KeySchema()
        if include_optional:
            return KeySchema(
                created_on = '',
                updated_on = '',
                id = '',
                name = '',
                key = '',
                user_license = '',
                last_used = '',
                scopes = [
                    'admin'
                    ]
            )
        else:
            return KeySchema(
                id = '',
                name = '',
                user_license = '',
        )
        """

    def testKeySchema(self):
        """Test KeySchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
