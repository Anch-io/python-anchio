# EmployeeSchemaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**title** | **str** |  | [optional] 
**email** | **str** |  | 
**company** | [**CompanySchemaInput**](CompanySchemaInput.md) |  | 
**employment_status** | [**EmploymentStatusEnum**](EmploymentStatusEnum.md) |  | 
**employment_type** | [**EmploymentTypeEnum**](EmploymentTypeEnum.md) |  | 
**employment_start** | **str** |  | 
**employment_end** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] [default to []]
**department_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from anchio.models.employee_schema_input import EmployeeSchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeSchemaInput from a JSON string
employee_schema_input_instance = EmployeeSchemaInput.from_json(json)
# print the JSON string representation of the object
print EmployeeSchemaInput.to_json()

# convert the object into a dict
employee_schema_input_dict = employee_schema_input_instance.to_dict()
# create an instance of EmployeeSchemaInput from a dict
employee_schema_input_form_dict = employee_schema_input.from_dict(employee_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


