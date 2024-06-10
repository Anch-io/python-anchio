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

from anchio.models.bank_account_schema import BankAccountSchema

class TestBankAccountSchema(unittest.TestCase):
    """BankAccountSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankAccountSchema:
        """Test BankAccountSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankAccountSchema`
        """
        model = BankAccountSchema()
        if include_optional:
            return BankAccountSchema(
                created_on = '',
                updated_on = '',
                id = '',
                provider = '',
                name = '',
                account_id = '',
                type = '',
                subtype = '',
                connected_tools = 56,
                last_sync_date = '',
                institution = '',
                logo = '',
                oauth_token = ''
            )
        else:
            return BankAccountSchema(
                id = '',
                provider = '',
                name = '',
                account_id = '',
                type = '',
                subtype = '',
                institution = '',
                logo = '',
        )
        """

    def testBankAccountSchema(self):
        """Test BankAccountSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
