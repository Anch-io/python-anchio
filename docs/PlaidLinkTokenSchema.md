# PlaidLinkTokenSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_token** | **str** |  | 

## Example

```python
from anchio.models.plaid_link_token_schema import PlaidLinkTokenSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PlaidLinkTokenSchema from a JSON string
plaid_link_token_schema_instance = PlaidLinkTokenSchema.from_json(json)
# print the JSON string representation of the object
print PlaidLinkTokenSchema.to_json()

# convert the object into a dict
plaid_link_token_schema_dict = plaid_link_token_schema_instance.to_dict()
# create an instance of PlaidLinkTokenSchema from a dict
plaid_link_token_schema_form_dict = plaid_link_token_schema.from_dict(plaid_link_token_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


