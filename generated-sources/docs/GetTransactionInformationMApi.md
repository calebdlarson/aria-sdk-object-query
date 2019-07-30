# swagger_client.GetTransactionInformationMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_information_m**](GetTransactionInformationMApi.md#get_transaction_information_m) | **POST** #GetTransactionInformationM | get_transaction_information_m


# **get_transaction_information_m**
> GetTransactionInformationMResponse get_transaction_information_m(body)

get_transaction_information_m

Gets transactional details for all accounts matching specified query. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetTransactionInformationMApi()
body = swagger_client.GetTransactionInformationMRequest() # GetTransactionInformationMRequest | 

try:
    # get_transaction_information_m
    api_response = api_instance.get_transaction_information_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetTransactionInformationMApi->get_transaction_information_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetTransactionInformationMRequest**](GetTransactionInformationMRequest.md)|  | 

### Return type

[**GetTransactionInformationMResponse**](GetTransactionInformationMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

