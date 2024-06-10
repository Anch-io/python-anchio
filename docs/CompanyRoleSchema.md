# CompanyRoleSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] [default to '']

## Example

```python
from anchio.models.company_role_schema import CompanyRoleSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyRoleSchema from a JSON string
company_role_schema_instance = CompanyRoleSchema.from_json(json)
# print the JSON string representation of the object
print CompanyRoleSchema.to_json()

# convert the object into a dict
company_role_schema_dict = company_role_schema_instance.to_dict()
# create an instance of CompanyRoleSchema from a dict
company_role_schema_form_dict = company_role_schema.from_dict(company_role_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


