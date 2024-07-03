# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.9
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from anchio.models.employee_role_tool_schema import EmployeeRoleToolSchema

class TestEmployeeRoleToolSchema(unittest.TestCase):
    """EmployeeRoleToolSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EmployeeRoleToolSchema:
        """Test EmployeeRoleToolSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EmployeeRoleToolSchema`
        """
        model = EmployeeRoleToolSchema()
        if include_optional:
            return EmployeeRoleToolSchema(
                created_on = '',
                updated_on = '',
                id = '',
                employee_role = '',
                tool = '',
                accesses = [
                    ''
                    ],
                notes = ''
            )
        else:
            return EmployeeRoleToolSchema(
                id = '',
                employee_role = '',
                tool = '',
        )
        """

    def testEmployeeRoleToolSchema(self):
        """Test EmployeeRoleToolSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
