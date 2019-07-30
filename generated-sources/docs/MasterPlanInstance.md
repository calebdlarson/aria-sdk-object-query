# MasterPlanInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_plan_instance_id** | **str** |  | [optional] 
**client_master_plan_instance_id** | **str** |  | [optional] 
**client_master_plan_id** | **str** |  | [optional] 
**master_plan_no** | **str** |  | [optional] 
**master_plan_instance_description** | **str** |  | [optional] 
**dunning_group_no** | **int** | Aria Internal Id for dunning group | [optional] 
**client_dunning_group_id** | **str** | Client defined dunning group id | [optional] 
**dunning_group_name** | **str** | Name of the dunning group | [optional] 
**dunning_group_description** | **str** | Dunning group description | [optional] 
**dunning_process_no** | **int** | The unique identifier of the dunning process | [optional] 
**client_dunning_process_id** | **str** | The client-defined identifier of the dunning process | [optional] 
**po_num** | **str** | Purchase order number assigned to the account or plan instance. | [optional] 
**supp_plans** | [**list[SuppPlan]**](SuppPlan.md) |  | [optional] 
**coupon_cd** | [**list[CouponCd]**](CouponCd.md) |  | 
**master_plan_plan_inst_fields** | [**list[MasterPlanPlanInstField]**](MasterPlanPlanInstField.md) |  | [optional] 
**bill_lag_days** | **int** | Bill lag days refer to the number of days prior to (negative) or after (positive) an account billing date at which an invoice should be generated for this Master Plan Instance.  Negative bill lag days are typically used for subscription-based services (often subscription-based services paid using net-terms), in which the user would like to send out invoices to customers well in advance of the real invoice date.  Positive bill lag days are typically used for usage-based services.   By default, bill lag days are restricted to +/- the (minimum number of days in a recurring interval period  ? 1 day).  However, if the ?Allow Negative Bill Lag Days to Extend Beyond One Bill Cycle?is enabled   set to TRUE)), then the negative value can go beyond a single recurring interval.  The precedence for bill lag days is as follows: Master Plan Instance (for a given account) &gt; Collection Group setting &gt; Payment Gateway setting &gt; Client  setting (Configuration ? Billing ? Bill Lag Days)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


