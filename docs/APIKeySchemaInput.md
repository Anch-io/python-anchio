# APIKeySchemaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**provider** | [**APIKeyProvider**](APIKeyProvider.md) |  | 
**key** | **str** |  | 
**context** | [**APIKeyContextInput**](APIKeyContextInput.md) |  | 

## Example

```python
from anchio.models.api_key_schema_input import APIKeySchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeySchemaInput from a JSON string
api_key_schema_input_instance = APIKeySchemaInput.from_json(json)
# print the JSON string representation of the object
print APIKeySchemaInput.to_json()

# convert the object into a dict
api_key_schema_input_dict = api_key_schema_input_instance.to_dict()
# create an instance of APIKeySchemaInput from a dict
api_key_schema_input_form_dict = api_key_schema_input.from_dict(api_key_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


