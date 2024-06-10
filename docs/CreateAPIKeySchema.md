# CreateAPIKeySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**provider** | [**APIKeyProvider**](APIKeyProvider.md) |  | 
**key** | **str** |  | 

## Example

```python
from anchio.models.create_api_key_schema import CreateAPIKeySchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPIKeySchema from a JSON string
create_api_key_schema_instance = CreateAPIKeySchema.from_json(json)
# print the JSON string representation of the object
print CreateAPIKeySchema.to_json()

# convert the object into a dict
create_api_key_schema_dict = create_api_key_schema_instance.to_dict()
# create an instance of CreateAPIKeySchema from a dict
create_api_key_schema_form_dict = create_api_key_schema.from_dict(create_api_key_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


