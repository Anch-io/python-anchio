# NotificationChannelSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**channel** | [**NotificationChannelEnum**](NotificationChannelEnum.md) |  | 
**destination** | **str** |  | 
**company** | **str** |  | 

## Example

```python
from anchio.models.notification_channel_schema import NotificationChannelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelSchema from a JSON string
notification_channel_schema_instance = NotificationChannelSchema.from_json(json)
# print the JSON string representation of the object
print NotificationChannelSchema.to_json()

# convert the object into a dict
notification_channel_schema_dict = notification_channel_schema_instance.to_dict()
# create an instance of NotificationChannelSchema from a dict
notification_channel_schema_form_dict = notification_channel_schema.from_dict(notification_channel_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


