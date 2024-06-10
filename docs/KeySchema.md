# KeySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**key** | **str** |  | [optional] 
**user_license** | **str** |  | 
**last_used** | **str** |  | [optional] 
**scopes** | [**List[ScopeEnum]**](ScopeEnum.md) |  | [optional] [default to []]

## Example

```python
from anchio.models.key_schema import KeySchema

# TODO update the JSON string below
json = "{}"
# create an instance of KeySchema from a JSON string
key_schema_instance = KeySchema.from_json(json)
# print the JSON string representation of the object
print KeySchema.to_json()

# convert the object into a dict
key_schema_dict = key_schema_instance.to_dict()
# create an instance of KeySchema from a dict
key_schema_form_dict = key_schema.from_dict(key_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


