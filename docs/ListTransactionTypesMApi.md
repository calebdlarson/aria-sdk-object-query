# swagger_client.ListTransactionTypesMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_transaction_types_m**](ListTransactionTypesMApi.md#list_transaction_types_m) | **POST** #ListTransactionTypesM | list_transaction_types_m


# **list_transaction_types_m**
> ListTransactionTypesMResponse list_transaction_types_m(body)

list_transaction_types_m

Retrieves list of transaction types recorded by Aria Systems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ListTransactionTypesMApi()
body = swagger_client.ListTransactionTypesMRequest() # ListTransactionTypesMRequest | 

try:
    # list_transaction_types_m
    api_response = api_instance.list_transaction_types_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListTransactionTypesMApi->list_transaction_types_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListTransactionTypesMRequest**](ListTransactionTypesMRequest.md)|  | 

### Return type

[**ListTransactionTypesMResponse**](ListTransactionTypesMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

