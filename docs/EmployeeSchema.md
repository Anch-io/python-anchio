# EmployeeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**title** | **str** |  | 
**email** | **str** |  | 
**company** | [**CompanySchema**](CompanySchema.md) |  | 
**employment_status** | [**EmploymentStatusEnum**](EmploymentStatusEnum.md) |  | 
**employment_type** | [**EmploymentTypeEnum**](EmploymentTypeEnum.md) |  | 
**employment_start** | **str** |  | 
**employment_end** | **str** |  | [optional] 
**department_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from anchio.models.employee_schema import EmployeeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeSchema from a JSON string
employee_schema_instance = EmployeeSchema.from_json(json)
# print the JSON string representation of the object
print EmployeeSchema.to_json()

# convert the object into a dict
employee_schema_dict = employee_schema_instance.to_dict()
# create an instance of EmployeeSchema from a dict
employee_schema_form_dict = employee_schema.from_dict(employee_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


