# CheckoutSessionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_url** | **str** |  | 
**cancel_url** | **str** |  | 

## Example

```python
from anchio.models.checkout_session_request_schema import CheckoutSessionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionRequestSchema from a JSON string
checkout_session_request_schema_instance = CheckoutSessionRequestSchema.from_json(json)
# print the JSON string representation of the object
print CheckoutSessionRequestSchema.to_json()

# convert the object into a dict
checkout_session_request_schema_dict = checkout_session_request_schema_instance.to_dict()
# create an instance of CheckoutSessionRequestSchema from a dict
checkout_session_request_schema_form_dict = checkout_session_request_schema.from_dict(checkout_session_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


