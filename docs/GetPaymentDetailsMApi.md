# swagger_client.GetPaymentDetailsMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_details_m**](GetPaymentDetailsMApi.md#get_payment_details_m) | **POST** #GetPaymentDetailsM | get_payment_details_m


# **get_payment_details_m**
> GetPaymentDetailsMResponse get_payment_details_m(body)

get_payment_details_m

Gets payment details for all accounts matching specified query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetPaymentDetailsMApi()
body = swagger_client.GetPaymentDetailsMRequest() # GetPaymentDetailsMRequest | 

try:
    # get_payment_details_m
    api_response = api_instance.get_payment_details_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPaymentDetailsMApi->get_payment_details_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetPaymentDetailsMRequest**](GetPaymentDetailsMRequest.md)|  | 

### Return type

[**GetPaymentDetailsMResponse**](GetPaymentDetailsMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

