# PublicToolSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**name** | **str** | name | 
**description** | **str** | description | 
**logo** | **str** |  | [optional] 

## Example

```python
from anchio.models.public_tool_schema import PublicToolSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PublicToolSchema from a JSON string
public_tool_schema_instance = PublicToolSchema.from_json(json)
# print the JSON string representation of the object
print PublicToolSchema.to_json()

# convert the object into a dict
public_tool_schema_dict = public_tool_schema_instance.to_dict()
# create an instance of PublicToolSchema from a dict
public_tool_schema_form_dict = public_tool_schema.from_dict(public_tool_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


