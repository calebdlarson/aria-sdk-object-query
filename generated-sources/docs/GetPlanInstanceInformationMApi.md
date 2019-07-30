# swagger_client.GetPlanInstanceInformationMApi

All URIs are relative to *https://secure.future.stage.ariasystems.net/api/AriaQuery/objects.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_plan_instance_information_m**](GetPlanInstanceInformationMApi.md#get_plan_instance_information_m) | **POST** #GetPlanInstanceInformationM | get_plan_instance_information_m


# **get_plan_instance_information_m**
> GetPlanInstanceInformationMResponse get_plan_instance_information_m(body)

get_plan_instance_information_m

Searches for stacks based on query-able fields.  Returns \"plan_instance_details\" 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetPlanInstanceInformationMApi()
body = swagger_client.GetPlanInstanceInformationMRequest() # GetPlanInstanceInformationMRequest | 

try:
    # get_plan_instance_information_m
    api_response = api_instance.get_plan_instance_information_m(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetPlanInstanceInformationMApi->get_plan_instance_information_m: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetPlanInstanceInformationMRequest**](GetPlanInstanceInformationMRequest.md)|  | 

### Return type

[**GetPlanInstanceInformationMResponse**](GetPlanInstanceInformationMResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

