# OnePasswordContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**OnePasswordDomain**](OnePasswordDomain.md) |  | 

## Example

```python
from anchio.models.one_password_context import OnePasswordContext

# TODO update the JSON string below
json = "{}"
# create an instance of OnePasswordContext from a JSON string
one_password_context_instance = OnePasswordContext.from_json(json)
# print the JSON string representation of the object
print OnePasswordContext.to_json()

# convert the object into a dict
one_password_context_dict = one_password_context_instance.to_dict()
# create an instance of OnePasswordContext from a dict
one_password_context_form_dict = one_password_context.from_dict(one_password_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


