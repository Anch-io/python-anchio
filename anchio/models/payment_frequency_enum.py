# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.9
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PaymentFrequencyEnum(int, Enum):
    """
    PaymentFrequencyEnum
    """

    """
    allowed enum values
    """
    NUMBER_12 = 12
    NUMBER_3 = 3
    NUMBER_6 = 6
    NUMBER_1 = 1

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentFrequencyEnum from a JSON string"""
        return cls(json.loads(json_str))


