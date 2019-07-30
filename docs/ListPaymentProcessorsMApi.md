# swagger_client.ListPaymentProcessorsMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_processors_m**](ListPaymentProcessorsMApi.md#list_payment_processors_m) | **POST** #ListPaymentProcessorsM | list_payment_processors_m


# **list_payment_processors_m**
> ListPaymentProcessorsMResponse list_payment_processors_m(body)

list_payment_processors_m

Retrieves list of payment processors supported by Aria Systems. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListPaymentProcessorsMApi()
body = swagger_client.ListPaymentProcessorsMRequest() # ListPaymentProcessorsMRequest | 

try:
    # list_payment_processors_m
    api_response = api_instance.list_payment_processors_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListPaymentProcessorsMApi->list_payment_processors_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListPaymentProcessorsMRequest**](ListPaymentProcessorsMRequest.md)|  | 

### Return type

[**ListPaymentProcessorsMResponse**](ListPaymentProcessorsMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

