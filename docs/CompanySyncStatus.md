# CompanySyncStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_sync** | [**SyncStatus**](SyncStatus.md) |  | [optional] 
**find_employee_app_sync** | [**SyncStatus**](SyncStatus.md) |  | [optional] 
**activity_sync** | [**SyncStatus**](SyncStatus.md) |  | [optional] 
**plaid_sync** | [**SyncStatus**](SyncStatus.md) |  | [optional] 
**lang_smith_sync** | [**SyncStatus**](SyncStatus.md) |  | [optional] 

## Example

```python
from anchio.models.company_sync_status import CompanySyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySyncStatus from a JSON string
company_sync_status_instance = CompanySyncStatus.from_json(json)
# print the JSON string representation of the object
print CompanySyncStatus.to_json()

# convert the object into a dict
company_sync_status_dict = company_sync_status_instance.to_dict()
# create an instance of CompanySyncStatus from a dict
company_sync_status_form_dict = company_sync_status.from_dict(company_sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


