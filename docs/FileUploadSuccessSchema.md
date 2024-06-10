# FileUploadSuccessSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_accesses** | **int** |  | [optional] [default to 0]
**contracts** | **int** |  | [optional] [default to 0]
**contract_tools** | **int** |  | [optional] [default to 0]
**departments** | **int** |  | [optional] [default to 0]
**department_contracts** | **int** |  | [optional] [default to 0]
**department_memberships** | **int** |  | [optional] [default to 0]
**employees** | **int** |  | [optional] [default to 0]
**tools** | **int** |  | [optional] [default to 0]
**tool_categories** | **int** |  | [optional] [default to 0]
**failed_rows** | [**List[FailedRowSchema]**](FailedRowSchema.md) |  | 

## Example

```python
from anchio.models.file_upload_success_schema import FileUploadSuccessSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadSuccessSchema from a JSON string
file_upload_success_schema_instance = FileUploadSuccessSchema.from_json(json)
# print the JSON string representation of the object
print FileUploadSuccessSchema.to_json()

# convert the object into a dict
file_upload_success_schema_dict = file_upload_success_schema_instance.to_dict()
# create an instance of FileUploadSuccessSchema from a dict
file_upload_success_schema_form_dict = file_upload_success_schema.from_dict(file_upload_success_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


