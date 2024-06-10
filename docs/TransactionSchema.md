# TransactionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**provider** | [**BankAccountProvider**](BankAccountProvider.md) |  | 
**account** | **str** |  | 
**amount** | **float** |  | 
**currency** | **str** |  | 
**check_number** | **str** |  | 
**transaction_date** | **str** |  | 
**authorization_date** | **str** |  | 
**merchant_name** | **str** |  | 
**tool** | **str** |  | 
**remote_transaction_id** | **str** |  | 
**transaction_type** | **str** |  | 
**payment_meta** | **object** |  | 
**pending** | **bool** |  | 

## Example

```python
from anchio.models.transaction_schema import TransactionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSchema from a JSON string
transaction_schema_instance = TransactionSchema.from_json(json)
# print the JSON string representation of the object
print TransactionSchema.to_json()

# convert the object into a dict
transaction_schema_dict = transaction_schema_instance.to_dict()
# create an instance of TransactionSchema from a dict
transaction_schema_form_dict = transaction_schema.from_dict(transaction_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


