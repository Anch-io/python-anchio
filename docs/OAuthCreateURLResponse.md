# OAuthCreateURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**provider** | [**OAuth2Integration**](OAuth2Integration.md) |  | 

## Example

```python
from anchio.models.o_auth_create_url_response import OAuthCreateURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCreateURLResponse from a JSON string
o_auth_create_url_response_instance = OAuthCreateURLResponse.from_json(json)
# print the JSON string representation of the object
print OAuthCreateURLResponse.to_json()

# convert the object into a dict
o_auth_create_url_response_dict = o_auth_create_url_response_instance.to_dict()
# create an instance of OAuthCreateURLResponse from a dict
o_auth_create_url_response_form_dict = o_auth_create_url_response.from_dict(o_auth_create_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


