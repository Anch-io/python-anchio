# UserSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created** | **bool** |  | [optional] [default to False]
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**keycloak_id** | **str** | keycloak_id | 
**keycloak_realm** | **str** | keycloak_realm | 
**is_active** | **bool** | is_active | [optional] [default to True]
**email_verified** | **bool** |  | 
**birthdate** | **str** |  | [optional] [default to '']
**roles** | **List[str]** |  | 

## Example

```python
from anchio.models.user_schema import UserSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchema from a JSON string
user_schema_instance = UserSchema.from_json(json)
# print the JSON string representation of the object
print UserSchema.to_json()

# convert the object into a dict
user_schema_dict = user_schema_instance.to_dict()
# create an instance of UserSchema from a dict
user_schema_form_dict = user_schema.from_dict(user_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


