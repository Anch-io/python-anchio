# BankAccountSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**provider** | **str** |  | 
**name** | **str** |  | 
**account_id** | **str** |  | 
**type** | **str** |  | 
**subtype** | **str** |  | 
**connected_tools** | **int** |  | [optional] [default to 0]
**last_sync_date** | **str** |  | [optional] 
**institution** | **str** |  | 
**logo** | **str** |  | [optional] 
**oauth_token** | **str** |  | [optional] 

## Example

```python
from anchio.models.bank_account_schema import BankAccountSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountSchema from a JSON string
bank_account_schema_instance = BankAccountSchema.from_json(json)
# print the JSON string representation of the object
print BankAccountSchema.to_json()

# convert the object into a dict
bank_account_schema_dict = bank_account_schema_instance.to_dict()
# create an instance of BankAccountSchema from a dict
bank_account_schema_form_dict = bank_account_schema.from_dict(bank_account_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


