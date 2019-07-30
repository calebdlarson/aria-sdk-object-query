# PlanInstanceDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acct_no** | **int** | The Aria assigned ID of the account | [optional] 
**user_id** | **str** | The client defined user_id for the account | [optional] 
**client_acct_id** | **str** | Client specified account identifier | [optional] 
**plan_instance_no** | **str** | The system defined ID of the plan instance | [optional] 
**client_plan_instance_id** | **str** | The client defined ID of the plan instance | [optional] 
**product_fields** | [**list[ProductField]**](ProductField.md) |  | 
**plan_no** | **int** | The Aria assigned ID of the master plan for this account | [optional] 
**client_plan_id** | **str** | The client defined ID of the plan on this instance | [optional] 
**plan_name** | **str** | The name of the plan on this instance | [optional] 
**plan_units** | **int** | The number of units assigned to this instance | [optional] 
**last_bill_date** | **str** | The last date on which the plan instance was billed | [optional] 
**next_bill_date** | **str** | The next date on which the plan instance is scheduled to be billed | [optional] 
**bill_thru_date** | **str** | The date through which the plan instance has been billed | [optional] 
**status_cd** | **str** | The status code of the plan instance  | [optional] 
**status_date** | **str** | The date at which the plan instance entered the current status | [optional] 
**schedule_no** | **str** | The balance of this \&quot;stack\&quot; (master plan instance only) | [optional] 
**master_plan_instance_balance** | **float** | The balance of this \&quot;master plan instance\&quot; | [optional] 
**billing_group_no** | **int** | The system defined billing group ID | [optional] 
**client_billing_group_id** | **str** | The client defined  defined billing group ID | [optional] 
**dunning_group_no** | **int** | The system defined dunning group ID | [optional] 
**responsibility_level_cd** | **float** | The responsibility level code. These are values 1 through 3 as described in the legend for this argument. | [optional] 
**responsible_plan_instance_no** | **int** | Identifier for the responsible plan instance. Applicable if responsibility_level_cd is 2 or 3. | [optional] 
**primary_payment_method_info** | [**list[PrimaryPaymentMethodInfo]**](PrimaryPaymentMethodInfo.md) |  | 
**backup_payment_method_info** | [**list[BackupPaymentMethodInfo]**](BackupPaymentMethodInfo.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


