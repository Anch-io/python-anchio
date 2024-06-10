# SignIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**redirect_uri** | **str** |  | 
**scope** | **str** |  | 
**grant_type** | **str** |  | 

## Example

```python
from anchio.models.sign_in import SignIn

# TODO update the JSON string below
json = "{}"
# create an instance of SignIn from a JSON string
sign_in_instance = SignIn.from_json(json)
# print the JSON string representation of the object
print SignIn.to_json()

# convert the object into a dict
sign_in_dict = sign_in_instance.to_dict()
# create an instance of SignIn from a dict
sign_in_form_dict = sign_in.from_dict(sign_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


