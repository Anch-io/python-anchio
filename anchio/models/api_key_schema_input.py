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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from anchio.models.api_key_context_input import APIKeyContextInput
from anchio.models.api_key_provider import APIKeyProvider
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class APIKeySchemaInput(BaseModel):
    """
    APIKeySchemaInput
    """ # noqa: E501
    created_on: Optional[StrictStr] = None
    updated_on: Optional[StrictStr] = None
    id: StrictStr
    enabled: Optional[StrictBool] = True
    provider: APIKeyProvider
    key: StrictStr
    context: APIKeyContextInput
    __properties: ClassVar[List[str]] = ["created_on", "updated_on", "id", "enabled", "provider", "key", "context"]

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
        """Create an instance of APIKeySchemaInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # set to None if created_on (nullable) is None
        # and model_fields_set contains the field
        if self.created_on is None and "created_on" in self.model_fields_set:
            _dict['created_on'] = None

        # set to None if updated_on (nullable) is None
        # and model_fields_set contains the field
        if self.updated_on is None and "updated_on" in self.model_fields_set:
            _dict['updated_on'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of APIKeySchemaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "id": obj.get("id"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "provider": obj.get("provider"),
            "key": obj.get("key"),
            "context": APIKeyContextInput.from_dict(obj.get("context")) if obj.get("context") is not None else None
        })
        return _obj

