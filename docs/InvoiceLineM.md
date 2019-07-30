# InvoiceLineM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_no** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**plan_no** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_no** | **int** |  | [optional] 
**ledger_code** | **str** |  | [optional] 
**coa_id** | **int** |  | [optional] 
**coa_description** | **str** |  | [optional] 
**usage_units** | **float** |  | [optional] 
**usage_rate** | **float** |  | [optional] 
**usage_type_no** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**client_sku** | **str** |  | [optional] 
**order_no** | **int** |  | [optional] 
**item_no** | **int** |  | [optional] 
**base_plan_units** | **int** |  | [optional] 
**plan_units_change** | **float** | Number of units changed because of an upgrade or downgrade to a plan.  For an upgrade from 1 unit to 3 units,  this would return a value of 2.  The calculation is ?base plan units minus prior base plan units?. This value  will only be calculated if both values are present.  | [optional] 
**proration_factor** | **float** |  | [optional] 
**proration_text** | **str** |  | [optional] 
**adv_billing_period_total_days** | **int** |  | [optional] 
**proration_remaining_days** | **int** |  | [optional] 
**proration_description** | **str** |  | [optional] 
**bill_from_address_no** | **int** | Address sent as the bill-from address to the tax engine for tax calculations.  Depending on the taxation configuration, this parameter may return the Aria-assigned  unique identifier of the service location for the invoice line item. Note that service locations can be associated with a service for a given plan instance on an account,  with an item (NSO) purchased as part of a one-time order, or with a service as defined in the product catalog.  | [optional] 
**ship_from_address_no** | **int** | Address sent as the ship-from address to the tax engine for tax calculations.  Depending on the taxation configuration, this parameter may return the Aria-assigned unique identifier of the service location for the invoice line item. Note that service locations can be associated with a service for a given plan instance on an account,  with an item (NSO) purchased as part of a one-time order, or with a service as defined in the product catalog.  | [optional] 
**bill_to_address_no** | **int** | Address sent as the bill-to address to the tax engine for tax calculations. This parameter will  return the Aria-assigned unique identifier of the contact on the account used as the  bill-to address for the invoice line item.  | [optional] 
**ship_to_address_no** | **int** | Address sent as the ship-to address to the tax engine for tax calculations.  This parameter will return the Aria-assigned unique identifier of the contact on the account used  as the ship-to address for the invoice line item  | [optional] 
**transaction_type** | **str** |  | [optional] 
**master_plan_instance_id** | **int** | Aria generated unique identifier for the master plan instance | [optional] 
**client_master_plan_instance_id** | **str** | Client defined unique identifier for the master plan instance | [optional] 
**invoice_transaction_id** | **int** |  | [optional] 
**po_num** | **str** | Purchase order number assigned to the invoice. | [optional] 
**invoice_line_tax_m** | [**list[InvoiceLineTaxM]**](InvoiceLineTaxM.md) |  | [optional] 
**rate_schedule_no** | **float** |  | [optional] 
**rate_schedule_tier_no** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


