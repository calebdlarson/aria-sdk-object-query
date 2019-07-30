# InvoiceDetailsM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_no** | **int** | The Aria assigned ID of the invoice | [optional] 
**acct_no** | **int** | The Aria assigned ID of the account | [optional] 
**user_id** | **str** | The client defined user_id for the account | [optional] 
**client_acct_id** | **str** | Client-specified account identifier | [optional] 
**amount** | **float** |  | [optional] 
**bill_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**paid_date** | **str** |  | [optional] 
**notify_date** | **str** |  | [optional] 
**from_date** | **str** |  | [optional] 
**to_date** | **str** |  | [optional] 
**currency_cd** | **str** |  | [optional] 
**balance_forward** | **float** |  | [optional] 
**statement_balance_forward** | **float** |  | [optional] 
**total_due** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**additional_comments** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**aria_statement_no** | **int** |  | [optional] 
**acct_statement_seq_str** | **str** |  | [optional] 
**second_acct_statement_seq_str** | **str** |  | [optional] 
**voiding_event_no** | **int** | The number given for a voided invoice | [optional] 
**custom_status_label** | **str** | Value allowed for Client specific custom invoice status that can be edited at the invoice or pending invoice level | [optional] 
**client_notes** | **str** | Client specific custom invoice notes that can be edited at the invoice or pending invoice level | [optional] 
**invoice_type_cd** | **str** | This field identifies the type of the invoice generated: &#39;O&#39; - Order based, &#39;F&#39; - Full (anniversary) invoice and &#39;P&#39; - Prorated invoice  | [optional] 
**billing_group_no** | **int** | Billing group for which the invoice was generated | [optional] 
**client_billing_group_id** | **int** | Client assigned billing group id for which the invoice was generated | [optional] 
**invoice_line_m** | [**list[InvoiceLineM]**](InvoiceLineM.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


