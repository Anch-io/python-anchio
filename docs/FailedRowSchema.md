# FailedRowSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** |  | 
**column** | **str** |  | [optional] [default to '']
**error** | **str** |  | [optional] [default to '']

## Example

```python
from anchio.models.failed_row_schema import FailedRowSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FailedRowSchema from a JSON string
failed_row_schema_instance = FailedRowSchema.from_json(json)
# print the JSON string representation of the object
print FailedRowSchema.to_json()

# convert the object into a dict
failed_row_schema_dict = failed_row_schema_instance.to_dict()
# create an instance of FailedRowSchema from a dict
failed_row_schema_form_dict = failed_row_schema.from_dict(failed_row_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


