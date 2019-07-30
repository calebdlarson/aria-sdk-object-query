# BillingGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_group_no** | **str** | The system defined billing group ID | [optional] 
**billing_group_name** | **str** |  | [optional] 
**billing_group_description** | **str** |  | [optional] 
**client_billing_group_id** | **str** | The client defined  defined billing group ID | [optional] 
**bg_list_start_master_file** | **int** | Indicates whether or not the account shall be listed at the start of a master file. | [optional] 
**primary_pay_method** | **int** | Primary pay method number | [optional] 
**primary_pay_method_name** | **str** | Primary pay method name | [optional] 
**secondary_pay_method** | **int** | Secondary pay method number | [optional] 
**secondary_pay_method_name** | **str** | Secondary pay method name | [optional] 
**stmt_email_list_cc** | **str** | Array containing the list of additional cc and bcc email addresses. | [optional] 
**stmt_email_list_bcc** | **str** | Array containing the list of additional cc and bcc email addresses. | [optional] 
**collection_group_bg_info** | [**list[CollectionGroupBgInfo]**](CollectionGroupBgInfo.md) | Array for collection groups for billing group | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


