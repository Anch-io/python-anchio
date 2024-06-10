# ToolAccessUpdateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**role** | **str** |  | 
**access_start** | **str** |  | 
**access_end** | **str** |  | [optional] 
**justification** | **str** |  | 
**notes** | **str** |  | 
**status** | [**ToolAccessStatusEnum**](ToolAccessStatusEnum.md) |  | 

## Example

```python
from anchio.models.tool_access_update_schema import ToolAccessUpdateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAccessUpdateSchema from a JSON string
tool_access_update_schema_instance = ToolAccessUpdateSchema.from_json(json)
# print the JSON string representation of the object
print ToolAccessUpdateSchema.to_json()

# convert the object into a dict
tool_access_update_schema_dict = tool_access_update_schema_instance.to_dict()
# create an instance of ToolAccessUpdateSchema from a dict
tool_access_update_schema_form_dict = tool_access_update_schema.from_dict(tool_access_update_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


