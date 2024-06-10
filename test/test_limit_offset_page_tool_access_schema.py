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

from anchio.models.limit_offset_page_tool_access_schema import LimitOffsetPageToolAccessSchema

class TestLimitOffsetPageToolAccessSchema(unittest.TestCase):
    """LimitOffsetPageToolAccessSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitOffsetPageToolAccessSchema:
        """Test LimitOffsetPageToolAccessSchema
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitOffsetPageToolAccessSchema`
        """
        model = LimitOffsetPageToolAccessSchema()
        if include_optional:
            return LimitOffsetPageToolAccessSchema(
                items = [
                    anchio.models.tool_access_schema.ToolAccessSchema(
                        id = '', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        tool = anchio.models.tool_schema.ToolSchema(
                            id = '', 
                            created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user_count = 56, 
                            name = '', 
                            description = '', 
                            logo = '', 
                            category = anchio.models.tool_category_schema.ToolCategorySchema(
                                id = '', 
                                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', 
                                description = '', ), 
                            country = '', 
                            has_subprocessor = True, 
                            hidden_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            tags = [
                                ''
                                ], ), 
                        employee = anchio.models.employee_schema.EmployeeSchema(
                            id = '', 
                            created_on = '', 
                            updated_on = '', 
                            first_name = '', 
                            last_name = '', 
                            title = '', 
                            email = '', 
                            company = anchio.models.company_schema.CompanySchema(
                                id = '', 
                                allowed_origins = [
                                    ''
                                    ], 
                                has_customer = True, 
                                is_trial_active = True, 
                                is_subscription_active = True, 
                                employee_count = 56, 
                                name = '', 
                                handle = '', 
                                keycloak_group = '', 
                                description = '', 
                                logo = '', 
                                email = '', 
                                phone = '', 
                                address_1 = '', 
                                address_2 = '', 
                                city = '', 
                                state = '', 
                                country = '', 
                                postal_code = '', 
                                last_employee_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_find_employee_app_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                slug = '', ), 
                            employment_status = 'ACTIVE', 
                            employment_type = 'FULL_TIME', 
                            employment_start = '', 
                            employment_end = '', 
                            department_ids = [
                                ''
                                ], ), 
                        role = '', 
                        access_start = '', 
                        access_end = '', 
                        justification = '', 
                        notes = '', 
                        status = 'PENDING', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0
            )
        else:
            return LimitOffsetPageToolAccessSchema(
                items = [
                    anchio.models.tool_access_schema.ToolAccessSchema(
                        id = '', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        tool = anchio.models.tool_schema.ToolSchema(
                            id = '', 
                            created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user_count = 56, 
                            name = '', 
                            description = '', 
                            logo = '', 
                            category = anchio.models.tool_category_schema.ToolCategorySchema(
                                id = '', 
                                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', 
                                description = '', ), 
                            country = '', 
                            has_subprocessor = True, 
                            hidden_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            tags = [
                                ''
                                ], ), 
                        employee = anchio.models.employee_schema.EmployeeSchema(
                            id = '', 
                            created_on = '', 
                            updated_on = '', 
                            first_name = '', 
                            last_name = '', 
                            title = '', 
                            email = '', 
                            company = anchio.models.company_schema.CompanySchema(
                                id = '', 
                                allowed_origins = [
                                    ''
                                    ], 
                                has_customer = True, 
                                is_trial_active = True, 
                                is_subscription_active = True, 
                                employee_count = 56, 
                                name = '', 
                                handle = '', 
                                keycloak_group = '', 
                                description = '', 
                                logo = '', 
                                email = '', 
                                phone = '', 
                                address_1 = '', 
                                address_2 = '', 
                                city = '', 
                                state = '', 
                                country = '', 
                                postal_code = '', 
                                last_employee_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_find_employee_app_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                slug = '', ), 
                            employment_status = 'ACTIVE', 
                            employment_type = 'FULL_TIME', 
                            employment_start = '', 
                            employment_end = '', 
                            department_ids = [
                                ''
                                ], ), 
                        role = '', 
                        access_start = '', 
                        access_end = '', 
                        justification = '', 
                        notes = '', 
                        status = 'PENDING', )
                    ],
                total = 0.0,
                limit = 1.0,
                offset = 0.0,
        )
        """

    def testLimitOffsetPageToolAccessSchema(self):
        """Test LimitOffsetPageToolAccessSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
