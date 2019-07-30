# TransactionInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aria_event_no** | **int** | The Aria assigned ID for the event. | 
**transaction_date** | **str** |  | 
**transaction_type** | **str** |  | [optional] 
**transaction_type_no** | **int** |  | 
**is_charge_type** | **int** |  | [optional] 
**type_specific_id** | **int** | e.g. payment_id for electronic payments, invoice_no for invoices, etc  | [optional] 
**acct_no** | **int** | The Aria assigned ID of the account. | 
**user_id** | **str** | The client defined user_id for the account. | [optional] 
**client_acct_id** | **str** | The client defined account ID for the account. | [optional] 
**amount** | **float** |  | [optional] 
**currency_cd** | **str** |  | [optional] 
**aria_statement_no** | **int** | Aria assigned ID of the statement related to this transaction | [optional] 
**total_amount_applied** | **float** | Total amount applied to any transactions. Does not apply to all transaction types.  | [optional] 
**related_amount_applied** | **float** | Always null. Place holder for related_transaction objects below. | [optional] 
**update_date** | **str** | Date transaction was last updated. | [optional] 
**void_date** | **str** | Void date of any voided transaction associated with the specified event ID number. Example: Void date of an invoice.  | [optional] 
**fully_applied_date** | **str** | Date transaction was fully offset by another transaction | [optional] 
**master_plan_instance_no** | **int** | The Master Plan Instance assigned to the account | [optional] 
**related_transaction** | [**list[RelatedTransaction]**](RelatedTransaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


