# EmployeeRoleToolSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**employee_role** | **str** |  | 
**tool** | **str** |  | 
**accesses** | **List[str]** |  | [optional] [default to []]
**notes** | **str** |  | [optional] 

## Example

```python
from anchio.models.employee_role_tool_schema import EmployeeRoleToolSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeRoleToolSchema from a JSON string
employee_role_tool_schema_instance = EmployeeRoleToolSchema.from_json(json)
# print the JSON string representation of the object
print EmployeeRoleToolSchema.to_json()

# convert the object into a dict
employee_role_tool_schema_dict = employee_role_tool_schema_instance.to_dict()
# create an instance of EmployeeRoleToolSchema from a dict
employee_role_tool_schema_form_dict = employee_role_tool_schema.from_dict(employee_role_tool_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


