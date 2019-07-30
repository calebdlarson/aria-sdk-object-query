# AllInvoiceDetailsM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_no** | **int** | The Aria assigned ID of the invoice | [optional] 
**acct_no** | **int** | The Aria assigned ID of the account | [optional] 
**user_id** | **str** | The client defined user_id for the account | [optional] 
**client_acct_id** | **str** | Client-specified account identifier | [optional] 
**invoice_type** | **str** | Determines if this is a real invoice (R) or a pending invoice (P) | [optional] 
**from_date** | **str** |  | [optional] 
**to_date** | **str** |  | [optional] 
**usage_bill_from_date** | **str** |  | [optional] 
**usage_bill_thru_date** | **str** |  | [optional] 
**taxed_email** | **str** | The email address of the taxed contact, or the general billing email address. | [optional] 
**taxed_first_name** | **str** | The first name of the taxed contact for the account. | [optional] 
**taxed_middle_initial** | **str** | The middle initial of the taxed contact. | [optional] 
**taxed_last_name** | **str** | The last name of the taxed contact. | [optional] 
**taxed_address1** | **str** | Street address (number and name) of the taxed contact address. | [optional] 
**taxed_address2** | **str** | The second taxed address line (for example: bldg, suite, apt., etc.) | [optional] 
**taxed_address3** | **str** | The third taxed address line (for example: bldg, suite, apt., etc.) | [optional] 
**taxed_city** | **str** | The city name of the taxed contact address. | [optional] 
**taxed_state** | **str** | The state or province of the taxed contact&#39;s address.  The official postal-service codes for all United States  and Canada states, provinces, and territories.  | [optional] 
**taxed_locality** | **str** | The billing contact&#39;s locality (for example: county, rural unincorporated area name).  | [optional] 
**taxed_zip** | **str** | The zip or postal code for the taxed contact&#39;s address.  | [optional] 
**taxed_country** | **str** | The country for the taxed contact&#39;s address.  The ISO-compliant 2-character country code abbreviation in uppercase.  | [optional] 
**amount** | **float** |  | [optional] 
**bill_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**paid_date** | **str** |  | [optional] 
**notify_date** | **str** |  | [optional] 
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
**invoice_line_items** | **str** | Whether or not the invoice has any line items | [optional] 
**voiding_event_no** | **int** | The number given for a voided invoice | [optional] 
**bill_company_name** | **str** | The company name of the billing contact for the invoice | [optional] 
**pay_method_type** | **int** | Integer values for the Aria supported payment method types. Allowable values are: 1, 0, 1-19 and 26.  | [optional] 
**pay_method_name** | **str** | Human readable names for the Aria supported payment method types. Allowable values are:   i. External Payment, ii. Other, iii. Credit card, iv. Electronic Check (ACH), v. Pre-paid4Net terms 30, vi. Net terms 10, vii. Net terms 15, viii. Net terms 60, ix. Click&amp;Buy, x. Net Terms 0, xi. PayByCash, xii. PayPal Express Checkout, xiii. Net Terms 45, xiv. Tokenized Credit Card, xv. Purchase Power, xvi. Net Terms 35, xvii. Net Terms 75, xviii. Net Terms 90, xix. Net Terms 120, xx. Net Terms 25, xxi. Direct Debit.  | [optional] 
**custom_status_label** | **str** | Value allowed for Client specific custom invoice status that can be edited at the invoice or pending invoice level | [optional] 
**client_notes** | **str** | Client specific custom invoice notes that can be edited at the invoice or pending invoice level | [optional] 
**billing_group_no** | **int** | Billing group for which the invoice was generated | [optional] 
**client_billing_group_id** | **str** | Client assigned billing group id for which the invoice was generated | [optional] 
**all_invoice_line_m** | [**list[AllInvoiceLineM]**](AllInvoiceLineM.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

