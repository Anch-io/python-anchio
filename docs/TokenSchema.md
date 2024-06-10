# TokenSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**scope** | **str** | scope | 
**token_type** | [**TokenSchemaTokenTypeEnum**](TokenSchemaTokenTypeEnum.md) |  | 
**expires_in** | **datetime** | expires_in | 
**date_invalidated** | **datetime** |  | [optional] 
**provider** | [**OAuth2Integration**](OAuth2Integration.md) |  | 

## Example

```python
from anchio.models.token_schema import TokenSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TokenSchema from a JSON string
token_schema_instance = TokenSchema.from_json(json)
# print the JSON string representation of the object
print TokenSchema.to_json()

# convert the object into a dict
token_schema_dict = token_schema_instance.to_dict()
# create an instance of TokenSchema from a dict
token_schema_form_dict = token_schema.from_dict(token_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


