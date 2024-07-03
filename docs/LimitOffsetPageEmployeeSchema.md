# LimitOffsetPageEmployeeSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmployeeSchemaOutput]**](EmployeeSchemaOutput.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from anchio.models.limit_offset_page_employee_schema import LimitOffsetPageEmployeeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageEmployeeSchema from a JSON string
limit_offset_page_employee_schema_instance = LimitOffsetPageEmployeeSchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageEmployeeSchema.to_json()

# convert the object into a dict
limit_offset_page_employee_schema_dict = limit_offset_page_employee_schema_instance.to_dict()
# create an instance of LimitOffsetPageEmployeeSchema from a dict
limit_offset_page_employee_schema_form_dict = limit_offset_page_employee_schema.from_dict(limit_offset_page_employee_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


