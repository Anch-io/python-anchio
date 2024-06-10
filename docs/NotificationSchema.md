# NotificationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**object_id** | **str** |  | 
**content_type** | [**ContentTypeNaturalKey**](ContentTypeNaturalKey.md) |  | 
**message** | **str** |  | 
**status** | [**NotificationStatusEnum**](NotificationStatusEnum.md) |  | 
**priority** | [**NotificationPriorityEnum**](NotificationPriorityEnum.md) |  | 
**company** | **str** |  | 
**license** | **str** |  | [optional] 

## Example

```python
from anchio.models.notification_schema import NotificationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSchema from a JSON string
notification_schema_instance = NotificationSchema.from_json(json)
# print the JSON string representation of the object
print NotificationSchema.to_json()

# convert the object into a dict
notification_schema_dict = notification_schema_instance.to_dict()
# create an instance of NotificationSchema from a dict
notification_schema_form_dict = notification_schema.from_dict(notification_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


