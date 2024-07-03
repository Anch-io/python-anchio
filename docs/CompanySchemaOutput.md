# CompanySchemaOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**allowed_origins** | **List[str]** |  | [optional] [default to []]
**has_customer** | **bool** |  | [optional] [default to False]
**is_trial_active** | **bool** |  | [optional] [default to False]
**is_subscription_active** | **bool** |  | [optional] [default to False]
**employee_count** | **int** |  | [optional] [default to 0]
**name** | **str** | name | 
**handle** | **str** | handle | 
**keycloak_group** | **str** |  | [optional] 
**description** | **str** | description | [optional] [default to '']
**logo** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**address_1** | **str** | address_1 | [optional] [default to '']
**address_2** | **str** | address_2 | [optional] [default to '']
**city** | **str** | city | [optional] [default to '']
**state** | **str** | state | [optional] [default to '']
**country** | **str** |  | 
**postal_code** | **str** | postal_code | [optional] [default to '']
**slug** | **str** | slug | [optional] 
**sync_status** | [**CompanySyncStatus**](CompanySyncStatus.md) |  | 
**allow_public_company_access_page** | **bool** |  | [optional] [default to False]

## Example

```python
from anchio.models.company_schema_output import CompanySchemaOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySchemaOutput from a JSON string
company_schema_output_instance = CompanySchemaOutput.from_json(json)
# print the JSON string representation of the object
print CompanySchemaOutput.to_json()

# convert the object into a dict
company_schema_output_dict = company_schema_output_instance.to_dict()
# create an instance of CompanySchemaOutput from a dict
company_schema_output_form_dict = company_schema_output.from_dict(company_schema_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


