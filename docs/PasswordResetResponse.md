# PasswordResetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from anchio.models.password_reset_response import PasswordResetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordResetResponse from a JSON string
password_reset_response_instance = PasswordResetResponse.from_json(json)
# print the JSON string representation of the object
print PasswordResetResponse.to_json()

# convert the object into a dict
password_reset_response_dict = password_reset_response_instance.to_dict()
# create an instance of PasswordResetResponse from a dict
password_reset_response_form_dict = password_reset_response.from_dict(password_reset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


