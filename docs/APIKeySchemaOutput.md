# APIKeySchemaOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**provider** | [**APIKeyProvider**](APIKeyProvider.md) |  | 
**key** | **str** |  | 
**context** | [**APIKeyContextOutput**](APIKeyContextOutput.md) |  | 

## Example

```python
from anchio.models.api_key_schema_output import APIKeySchemaOutput

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeySchemaOutput from a JSON string
api_key_schema_output_instance = APIKeySchemaOutput.from_json(json)
# print the JSON string representation of the object
print APIKeySchemaOutput.to_json()

# convert the object into a dict
api_key_schema_output_dict = api_key_schema_output_instance.to_dict()
# create an instance of APIKeySchemaOutput from a dict
api_key_schema_output_form_dict = api_key_schema_output.from_dict(api_key_schema_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


