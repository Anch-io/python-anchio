# UserLicenseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**user** | **str** |  | [optional] 
**company** | **str** |  | 
**handle** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**email** | **str** |  | 
**onboarding_complete** | **bool** |  | [optional] [default to False]
**roles** | **List[str]** |  | 
**permissions** | [**List[PermissionEnum]**](PermissionEnum.md) |  | 

## Example

```python
from anchio.models.user_license_schema import UserLicenseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserLicenseSchema from a JSON string
user_license_schema_instance = UserLicenseSchema.from_json(json)
# print the JSON string representation of the object
print UserLicenseSchema.to_json()

# convert the object into a dict
user_license_schema_dict = user_license_schema_instance.to_dict()
# create an instance of UserLicenseSchema from a dict
user_license_schema_form_dict = user_license_schema.from_dict(user_license_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


