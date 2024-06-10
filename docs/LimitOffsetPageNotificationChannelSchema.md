# LimitOffsetPageNotificationChannelSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NotificationChannelSchema]**](NotificationChannelSchema.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from anchio.models.limit_offset_page_notification_channel_schema import LimitOffsetPageNotificationChannelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageNotificationChannelSchema from a JSON string
limit_offset_page_notification_channel_schema_instance = LimitOffsetPageNotificationChannelSchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageNotificationChannelSchema.to_json()

# convert the object into a dict
limit_offset_page_notification_channel_schema_dict = limit_offset_page_notification_channel_schema_instance.to_dict()
# create an instance of LimitOffsetPageNotificationChannelSchema from a dict
limit_offset_page_notification_channel_schema_form_dict = limit_offset_page_notification_channel_schema.from_dict(limit_offset_page_notification_channel_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


