# ContractSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**department_ids** | **List[str]** |  | 
**contract_tools** | [**List[ToolContractSchema]**](ToolContractSchema.md) |  | 
**name** | **str** | name | [optional] 
**start** | **str** |  | 
**end** | **str** |  | [optional] 
**signing_date** | **str** |  | [optional] 
**contract_amount** | **float** |  | [optional] [default to 0]
**payment_terms** | [**PaymentTermsEnum**](PaymentTermsEnum.md) |  | 
**payment_frequency** | [**PaymentFrequencyEnum**](PaymentFrequencyEnum.md) |  | 
**justification** | **str** |  | 
**notes** | **str** |  | [optional] [default to '']
**agreement_link** | **str** |  | [optional] [default to '']
**renewal_policy** | [**RenewalPolicyEnum**](RenewalPolicyEnum.md) |  | 
**contract_signer** | [**EmployeeSchemaOutput**](EmployeeSchemaOutput.md) |  | [optional] 
**user_count** | **int** |  | [optional] [default to 0]

## Example

```python
from anchio.models.contract_schema import ContractSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ContractSchema from a JSON string
contract_schema_instance = ContractSchema.from_json(json)
# print the JSON string representation of the object
print ContractSchema.to_json()

# convert the object into a dict
contract_schema_dict = contract_schema_instance.to_dict()
# create an instance of ContractSchema from a dict
contract_schema_form_dict = contract_schema.from_dict(contract_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


