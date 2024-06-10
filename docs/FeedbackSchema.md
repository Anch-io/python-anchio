# FeedbackSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 

## Example

```python
from anchio.models.feedback_schema import FeedbackSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackSchema from a JSON string
feedback_schema_instance = FeedbackSchema.from_json(json)
# print the JSON string representation of the object
print FeedbackSchema.to_json()

# convert the object into a dict
feedback_schema_dict = feedback_schema_instance.to_dict()
# create an instance of FeedbackSchema from a dict
feedback_schema_form_dict = feedback_schema.from_dict(feedback_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


