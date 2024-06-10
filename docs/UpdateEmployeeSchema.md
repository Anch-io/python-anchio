# UpdateEmployeeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**employment_status** | [**EmploymentStatusEnum**](EmploymentStatusEnum.md) |  | 
**employment_type** | [**EmploymentTypeEnum**](EmploymentTypeEnum.md) |  | 
**department_ids** | **List[str]** |  | [optional] [default to []]
**employment_start** | **str** |  | 
**employment_end** | **str** |  | [optional] 
**title** | **str** |  | 

## Example

```python
from anchio.models.update_employee_schema import UpdateEmployeeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmployeeSchema from a JSON string
update_employee_schema_instance = UpdateEmployeeSchema.from_json(json)
# print the JSON string representation of the object
print UpdateEmployeeSchema.to_json()

# convert the object into a dict
update_employee_schema_dict = update_employee_schema_instance.to_dict()
# create an instance of UpdateEmployeeSchema from a dict
update_employee_schema_form_dict = update_employee_schema.from_dict(update_employee_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


