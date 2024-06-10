# LimitOffsetPageDepartmentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DepartmentSchema]**](DepartmentSchema.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from anchio.models.limit_offset_page_department_schema import LimitOffsetPageDepartmentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageDepartmentSchema from a JSON string
limit_offset_page_department_schema_instance = LimitOffsetPageDepartmentSchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageDepartmentSchema.to_json()

# convert the object into a dict
limit_offset_page_department_schema_dict = limit_offset_page_department_schema_instance.to_dict()
# create an instance of LimitOffsetPageDepartmentSchema from a dict
limit_offset_page_department_schema_form_dict = limit_offset_page_department_schema.from_dict(limit_offset_page_department_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


