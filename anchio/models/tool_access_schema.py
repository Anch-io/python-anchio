# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.2
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from anchio.models.employee_schema import EmployeeSchema
from anchio.models.tool_access_status_enum import ToolAccessStatusEnum
from anchio.models.tool_schema import ToolSchema
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ToolAccessSchema(BaseModel):
    """
    ToolAccessSchema
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id")
    created_on: Optional[datetime] = Field(default=None, description="created_on")
    updated_on: Optional[datetime] = Field(default=None, description="updated_on")
    tool: ToolSchema
    employee: EmployeeSchema
    role: StrictStr
    access_start: StrictStr
    access_end: Optional[StrictStr] = None
    justification: StrictStr
    notes: StrictStr
    status: ToolAccessStatusEnum
    __properties: ClassVar[List[str]] = ["id", "created_on", "updated_on", "tool", "employee", "role", "access_start", "access_end", "justification", "notes", "status"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ToolAccessSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tool
        if self.tool:
            _dict['tool'] = self.tool.to_dict()
        # override the default output from pydantic by calling `to_dict()` of employee
        if self.employee:
            _dict['employee'] = self.employee.to_dict()
        # set to None if access_end (nullable) is None
        # and model_fields_set contains the field
        if self.access_end is None and "access_end" in self.model_fields_set:
            _dict['access_end'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ToolAccessSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "tool": ToolSchema.from_dict(obj.get("tool")) if obj.get("tool") is not None else None,
            "employee": EmployeeSchema.from_dict(obj.get("employee")) if obj.get("employee") is not None else None,
            "role": obj.get("role"),
            "access_start": obj.get("access_start"),
            "access_end": obj.get("access_end"),
            "justification": obj.get("justification"),
            "notes": obj.get("notes"),
            "status": obj.get("status")
        })
        return _obj


