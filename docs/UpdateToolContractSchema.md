# UpdateToolContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seat_limit** | **int** |  | [optional] 
**tool_id** | **str** |  | 
**contract_id** | **str** |  | 

## Example

```python
from anchio.models.update_tool_contract_schema import UpdateToolContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateToolContractSchema from a JSON string
update_tool_contract_schema_instance = UpdateToolContractSchema.from_json(json)
# print the JSON string representation of the object
print UpdateToolContractSchema.to_json()

# convert the object into a dict
update_tool_contract_schema_dict = update_tool_contract_schema_instance.to_dict()
# create an instance of UpdateToolContractSchema from a dict
update_tool_contract_schema_form_dict = update_tool_contract_schema.from_dict(update_tool_contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


