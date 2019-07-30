# swagger_client.ListPaymentMethodsMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_methods_m**](ListPaymentMethodsMApi.md#list_payment_methods_m) | **POST** #ListPaymentMethodsM | list_payment_methods_m


# **list_payment_methods_m**
> ListPaymentMethodsMResponse list_payment_methods_m(body)

list_payment_methods_m

Retrieves list of payment methods known by Aria Systems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListPaymentMethodsMApi()
body = swagger_client.ListPaymentMethodsMRequest() # ListPaymentMethodsMRequest | 

try:
    # list_payment_methods_m
    api_response = api_instance.list_payment_methods_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListPaymentMethodsMApi->list_payment_methods_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListPaymentMethodsMRequest**](ListPaymentMethodsMRequest.md)|  | 

### Return type

[**ListPaymentMethodsMResponse**](ListPaymentMethodsMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

