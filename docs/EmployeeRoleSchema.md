# EmployeeRoleSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**company** | **str** |  | 
**tools** | **List[str]** |  | [optional] [default to []]
**sync_employee** | **str** |  | [optional] 
**notification_channels** | **List[str]** |  | [optional] [default to []]

## Example

```python
from anchio.models.employee_role_schema import EmployeeRoleSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeRoleSchema from a JSON string
employee_role_schema_instance = EmployeeRoleSchema.from_json(json)
# print the JSON string representation of the object
print EmployeeRoleSchema.to_json()

# convert the object into a dict
employee_role_schema_dict = employee_role_schema_instance.to_dict()
# create an instance of EmployeeRoleSchema from a dict
employee_role_schema_form_dict = employee_role_schema.from_dict(employee_role_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


