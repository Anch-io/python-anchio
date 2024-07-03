# ToolAccessRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**justification** | **str** |  | 
**tool** | **str** |  | 
**title** | **str** |  | 
**company_name** | **str** |  | 

## Example

```python
from anchio.models.tool_access_request_schema import ToolAccessRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAccessRequestSchema from a JSON string
tool_access_request_schema_instance = ToolAccessRequestSchema.from_json(json)
# print the JSON string representation of the object
print ToolAccessRequestSchema.to_json()

# convert the object into a dict
tool_access_request_schema_dict = tool_access_request_schema_instance.to_dict()
# create an instance of ToolAccessRequestSchema from a dict
tool_access_request_schema_form_dict = tool_access_request_schema.from_dict(tool_access_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


