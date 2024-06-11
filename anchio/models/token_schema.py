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
from anchio.models.o_auth2_integration import OAuth2Integration
from anchio.models.token_schema_token_type_enum import TokenSchemaTokenTypeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TokenSchema(BaseModel):
    """
    TokenSchema
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id")
    created_on: Optional[datetime] = Field(default=None, description="created_on")
    updated_on: Optional[datetime] = Field(default=None, description="updated_on")
    scope: StrictStr = Field(description="scope")
    token_type: TokenSchemaTokenTypeEnum
    expires_in: datetime = Field(description="expires_in")
    date_invalidated: Optional[datetime] = None
    provider: OAuth2Integration
    __properties: ClassVar[List[str]] = ["id", "created_on", "updated_on", "scope", "token_type", "expires_in", "date_invalidated", "provider"]

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
        """Create an instance of TokenSchema from a JSON string"""
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
        # set to None if date_invalidated (nullable) is None
        # and model_fields_set contains the field
        if self.date_invalidated is None and "date_invalidated" in self.model_fields_set:
            _dict['date_invalidated'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TokenSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on"),
            "scope": obj.get("scope"),
            "token_type": obj.get("token_type"),
            "expires_in": obj.get("expires_in"),
            "date_invalidated": obj.get("date_invalidated"),
            "provider": obj.get("provider")
        })
        return _obj


