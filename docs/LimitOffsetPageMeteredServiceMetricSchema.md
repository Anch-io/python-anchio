# LimitOffsetPageMeteredServiceMetricSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MeteredServiceMetricSchema]**](MeteredServiceMetricSchema.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from anchio.models.limit_offset_page_metered_service_metric_schema import LimitOffsetPageMeteredServiceMetricSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LimitOffsetPageMeteredServiceMetricSchema from a JSON string
limit_offset_page_metered_service_metric_schema_instance = LimitOffsetPageMeteredServiceMetricSchema.from_json(json)
# print the JSON string representation of the object
print LimitOffsetPageMeteredServiceMetricSchema.to_json()

# convert the object into a dict
limit_offset_page_metered_service_metric_schema_dict = limit_offset_page_metered_service_metric_schema_instance.to_dict()
# create an instance of LimitOffsetPageMeteredServiceMetricSchema from a dict
limit_offset_page_metered_service_metric_schema_form_dict = limit_offset_page_metered_service_metric_schema.from_dict(limit_offset_page_metered_service_metric_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


