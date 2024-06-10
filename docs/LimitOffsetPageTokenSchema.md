# LimitOffsetPageTokenSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TokenSchema]**](TokenSchema.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from anchio.models.limit_offset_page_token_schema import LimitOffsetPageTokenSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageTokenSchema from a JSON string
limit_offset_page_token_schema_instance = LimitOffsetPageTokenSchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageTokenSchema.to_json()

# convert the object into a dict
limit_offset_page_token_schema_dict = limit_offset_page_token_schema_instance.to_dict()
# create an instance of LimitOffsetPageTokenSchema from a dict
limit_offset_page_token_schema_form_dict = limit_offset_page_token_schema.from_dict(limit_offset_page_token_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


