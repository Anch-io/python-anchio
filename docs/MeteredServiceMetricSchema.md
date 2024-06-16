# MeteredServiceMetricSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**service** | **str** |  | 
**name** | **str** |  | 
**value_type** | [**MeterValueTypeEnum**](MeterValueTypeEnum.md) |  | 
**currency_iso** | **str** |  | [optional] 

## Example

```python
from anchio.models.metered_service_metric_schema import MeteredServiceMetricSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MeteredServiceMetricSchema from a JSON string
metered_service_metric_schema_instance = MeteredServiceMetricSchema.from_json(json)
# print the JSON string representation of the object
print MeteredServiceMetricSchema.to_json()

# convert the object into a dict
metered_service_metric_schema_dict = metered_service_metric_schema_instance.to_dict()
# create an instance of MeteredServiceMetricSchema from a dict
metered_service_metric_schema_form_dict = metered_service_metric_schema.from_dict(metered_service_metric_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


