# SlackChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_channel** | **bool** |  | 
**is_group** | **bool** |  | 
**is_im** | **bool** |  | 
**created** | **int** |  | 
**creator** | **str** |  | 
**is_archived** | **bool** |  | 
**is_general** | **bool** |  | 
**unlinked** | **int** |  | 
**name_normalized** | **str** |  | 
**is_shared** | **bool** |  | 
**is_ext_shared** | **bool** |  | 
**is_org_shared** | **bool** |  | 
**pending_shared** | **List[str]** |  | 
**is_pending_ext_shared** | **bool** |  | 
**is_member** | **bool** |  | 
**is_private** | **bool** |  | 
**is_mpim** | **bool** |  | 
**updated** | **int** |  | 
**topic** | [**SlackChannelTopic**](SlackChannelTopic.md) |  | 
**purpose** | [**SlackChannelPurpose**](SlackChannelPurpose.md) |  | 
**previous_names** | **List[str]** |  | 
**num_members** | **int** |  | 

## Example

```python
from anchio.models.slack_channel import SlackChannel

# TODO update the JSON string below
json = "{}"
# create an instance of SlackChannel from a JSON string
slack_channel_instance = SlackChannel.from_json(json)
# print the JSON string representation of the object
print SlackChannel.to_json()

# convert the object into a dict
slack_channel_dict = slack_channel_instance.to_dict()
# create an instance of SlackChannel from a dict
slack_channel_form_dict = slack_channel.from_dict(slack_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


