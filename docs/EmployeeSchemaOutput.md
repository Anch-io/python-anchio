# EmployeeSchemaOutput


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
**company** | [**CompanySchemaOutput**](CompanySchemaOutput.md) |  | 
**employment_status** | [**EmploymentStatusEnum**](EmploymentStatusEnum.md) |  | 
**employment_type** | [**EmploymentTypeEnum**](EmploymentTypeEnum.md) |  | 
**employment_start** | **str** |  | 
**employment_end** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] [default to []]
**department_ids** | **List[str]** |  | [optional] [default to []]

## Example

```python
from anchio.models.employee_schema_output import EmployeeSchemaOutput

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeSchemaOutput from a JSON string
employee_schema_output_instance = EmployeeSchemaOutput.from_json(json)
# print the JSON string representation of the object
print EmployeeSchemaOutput.to_json()

# convert the object into a dict
employee_schema_output_dict = employee_schema_output_instance.to_dict()
# create an instance of EmployeeSchemaOutput from a dict
employee_schema_output_form_dict = employee_schema_output.from_dict(employee_schema_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


