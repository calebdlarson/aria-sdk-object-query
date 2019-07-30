# GetOrderDetailsMResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Aria-assigned error identifier. 0 indicates no error | 
**error_msg** | **str** | Textual description of any error that occurred.  \&quot;OK\&quot; if there was no error.  | 
**starting_record** | **int** | This indicates the number of objects that were (or would be) skipped before beginning output.  | [optional] 
**total_records** | **int** | This is the total number of objects that matched the provided criteria.  | [optional] 
**order_details** | [**list[OrderDetail]**](OrderDetail.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


