# PublicToolAccessSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**tool** | **str** | id | 

## Example

```python
from anchio.models.public_tool_access_schema import PublicToolAccessSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PublicToolAccessSchema from a JSON string
public_tool_access_schema_instance = PublicToolAccessSchema.from_json(json)
# print the JSON string representation of the object
print PublicToolAccessSchema.to_json()

# convert the object into a dict
public_tool_access_schema_dict = public_tool_access_schema_instance.to_dict()
# create an instance of PublicToolAccessSchema from a dict
public_tool_access_schema_form_dict = public_tool_access_schema.from_dict(public_tool_access_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


