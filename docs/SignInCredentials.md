# SignInCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**scope** | **str** |  | 

## Example

```python
from anchio.models.sign_in_credentials import SignInCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SignInCredentials from a JSON string
sign_in_credentials_instance = SignInCredentials.from_json(json)
# print the JSON string representation of the object
print SignInCredentials.to_json()

# convert the object into a dict
sign_in_credentials_dict = sign_in_credentials_instance.to_dict()
# create an instance of SignInCredentials from a dict
sign_in_credentials_form_dict = sign_in_credentials.from_dict(sign_in_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


