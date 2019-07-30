# RelatedTransaction

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
**amount** | **float** |  | [optional] 
**currency_cd** | **str** |  | [optional] 
**aria_statement_no** | **int** | Aria assigned ID of the statement related to this transaction  | [optional] 
**total_amount_applied** | **float** | Total amount applied to any other transactions | [optional] 
**related_amount_applied** | **float** | Amount applied to this transaction | [optional] 
**update_date** | **str** | Date transaction was last updated. | 
**void_date** | **str** | Void date of related transactions associated with the specified event ID number. Example: Void date of a payment.  | [optional] 
**fully_applied_date** | **str** | Date transaction was fully offset by another transaction | 
**master_plan_instance_no** | **int** | The Master Plan Instance assigned to the account | [optional] 
**related_amount** | **float** | Amount applied to this transaction. Duplicate of related_amount_applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


