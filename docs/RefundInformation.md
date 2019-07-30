# RefundInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aria_event_no** | **int** | The Aria assigned ID for the event. | 
**acct_no** | **int** | The Aria assigned ID of the account. | 
**user_id** | **str** | The client defined user_id for the account. | 
**refund_amount** | **float** | Amount of the refund disbursement. | 
**create_date** | **str** |  | 
**create_user** | **str** |  | 
**refund_reason_code** | **int** |  | 
**refund_reason_label** | **str** |  | 
**refund_reason_description** | **str** |  | 
**currency_cd** | **str** |  | 
**aria_statement_no** | **int** |  | 
**ref_payment_event_no** | **int** | The payment event is being refunded. | 
**ref_payment_transaction_type** | **int** | The transaction type code of the payment event that is being refunded.  | 
**ref_payment_transaction_desc** | **str** | The transaction type of the payment event that is being refunded.  | 
**ref_payment_amount** | **float** | The amount of the original payment. | 
**refund_transaction_type** | **int** | The transaction type code of the refund. | 
**refund_transaction_desc** | **str** | The transaction type of the refund. | 
**refund_check_num** | **str** | The check that was recorded as being sent to the end user, for external check refunds.  | 
**refund_bill_seq_no** | **int** | The billing information sequence number used, for electronic refunds.  | 
**refund_pay_method_id** | **int** | The electronic method ID used (e.g. 1), for electronic refunds.  | 
**refund_pay_method_name** | **str** | The pay method name (e.g. Credit Card), for electronic refunds.  | 
**refund_cc_id** | **int** | The credit card type ID used, for electronic refunds. | 
**refund_cc_type** | **str** | The credit card type name (e.g. MasterCard), for electronic refunds.  | 
**refund_payment_src_suffix** | **str** | The payment suffix from the original electronic billing record.  | 
**refund_is_voided_ind** | **int** | Value is 1 if this refund has been subsequently voided, otherwise 0  | 
**bill_email** | **str** | Email of the billing contact.  Note that this value is currently populated only if the payment method is PayPal Express Checkout and configured to update the billing email address with the PayPal Express Checkout email address.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


