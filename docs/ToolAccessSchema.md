# ToolAccessSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**tool** | [**ToolSchema**](ToolSchema.md) |  | 
**employee** | [**EmployeeSchemaOutput**](EmployeeSchemaOutput.md) |  | 
**role** | [**ToolAccessSchemaRoleEnum**](ToolAccessSchemaRoleEnum.md) |  | [optional] 
**access_start** | **str** |  | 
**access_end** | **str** |  | [optional] 
**justification** | **str** |  | 
**notes** | **str** |  | 
**status** | [**ToolAccessStatusEnum**](ToolAccessStatusEnum.md) |  | 

## Example

```python
from anchio.models.tool_access_schema import ToolAccessSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAccessSchema from a JSON string
tool_access_schema_instance = ToolAccessSchema.from_json(json)
# print the JSON string representation of the object
print ToolAccessSchema.to_json()

# convert the object into a dict
tool_access_schema_dict = tool_access_schema_instance.to_dict()
# create an instance of ToolAccessSchema from a dict
tool_access_schema_form_dict = tool_access_schema.from_dict(tool_access_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


