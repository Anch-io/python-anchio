# coding: utf-8

"""
    Anch.io

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Contact: opensource@anchio.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from anchio.models.employment_status_enum import EmploymentStatusEnum
from anchio.models.employment_type_enum import EmploymentTypeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateEmployeeSchema(BaseModel):
    """
    UpdateEmployeeSchema
    """ # noqa: E501
    id: StrictStr
    first_name: StrictStr
    last_name: StrictStr
    email: StrictStr
    employment_status: EmploymentStatusEnum
    employment_type: EmploymentTypeEnum
    department_ids: Optional[List[StrictStr]] = None
    employment_start: StrictStr
    employment_end: Optional[StrictStr] = None
    title: StrictStr
    __properties: ClassVar[List[str]] = ["id", "first_name", "last_name", "email", "employment_status", "employment_type", "department_ids", "employment_start", "employment_end", "title"]

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
        """Create an instance of UpdateEmployeeSchema from a JSON string"""
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
        # set to None if employment_end (nullable) is None
        # and model_fields_set contains the field
        if self.employment_end is None and "employment_end" in self.model_fields_set:
            _dict['employment_end'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateEmployeeSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "email": obj.get("email"),
            "employment_status": obj.get("employment_status"),
            "employment_type": obj.get("employment_type"),
            "department_ids": obj.get("department_ids"),
            "employment_start": obj.get("employment_start"),
            "employment_end": obj.get("employment_end"),
            "title": obj.get("title")
        })
        return _obj


