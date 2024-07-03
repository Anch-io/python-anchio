# APIKeyContextInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_password** | [**OnePasswordContext**](OnePasswordContext.md) |  | [optional] 

## Example

```python
from anchio.models.api_key_context_input import APIKeyContextInput

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyContextInput from a JSON string
api_key_context_input_instance = APIKeyContextInput.from_json(json)
# print the JSON string representation of the object
print APIKeyContextInput.to_json()

# convert the object into a dict
api_key_context_input_dict = api_key_context_input_instance.to_dict()
# create an instance of APIKeyContextInput from a dict
api_key_context_input_form_dict = api_key_context_input.from_dict(api_key_context_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


