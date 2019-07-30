# swagger_client.GetAccountDetailsMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_details_m**](GetAccountDetailsMApi.md#get_account_details_m) | **POST** #GetAccountDetailsM | get_account_details_m


# **get_account_details_m**
> GetAccountDetailsMResponse get_account_details_m(body)

get_account_details_m

Gets detailed account level information for all accounts matching specified query. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetAccountDetailsMApi()
body = swagger_client.GetAccountDetailsMRequest() # GetAccountDetailsMRequest | 

try:
    # get_account_details_m
    api_response = api_instance.get_account_details_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetAccountDetailsMApi->get_account_details_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAccountDetailsMRequest**](GetAccountDetailsMRequest.md)|  | 

### Return type

[**GetAccountDetailsMResponse**](GetAccountDetailsMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

