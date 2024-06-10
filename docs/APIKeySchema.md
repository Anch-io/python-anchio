# APIKeySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**key** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**provider** | [**APIKeyProvider**](APIKeyProvider.md) |  | 

## Example

```python
from anchio.models.api_key_schema import APIKeySchema

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeySchema from a JSON string
api_key_schema_instance = APIKeySchema.from_json(json)
# print the JSON string representation of the object
print APIKeySchema.to_json()

# convert the object into a dict
api_key_schema_dict = api_key_schema_instance.to_dict()
# create an instance of APIKeySchema from a dict
api_key_schema_form_dict = api_key_schema.from_dict(api_key_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


