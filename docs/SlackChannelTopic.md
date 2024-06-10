# SlackChannelTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**creator** | **str** |  | 
**last_set** | **int** |  | 

## Example

```python
from anchio.models.slack_channel_topic import SlackChannelTopic

# TODO update the JSON string below
json = "{}"
# create an instance of SlackChannelTopic from a JSON string
slack_channel_topic_instance = SlackChannelTopic.from_json(json)
# print the JSON string representation of the object
print SlackChannelTopic.to_json()

# convert the object into a dict
slack_channel_topic_dict = slack_channel_topic_instance.to_dict()
# create an instance of SlackChannelTopic from a dict
slack_channel_topic_form_dict = slack_channel_topic.from_dict(slack_channel_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


