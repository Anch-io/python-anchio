# LimitOffsetPageAPIKeySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[APIKeySchemaOutput]**](APIKeySchemaOutput.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from anchio.models.limit_offset_page_api_key_schema import LimitOffsetPageAPIKeySchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageAPIKeySchema from a JSON string
limit_offset_page_api_key_schema_instance = LimitOffsetPageAPIKeySchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageAPIKeySchema.to_json()

# convert the object into a dict
limit_offset_page_api_key_schema_dict = limit_offset_page_api_key_schema_instance.to_dict()
# create an instance of LimitOffsetPageAPIKeySchema from a dict
limit_offset_page_api_key_schema_form_dict = limit_offset_page_api_key_schema.from_dict(limit_offset_page_api_key_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


