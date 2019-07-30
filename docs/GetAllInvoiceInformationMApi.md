# swagger_client.GetAllInvoiceInformationMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_invoice_information_m**](GetAllInvoiceInformationMApi.md#get_all_invoice_information_m) | **POST** #GetAllInvoiceInformationM | get_all_invoice_information_m


# **get_all_invoice_information_m**
> GetAllInvoiceInformationMResponse get_all_invoice_information_m(body)

get_all_invoice_information_m

This API returns both real and pending invoice details for all accounts matching specified query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetAllInvoiceInformationMApi()
body = swagger_client.GetAllInvoiceInformationMRequest() # GetAllInvoiceInformationMRequest | 

try:
    # get_all_invoice_information_m
    api_response = api_instance.get_all_invoice_information_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetAllInvoiceInformationMApi->get_all_invoice_information_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAllInvoiceInformationMRequest**](GetAllInvoiceInformationMRequest.md)|  | 

### Return type

[**GetAllInvoiceInformationMResponse**](GetAllInvoiceInformationMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

