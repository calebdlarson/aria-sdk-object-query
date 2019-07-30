# swagger_client.GetRefundInformationMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_refund_information_m**](GetRefundInformationMApi.md#get_refund_information_m) | **POST** #GetRefundInformationM | get_refund_information_m


# **get_refund_information_m**
> GetRefundInformationMResponse get_refund_information_m(body)

get_refund_information_m

This object includes information about a refund disbursement. Recommended query parameters include acct_no and aria_event_no for optimal performance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetRefundInformationMApi()
body = swagger_client.GetRefundInformationMRequest() # GetRefundInformationMRequest | 

try:
    # get_refund_information_m
    api_response = api_instance.get_refund_information_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetRefundInformationMApi->get_refund_information_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetRefundInformationMRequest**](GetRefundInformationMRequest.md)|  | 

### Return type

[**GetRefundInformationMResponse**](GetRefundInformationMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

