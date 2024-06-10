# SlackChannelPurpose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**creator** | **str** |  | 
**last_set** | **int** |  | 

## Example

```python
from anchio.models.slack_channel_purpose import SlackChannelPurpose

# TODO update the JSON string below
json = "{}"
# create an instance of SlackChannelPurpose from a JSON string
slack_channel_purpose_instance = SlackChannelPurpose.from_json(json)
# print the JSON string representation of the object
print SlackChannelPurpose.to_json()

# convert the object into a dict
slack_channel_purpose_dict = slack_channel_purpose_instance.to_dict()
# create an instance of SlackChannelPurpose from a dict
slack_channel_purpose_form_dict = slack_channel_purpose.from_dict(slack_channel_purpose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


