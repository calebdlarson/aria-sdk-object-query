# coding: utf-8

"""
    Object Query API

    Object Query API for Aria billing  # noqa: E501

    OpenAPI spec version: 23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ListPaymentProcessorsMRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rest_call': 'str',
        'release_version': 'str',
        'output_format': 'str',
        'client_no': 'int',
        'auth_key': 'str',
        'limit': 'int',
        'offset': 'int',
        'query_string': 'str'
    }

    attribute_map = {
        'rest_call': 'rest_call',
        'release_version': 'releaseVersion',
        'output_format': 'output_format',
        'client_no': 'client_no',
        'auth_key': 'auth_key',
        'limit': 'limit',
        'offset': 'offset',
        'query_string': 'query_string'
    }

    def __init__(self, rest_call='list_payment_processors_m', release_version='23', output_format='json', client_no=None, auth_key=None, limit=None, offset=None, query_string=None):  # noqa: E501
        """ListPaymentProcessorsMRequest - a model defined in Swagger"""  # noqa: E501

        self._rest_call = None
        self._release_version = None
        self._output_format = None
        self._client_no = None
        self._auth_key = None
        self._limit = None
        self._offset = None
        self._query_string = None
        self.discriminator = None

        self.rest_call = rest_call
        self.release_version = release_version
        self.output_format = output_format
        self.client_no = client_no
        self.auth_key = auth_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if query_string is not None:
            self.query_string = query_string

    @property
    def rest_call(self):
        """Gets the rest_call of this ListPaymentProcessorsMRequest.  # noqa: E501


        :return: The rest_call of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: str
        """
        return self._rest_call

    @rest_call.setter
    def rest_call(self, rest_call):
        """Sets the rest_call of this ListPaymentProcessorsMRequest.


        :param rest_call: The rest_call of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: str
        """
        if rest_call is None:
            raise ValueError("Invalid value for `rest_call`, must not be `None`")  # noqa: E501
        allowed_values = ["list_payment_processors_m"]  # noqa: E501
        if rest_call not in allowed_values:
            raise ValueError(
                "Invalid value for `rest_call` ({0}), must be one of {1}"  # noqa: E501
                .format(rest_call, allowed_values)
            )

        self._rest_call = rest_call

    @property
    def release_version(self):
        """Gets the release_version of this ListPaymentProcessorsMRequest.  # noqa: E501


        :return: The release_version of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        """Sets the release_version of this ListPaymentProcessorsMRequest.


        :param release_version: The release_version of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: str
        """
        if release_version is None:
            raise ValueError("Invalid value for `release_version`, must not be `None`")  # noqa: E501
        allowed_values = ["23"]  # noqa: E501
        if release_version not in allowed_values:
            raise ValueError(
                "Invalid value for `release_version` ({0}), must be one of {1}"  # noqa: E501
                .format(release_version, allowed_values)
            )

        self._release_version = release_version

    @property
    def output_format(self):
        """Gets the output_format of this ListPaymentProcessorsMRequest.  # noqa: E501


        :return: The output_format of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this ListPaymentProcessorsMRequest.


        :param output_format: The output_format of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: str
        """
        if output_format is None:
            raise ValueError("Invalid value for `output_format`, must not be `None`")  # noqa: E501
        allowed_values = ["json"]  # noqa: E501
        if output_format not in allowed_values:
            raise ValueError(
                "Invalid value for `output_format` ({0}), must be one of {1}"  # noqa: E501
                .format(output_format, allowed_values)
            )

        self._output_format = output_format

    @property
    def client_no(self):
        """Gets the client_no of this ListPaymentProcessorsMRequest.  # noqa: E501

        Aria-assigned unique identifier indicating the Aria client providing service to this account.   # noqa: E501

        :return: The client_no of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_no

    @client_no.setter
    def client_no(self, client_no):
        """Sets the client_no of this ListPaymentProcessorsMRequest.

        Aria-assigned unique identifier indicating the Aria client providing service to this account.   # noqa: E501

        :param client_no: The client_no of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: int
        """
        if client_no is None:
            raise ValueError("Invalid value for `client_no`, must not be `None`")  # noqa: E501

        self._client_no = client_no

    @property
    def auth_key(self):
        """Gets the auth_key of this ListPaymentProcessorsMRequest.  # noqa: E501

        Aria-assigned unique key to be passed with each method call for authenticating the validity of the requestor.   # noqa: E501

        :return: The auth_key of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this ListPaymentProcessorsMRequest.

        Aria-assigned unique key to be passed with each method call for authenticating the validity of the requestor.   # noqa: E501

        :param auth_key: The auth_key of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: str
        """
        if auth_key is None:
            raise ValueError("Invalid value for `auth_key`, must not be `None`")  # noqa: E501

        self._auth_key = auth_key

    @property
    def limit(self):
        """Gets the limit of this ListPaymentProcessorsMRequest.  # noqa: E501

        The maximum number of objects to be returned by this call. Note that Aria recommends a maximum limit  of less than 1,000. Higher limits may take much longer to return data. If you do not specify a value,  or specify a value of \"0\", this field defaults to 100. Specifying a value of \"-1\" returns a count of  the number of matching records, but does not return any records.   # noqa: E501

        :return: The limit of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPaymentProcessorsMRequest.

        The maximum number of objects to be returned by this call. Note that Aria recommends a maximum limit  of less than 1,000. Higher limits may take much longer to return data. If you do not specify a value,  or specify a value of \"0\", this field defaults to 100. Specifying a value of \"-1\" returns a count of  the number of matching records, but does not return any records.   # noqa: E501

        :param limit: The limit of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPaymentProcessorsMRequest.  # noqa: E501

        The number of records to skip. Note that both \"0\" and NULL will cause the interface not to skip any records.   # noqa: E501

        :return: The offset of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPaymentProcessorsMRequest.

        The number of records to skip. Note that both \"0\" and NULL will cause the interface not to skip any records.   # noqa: E501

        :param offset: The offset of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def query_string(self):
        """Gets the query_string of this ListPaymentProcessorsMRequest.  # noqa: E501

        The criteria which all returned objects must match. Different objects have a different set of searchable criteria. Fields marked with \"*Query\" in the returns section can be used as part of the query_string. Valid operations for the query string include \"=\", \"!=\", \"<\", \"<=\", \">=\", \">\", \"IS NULL\", \"IS NOT NULL\", \"LIKE\", and \"NOT LIKE\". You must leave a space before and after each operation. The first operand must always be a field name, and the second operand must always be a value (except for \"IS NULL\" and \"IS NOT NULL\", where the second operand is implicitly \"NULL\"). If the second operand contains a space, less than, greater than, or equals sign, then it must be enclosed in double quotes. The second operand may not contain double quotes. Multiple conditions must be joined with either \"AND\" or \"OR\". Additionally, any queryable field can also be used to order the results, by appending \"ORDER BY\" to the query, followed by a field name and either \"ASC\" or \"DESC\".   # noqa: E501

        :return: The query_string of this ListPaymentProcessorsMRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this ListPaymentProcessorsMRequest.

        The criteria which all returned objects must match. Different objects have a different set of searchable criteria. Fields marked with \"*Query\" in the returns section can be used as part of the query_string. Valid operations for the query string include \"=\", \"!=\", \"<\", \"<=\", \">=\", \">\", \"IS NULL\", \"IS NOT NULL\", \"LIKE\", and \"NOT LIKE\". You must leave a space before and after each operation. The first operand must always be a field name, and the second operand must always be a value (except for \"IS NULL\" and \"IS NOT NULL\", where the second operand is implicitly \"NULL\"). If the second operand contains a space, less than, greater than, or equals sign, then it must be enclosed in double quotes. The second operand may not contain double quotes. Multiple conditions must be joined with either \"AND\" or \"OR\". Additionally, any queryable field can also be used to order the results, by appending \"ORDER BY\" to the query, followed by a field name and either \"ASC\" or \"DESC\".   # noqa: E501

        :param query_string: The query_string of this ListPaymentProcessorsMRequest.  # noqa: E501
        :type: str
        """

        self._query_string = query_string

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPaymentProcessorsMRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
