# CompanySchema


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
**last_employee_sync** | **datetime** |  | [optional] 
**last_find_employee_app_sync** | **datetime** |  | [optional] 
**slug** | **str** | slug | [optional] 

## Example

```python
from anchio.models.company_schema import CompanySchema

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySchema from a JSON string
company_schema_instance = CompanySchema.from_json(json)
# print the JSON string representation of the object
print CompanySchema.to_json()

# convert the object into a dict
company_schema_dict = company_schema_instance.to_dict()
# create an instance of CompanySchema from a dict
company_schema_form_dict = company_schema.from_dict(company_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


