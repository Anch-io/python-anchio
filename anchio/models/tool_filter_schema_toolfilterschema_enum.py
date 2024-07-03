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


class ToolFilterSchemaToolfilterschemaEnum(str, Enum):
    """
    ToolFilterSchemaToolfilterschemaEnum
    """

    """
    allowed enum values
    """
    EMPTY = ''
    NAME = 'name'
    MINUS_NAME = '-name'
    CATEGORY = 'category'
    MINUS_CATEGORY = '-category'
    CREATED_ON = 'created_on'
    MINUS_CREATED_ON = '-created_on'
    UPDATED_ON = 'updated_on'
    MINUS_UPDATED_ON = '-updated_on'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ToolFilterSchemaToolfilterschemaEnum from a JSON string"""
        return cls(json.loads(json_str))


