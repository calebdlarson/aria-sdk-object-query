# OrderDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_no** | **int** | The Aria assigned ID of the order | 
**acct_no** | **int** | The Aria assigned ID of the account | 
**user_id** | **str** | The client defined user_id for the account | 
**invoice_no** | **str** | The Aria assigned ID of the invoice on which this order appears | [optional] 
**create_date** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**currency_cd** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**order_status** | **str** |  | 
**po_num** | **str** | Purchase Order Number for this order. | [optional] 
**order_item** | [**list[OrderItem]**](OrderItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


