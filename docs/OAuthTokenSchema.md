# OAuthTokenSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | 
**access_token** | **str** |  | 
**id_token** | **str** |  | 
**expires_in** | **int** |  | 
**not_before_policy** | **int** |  | 
**refresh_expires_in** | **int** |  | 
**session_state** | **str** |  | 

## Example

```python
from anchio.models.o_auth_token_schema import OAuthTokenSchema

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenSchema from a JSON string
o_auth_token_schema_instance = OAuthTokenSchema.from_json(json)
# print the JSON string representation of the object
print OAuthTokenSchema.to_json()

# convert the object into a dict
o_auth_token_schema_dict = o_auth_token_schema_instance.to_dict()
# create an instance of OAuthTokenSchema from a dict
o_auth_token_schema_form_dict = o_auth_token_schema.from_dict(o_auth_token_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


