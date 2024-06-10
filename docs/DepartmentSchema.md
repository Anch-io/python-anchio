# DepartmentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from anchio.models.department_schema import DepartmentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentSchema from a JSON string
department_schema_instance = DepartmentSchema.from_json(json)
# print the JSON string representation of the object
print DepartmentSchema.to_json()

# convert the object into a dict
department_schema_dict = department_schema_instance.to_dict()
# create an instance of DepartmentSchema from a dict
department_schema_form_dict = department_schema.from_dict(department_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


