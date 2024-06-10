# UpdateContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**department_ids** | **List[str]** |  | 
**justification** | **str** |  | 
**start** | **str** |  | 
**end** | **str** |  | [optional] 
**signing_date** | **str** |  | [optional] 
**contract_amount** | **float** |  | [optional] [default to 0]
**payment_terms** | [**PaymentTermsEnum**](PaymentTermsEnum.md) |  | 
**payment_frequency** | [**PaymentFrequencyEnum**](PaymentFrequencyEnum.md) |  | 
**notes** | **str** |  | [optional] [default to '']
**agreement_link** | **str** |  | [optional] [default to '']
**contract_signer** | **str** |  | [optional] 
**renewal_policy** | [**RenewalPolicyEnum**](RenewalPolicyEnum.md) |  | 

## Example

```python
from anchio.models.update_contract_schema import UpdateContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateContractSchema from a JSON string
update_contract_schema_instance = UpdateContractSchema.from_json(json)
# print the JSON string representation of the object
print UpdateContractSchema.to_json()

# convert the object into a dict
update_contract_schema_dict = update_contract_schema_instance.to_dict()
# create an instance of UpdateContractSchema from a dict
update_contract_schema_form_dict = update_contract_schema.from_dict(update_contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


