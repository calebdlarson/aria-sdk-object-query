# swagger_client.GetAccountPlanHistoryMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_plan_history_m**](GetAccountPlanHistoryMApi.md#get_account_plan_history_m) | **POST** #GetAccountPlanHistoryM | get_account_plan_history_m


# **get_account_plan_history_m**
> GetAccountPlanHistoryMResponse get_account_plan_history_m(body)

get_account_plan_history_m

Gets account plan history for all accounts matching specified query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetAccountPlanHistoryMApi()
body = swagger_client.GetAccountPlanHistoryMRequest() # GetAccountPlanHistoryMRequest | 

try:
    # get_account_plan_history_m
    api_response = api_instance.get_account_plan_history_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetAccountPlanHistoryMApi->get_account_plan_history_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAccountPlanHistoryMRequest**](GetAccountPlanHistoryMRequest.md)|  | 

### Return type

[**GetAccountPlanHistoryMResponse**](GetAccountPlanHistoryMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

