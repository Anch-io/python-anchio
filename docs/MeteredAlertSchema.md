# MeteredAlertSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**metric** | **str** |  | 
**threshold** | **float** |  | 
**period** | **str** |  | 
**notification_channels** | **List[str]** |  | 

## Example

```python
from anchio.models.metered_alert_schema import MeteredAlertSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MeteredAlertSchema from a JSON string
metered_alert_schema_instance = MeteredAlertSchema.from_json(json)
# print the JSON string representation of the object
print MeteredAlertSchema.to_json()

# convert the object into a dict
metered_alert_schema_dict = metered_alert_schema_instance.to_dict()
# create an instance of MeteredAlertSchema from a dict
metered_alert_schema_form_dict = metered_alert_schema.from_dict(metered_alert_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


