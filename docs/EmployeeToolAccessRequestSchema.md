# EmployeeToolAccessRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | **str** |  | 
**tool** | **str** |  | 

## Example

```python
from anchio.models.employee_tool_access_request_schema import EmployeeToolAccessRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeToolAccessRequestSchema from a JSON string
employee_tool_access_request_schema_instance = EmployeeToolAccessRequestSchema.from_json(json)
# print the JSON string representation of the object
print EmployeeToolAccessRequestSchema.to_json()

# convert the object into a dict
employee_tool_access_request_schema_dict = employee_tool_access_request_schema_instance.to_dict()
# create an instance of EmployeeToolAccessRequestSchema from a dict
employee_tool_access_request_schema_form_dict = employee_tool_access_request_schema.from_dict(employee_tool_access_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


