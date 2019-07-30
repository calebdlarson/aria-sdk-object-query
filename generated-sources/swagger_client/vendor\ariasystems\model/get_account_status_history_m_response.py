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

from swagger_client.vendor\ariasystems\model.account_status_history import AccountStatusHistory  # noqa: F401,E501


class GetAccountStatusHistoryMResponse(object):
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
        'error_code': 'int',
        'error_msg': 'str',
        'starting_record': 'int',
        'total_records': 'int',
        'account_status_history': 'list[AccountStatusHistory]'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'starting_record': 'starting_record',
        'total_records': 'total_records',
        'account_status_history': 'account_status_history'
    }

    def __init__(self, error_code=None, error_msg=None, starting_record=None, total_records=None, account_status_history=None):  # noqa: E501
        """GetAccountStatusHistoryMResponse - a model defined in Swagger"""  # noqa: E501

        self._error_code = None
        self._error_msg = None
        self._starting_record = None
        self._total_records = None
        self._account_status_history = None
        self.discriminator = None

        self.error_code = error_code
        self.error_msg = error_msg
        if starting_record is not None:
            self.starting_record = starting_record
        if total_records is not None:
            self.total_records = total_records
        if account_status_history is not None:
            self.account_status_history = account_status_history

    @property
    def error_code(self):
        """Gets the error_code of this GetAccountStatusHistoryMResponse.  # noqa: E501

        Aria-assigned error identifier. 0 indicates no error  # noqa: E501

        :return: The error_code of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this GetAccountStatusHistoryMResponse.

        Aria-assigned error identifier. 0 indicates no error  # noqa: E501

        :param error_code: The error_code of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :type: int
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this GetAccountStatusHistoryMResponse.  # noqa: E501

        Textual description of any error that occurred.  \"OK\" if there was no error.   # noqa: E501

        :return: The error_msg of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this GetAccountStatusHistoryMResponse.

        Textual description of any error that occurred.  \"OK\" if there was no error.   # noqa: E501

        :param error_msg: The error_msg of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :type: str
        """
        if error_msg is None:
            raise ValueError("Invalid value for `error_msg`, must not be `None`")  # noqa: E501

        self._error_msg = error_msg

    @property
    def starting_record(self):
        """Gets the starting_record of this GetAccountStatusHistoryMResponse.  # noqa: E501

        This indicates the number of objects that were (or would be) skipped before beginning output.   # noqa: E501

        :return: The starting_record of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :rtype: int
        """
        return self._starting_record

    @starting_record.setter
    def starting_record(self, starting_record):
        """Sets the starting_record of this GetAccountStatusHistoryMResponse.

        This indicates the number of objects that were (or would be) skipped before beginning output.   # noqa: E501

        :param starting_record: The starting_record of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :type: int
        """

        self._starting_record = starting_record

    @property
    def total_records(self):
        """Gets the total_records of this GetAccountStatusHistoryMResponse.  # noqa: E501

        This is the total number of objects that matched the provided criteria.   # noqa: E501

        :return: The total_records of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this GetAccountStatusHistoryMResponse.

        This is the total number of objects that matched the provided criteria.   # noqa: E501

        :param total_records: The total_records of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :type: int
        """

        self._total_records = total_records

    @property
    def account_status_history(self):
        """Gets the account_status_history of this GetAccountStatusHistoryMResponse.  # noqa: E501

          # noqa: E501

        :return: The account_status_history of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :rtype: list[AccountStatusHistory]
        """
        return self._account_status_history

    @account_status_history.setter
    def account_status_history(self, account_status_history):
        """Sets the account_status_history of this GetAccountStatusHistoryMResponse.

          # noqa: E501

        :param account_status_history: The account_status_history of this GetAccountStatusHistoryMResponse.  # noqa: E501
        :type: list[AccountStatusHistory]
        """

        self._account_status_history = account_status_history

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
        if not isinstance(other, GetAccountStatusHistoryMResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
