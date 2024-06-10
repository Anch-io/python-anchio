# OAuthPostAuthorizationUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_response** | **str** |  | 
**redirect_uri** | **str** |  | 

## Example

```python
from anchio.models.o_auth_post_authorization_url import OAuthPostAuthorizationUrl

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthPostAuthorizationUrl from a JSON string
o_auth_post_authorization_url_instance = OAuthPostAuthorizationUrl.from_json(json)
# print the JSON string representation of the object
print OAuthPostAuthorizationUrl.to_json()

# convert the object into a dict
o_auth_post_authorization_url_dict = o_auth_post_authorization_url_instance.to_dict()
# create an instance of OAuthPostAuthorizationUrl from a dict
o_auth_post_authorization_url_form_dict = o_auth_post_authorization_url.from_dict(o_auth_post_authorization_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


