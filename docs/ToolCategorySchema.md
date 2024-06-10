# ToolCategorySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**name** | **str** | name | 
**description** | **str** | description | [optional] [default to '']

## Example

```python
from anchio.models.tool_category_schema import ToolCategorySchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCategorySchema from a JSON string
tool_category_schema_instance = ToolCategorySchema.from_json(json)
# print the JSON string representation of the object
print ToolCategorySchema.to_json()

# convert the object into a dict
tool_category_schema_dict = tool_category_schema_instance.to_dict()
# create an instance of ToolCategorySchema from a dict
tool_category_schema_form_dict = tool_category_schema.from_dict(tool_category_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


