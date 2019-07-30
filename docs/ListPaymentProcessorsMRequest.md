# ListPaymentProcessorsMRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest_call** | **str** |  | [default to 'list_payment_processors_m']
**release_version** | **str** |  | [default to '23']
**output_format** | **str** |  | [default to 'json']
**client_no** | **int** | Aria-assigned unique identifier indicating the Aria client providing service to this account.  | 
**auth_key** | **str** | Aria-assigned unique key to be passed with each method call for authenticating the validity of the requestor.  | 
**limit** | **int** | The maximum number of objects to be returned by this call. Note that Aria recommends a maximum limit  of less than 1,000. Higher limits may take much longer to return data. If you do not specify a value,  or specify a value of \&quot;0\&quot;, this field defaults to 100. Specifying a value of \&quot;-1\&quot; returns a count of  the number of matching records, but does not return any records.  | [optional] 
**offset** | **int** | The number of records to skip. Note that both \&quot;0\&quot; and NULL will cause the interface not to skip any records.  | [optional] 
**query_string** | **str** | The criteria which all returned objects must match. Different objects have a different set of searchable criteria. Fields marked with \&quot;*Query\&quot; in the returns section can be used as part of the query_string. Valid operations for the query string include \&quot;&#x3D;\&quot;, \&quot;!&#x3D;\&quot;, \&quot;&lt;\&quot;, \&quot;&lt;&#x3D;\&quot;, \&quot;&gt;&#x3D;\&quot;, \&quot;&gt;\&quot;, \&quot;IS NULL\&quot;, \&quot;IS NOT NULL\&quot;, \&quot;LIKE\&quot;, and \&quot;NOT LIKE\&quot;. You must leave a space before and after each operation. The first operand must always be a field name, and the second operand must always be a value (except for \&quot;IS NULL\&quot; and \&quot;IS NOT NULL\&quot;, where the second operand is implicitly \&quot;NULL\&quot;). If the second operand contains a space, less than, greater than, or equals sign, then it must be enclosed in double quotes. The second operand may not contain double quotes. Multiple conditions must be joined with either \&quot;AND\&quot; or \&quot;OR\&quot;. Additionally, any queryable field can also be used to order the results, by appending \&quot;ORDER BY\&quot; to the query, followed by a field name and either \&quot;ASC\&quot; or \&quot;DESC\&quot;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


