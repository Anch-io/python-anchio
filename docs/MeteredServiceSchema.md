# MeteredServiceSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**tool_contract** | **str** |  | 
**source** | [**MeteringServiceSourceEnum**](MeteringServiceSourceEnum.md) |  | 
**seven_day_usage** | **int** |  | [optional] 
**thirty_day_usage** | **int** |  | [optional] 
**ninety_day_usage** | **int** |  | [optional] 

## Example

```python
from anchio.models.metered_service_schema import MeteredServiceSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MeteredServiceSchema from a JSON string
metered_service_schema_instance = MeteredServiceSchema.from_json(json)
# print the JSON string representation of the object
print MeteredServiceSchema.to_json()

# convert the object into a dict
metered_service_schema_dict = metered_service_schema_instance.to_dict()
# create an instance of MeteredServiceSchema from a dict
metered_service_schema_form_dict = metered_service_schema.from_dict(metered_service_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


