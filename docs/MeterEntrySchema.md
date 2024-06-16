# MeterEntrySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**id** | **str** |  | 
**group** | **str** |  | [optional] 
**metric** | **str** |  | 
**service** | **str** |  | 
**value** | **int** |  | 
**value_type** | [**MeterValueTypeEnum**](MeterValueTypeEnum.md) |  | [optional] 
**currency_iso** | **str** |  | [optional] 
**start** | **datetime** |  | 
**end** | **datetime** |  | 

## Example

```python
from anchio.models.meter_entry_schema import MeterEntrySchema

# TODO update the JSON string below
json = "{}"
# create an instance of MeterEntrySchema from a JSON string
meter_entry_schema_instance = MeterEntrySchema.from_json(json)
# print the JSON string representation of the object
print MeterEntrySchema.to_json()

# convert the object into a dict
meter_entry_schema_dict = meter_entry_schema_instance.to_dict()
# create an instance of MeterEntrySchema from a dict
meter_entry_schema_form_dict = meter_entry_schema.from_dict(meter_entry_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


