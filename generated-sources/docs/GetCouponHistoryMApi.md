# swagger_client.GetCouponHistoryMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coupon_history_m**](GetCouponHistoryMApi.md#get_coupon_history_m) | **POST** #GetCouponHistoryM | get_coupon_history_m


# **get_coupon_history_m**
> GetCouponHistoryMResponse get_coupon_history_m(body)

get_coupon_history_m

This API returns a list of coupons applied to an account and/or master  plan instances. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetCouponHistoryMApi()
body = swagger_client.GetCouponHistoryMRequest() # GetCouponHistoryMRequest | 

try:
    # get_coupon_history_m
    api_response = api_instance.get_coupon_history_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetCouponHistoryMApi->get_coupon_history_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetCouponHistoryMRequest**](GetCouponHistoryMRequest.md)|  | 

### Return type

[**GetCouponHistoryMResponse**](GetCouponHistoryMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

