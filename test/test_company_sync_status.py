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

from anchio.models.company_sync_status import CompanySyncStatus

class TestCompanySyncStatus(unittest.TestCase):
    """CompanySyncStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanySyncStatus:
        """Test CompanySyncStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanySyncStatus`
        """
        model = CompanySyncStatus()
        if include_optional:
            return CompanySyncStatus(
                employee_sync = anchio.models.sync_status.SyncStatus(
                    last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_message = '', ),
                find_employee_app_sync = anchio.models.sync_status.SyncStatus(
                    last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_message = '', ),
                activity_sync = anchio.models.sync_status.SyncStatus(
                    last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_message = '', ),
                plaid_sync = anchio.models.sync_status.SyncStatus(
                    last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_message = '', ),
                lang_smith_sync = anchio.models.sync_status.SyncStatus(
                    last_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_sync = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    error_message = '', )
            )
        else:
            return CompanySyncStatus(
        )
        """

    def testCompanySyncStatus(self):
        """Test CompanySyncStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
