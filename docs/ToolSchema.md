# ToolSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**user_count** | **int** |  | [optional] 
**name** | **str** | name | 
**description** | **str** | description | 
**logo** | **str** |  | [optional] 
**category** | [**ToolCategorySchema**](ToolCategorySchema.md) |  | [optional] 
**country** | **str** |  | 
**has_subprocessor** | **bool** |  | [optional] [default to False]
**hidden_date** | **datetime** |  | [optional] 
**tags** | **List[str]** |  | [optional] [default to []]

## Example

```python
from anchio.models.tool_schema import ToolSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolSchema from a JSON string
tool_schema_instance = ToolSchema.from_json(json)
# print the JSON string representation of the object
print ToolSchema.to_json()

# convert the object into a dict
tool_schema_dict = tool_schema_instance.to_dict()
# create an instance of ToolSchema from a dict
tool_schema_form_dict = tool_schema.from_dict(tool_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


