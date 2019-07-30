# swagger_client.GetAccountStatusHistoryMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_status_history_m**](GetAccountStatusHistoryMApi.md#get_account_status_history_m) | **POST** #GetAccountStatusHistoryM | get_account_status_history_m


# **get_account_status_history_m**
> GetAccountStatusHistoryMResponse get_account_status_history_m(body)

get_account_status_history_m

Gets account status history for all accounts matching specified query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetAccountStatusHistoryMApi()
body = swagger_client.GetAccountStatusHistoryMRequest() # GetAccountStatusHistoryMRequest | 

try:
    # get_account_status_history_m
    api_response = api_instance.get_account_status_history_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetAccountStatusHistoryMApi->get_account_status_history_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAccountStatusHistoryMRequest**](GetAccountStatusHistoryMRequest.md)|  | 

### Return type

[**GetAccountStatusHistoryMResponse**](GetAccountStatusHistoryMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

