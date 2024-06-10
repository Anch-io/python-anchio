# DefaultSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from anchio.models.default_schema import DefaultSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultSchema from a JSON string
default_schema_instance = DefaultSchema.from_json(json)
# print the JSON string representation of the object
print DefaultSchema.to_json()

# convert the object into a dict
default_schema_dict = default_schema_instance.to_dict()
# create an instance of DefaultSchema from a dict
default_schema_form_dict = default_schema.from_dict(default_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


