# CheckoutSessionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from anchio.models.checkout_session_schema import CheckoutSessionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionSchema from a JSON string
checkout_session_schema_instance = CheckoutSessionSchema.from_json(json)
# print the JSON string representation of the object
print CheckoutSessionSchema.to_json()

# convert the object into a dict
checkout_session_schema_dict = checkout_session_schema_instance.to_dict()
# create an instance of CheckoutSessionSchema from a dict
checkout_session_schema_form_dict = checkout_session_schema.from_dict(checkout_session_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


