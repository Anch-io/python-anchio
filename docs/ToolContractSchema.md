# ToolContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**created_on** | **datetime** | created_on | [optional] 
**updated_on** | **datetime** | updated_on | [optional] 
**user_count** | **int** |  | [optional] 
**name** | **str** | name | 
**description** | **str** | description | 
**logo** | **str** | logo | 
**category** | [**ToolCategorySchema**](ToolCategorySchema.md) |  | [optional] 
**country** | **str** |  | 
**has_subprocessor** | **bool** |  | [optional] [default to False]
**hidden_date** | **datetime** |  | [optional] 
**tags** | **List[str]** |  | [optional] [default to []]
**seat_limit** | **int** |  | [optional] 
**tool_id** | **str** |  | 
**contract_id** | **str** |  | 

## Example

```python
from anchio.models.tool_contract_schema import ToolContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ToolContractSchema from a JSON string
tool_contract_schema_instance = ToolContractSchema.from_json(json)
# print the JSON string representation of the object
print ToolContractSchema.to_json()

# convert the object into a dict
tool_contract_schema_dict = tool_contract_schema_instance.to_dict()
# create an instance of ToolContractSchema from a dict
tool_contract_schema_form_dict = tool_contract_schema.from_dict(tool_contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


