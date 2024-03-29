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


class CouponHistoryM(object):
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
        'acct_no': 'int',
        'user_id': 'str',
        'client_acct_id': 'str',
        'master_plan_instance_id': 'str',
        'client_master_plan_instance_id': 'str',
        'currency_cd': 'str',
        'coupon_cd': 'str',
        'coupon_create_date': 'str',
        'coupon_status': 'str',
        'coupon_cancel_date': 'str'
    }

    attribute_map = {
        'acct_no': 'acct_no',
        'user_id': 'user_id',
        'client_acct_id': 'client_acct_id',
        'master_plan_instance_id': 'master_plan_instance_id',
        'client_master_plan_instance_id': 'client_master_plan_instance_id',
        'currency_cd': 'currency_cd',
        'coupon_cd': 'coupon_cd',
        'coupon_create_date': 'coupon_create_date',
        'coupon_status': 'coupon_status',
        'coupon_cancel_date': 'coupon_cancel_date'
    }

    def __init__(self, acct_no=None, user_id=None, client_acct_id=None, master_plan_instance_id=None, client_master_plan_instance_id=None, currency_cd=None, coupon_cd=None, coupon_create_date=None, coupon_status=None, coupon_cancel_date=None):  # noqa: E501
        """CouponHistoryM - a model defined in Swagger"""  # noqa: E501

        self._acct_no = None
        self._user_id = None
        self._client_acct_id = None
        self._master_plan_instance_id = None
        self._client_master_plan_instance_id = None
        self._currency_cd = None
        self._coupon_cd = None
        self._coupon_create_date = None
        self._coupon_status = None
        self._coupon_cancel_date = None
        self.discriminator = None

        self.acct_no = acct_no
        self.user_id = user_id
        self.client_acct_id = client_acct_id
        self.master_plan_instance_id = master_plan_instance_id
        self.client_master_plan_instance_id = client_master_plan_instance_id
        self.currency_cd = currency_cd
        self.coupon_cd = coupon_cd
        self.coupon_create_date = coupon_create_date
        self.coupon_status = coupon_status
        self.coupon_cancel_date = coupon_cancel_date

    @property
    def acct_no(self):
        """Gets the acct_no of this CouponHistoryM.  # noqa: E501

        Aria-assigned unique account identifier.  # noqa: E501

        :return: The acct_no of this CouponHistoryM.  # noqa: E501
        :rtype: int
        """
        return self._acct_no

    @acct_no.setter
    def acct_no(self, acct_no):
        """Sets the acct_no of this CouponHistoryM.

        Aria-assigned unique account identifier.  # noqa: E501

        :param acct_no: The acct_no of this CouponHistoryM.  # noqa: E501
        :type: int
        """
        if acct_no is None:
            raise ValueError("Invalid value for `acct_no`, must not be `None`")  # noqa: E501

        self._acct_no = acct_no

    @property
    def user_id(self):
        """Gets the user_id of this CouponHistoryM.  # noqa: E501

        Unique alphanumeric identifier for an account holder.  # noqa: E501

        :return: The user_id of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CouponHistoryM.

        Unique alphanumeric identifier for an account holder.  # noqa: E501

        :param user_id: The user_id of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def client_acct_id(self):
        """Gets the client_acct_id of this CouponHistoryM.  # noqa: E501

        Client-specified account identifier  # noqa: E501

        :return: The client_acct_id of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._client_acct_id

    @client_acct_id.setter
    def client_acct_id(self, client_acct_id):
        """Sets the client_acct_id of this CouponHistoryM.

        Client-specified account identifier  # noqa: E501

        :param client_acct_id: The client_acct_id of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if client_acct_id is None:
            raise ValueError("Invalid value for `client_acct_id`, must not be `None`")  # noqa: E501

        self._client_acct_id = client_acct_id

    @property
    def master_plan_instance_id(self):
        """Gets the master_plan_instance_id of this CouponHistoryM.  # noqa: E501

        Aria generated unique identifier for the master plan instance  # noqa: E501

        :return: The master_plan_instance_id of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._master_plan_instance_id

    @master_plan_instance_id.setter
    def master_plan_instance_id(self, master_plan_instance_id):
        """Sets the master_plan_instance_id of this CouponHistoryM.

        Aria generated unique identifier for the master plan instance  # noqa: E501

        :param master_plan_instance_id: The master_plan_instance_id of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if master_plan_instance_id is None:
            raise ValueError("Invalid value for `master_plan_instance_id`, must not be `None`")  # noqa: E501

        self._master_plan_instance_id = master_plan_instance_id

    @property
    def client_master_plan_instance_id(self):
        """Gets the client_master_plan_instance_id of this CouponHistoryM.  # noqa: E501

        Client defined unique identifier for the master plan instance  # noqa: E501

        :return: The client_master_plan_instance_id of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._client_master_plan_instance_id

    @client_master_plan_instance_id.setter
    def client_master_plan_instance_id(self, client_master_plan_instance_id):
        """Sets the client_master_plan_instance_id of this CouponHistoryM.

        Client defined unique identifier for the master plan instance  # noqa: E501

        :param client_master_plan_instance_id: The client_master_plan_instance_id of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if client_master_plan_instance_id is None:
            raise ValueError("Invalid value for `client_master_plan_instance_id`, must not be `None`")  # noqa: E501

        self._client_master_plan_instance_id = client_master_plan_instance_id

    @property
    def currency_cd(self):
        """Gets the currency_cd of this CouponHistoryM.  # noqa: E501

        ISO currency code.  # noqa: E501

        :return: The currency_cd of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._currency_cd

    @currency_cd.setter
    def currency_cd(self, currency_cd):
        """Sets the currency_cd of this CouponHistoryM.

        ISO currency code.  # noqa: E501

        :param currency_cd: The currency_cd of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if currency_cd is None:
            raise ValueError("Invalid value for `currency_cd`, must not be `None`")  # noqa: E501

        self._currency_cd = currency_cd

    @property
    def coupon_cd(self):
        """Gets the coupon_cd of this CouponHistoryM.  # noqa: E501

        Coupon identification code.  # noqa: E501

        :return: The coupon_cd of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._coupon_cd

    @coupon_cd.setter
    def coupon_cd(self, coupon_cd):
        """Sets the coupon_cd of this CouponHistoryM.

        Coupon identification code.  # noqa: E501

        :param coupon_cd: The coupon_cd of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if coupon_cd is None:
            raise ValueError("Invalid value for `coupon_cd`, must not be `None`")  # noqa: E501

        self._coupon_cd = coupon_cd

    @property
    def coupon_create_date(self):
        """Gets the coupon_create_date of this CouponHistoryM.  # noqa: E501

        Date on which the coupon was added to the account.  # noqa: E501

        :return: The coupon_create_date of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._coupon_create_date

    @coupon_create_date.setter
    def coupon_create_date(self, coupon_create_date):
        """Sets the coupon_create_date of this CouponHistoryM.

        Date on which the coupon was added to the account.  # noqa: E501

        :param coupon_create_date: The coupon_create_date of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if coupon_create_date is None:
            raise ValueError("Invalid value for `coupon_create_date`, must not be `None`")  # noqa: E501

        self._coupon_create_date = coupon_create_date

    @property
    def coupon_status(self):
        """Gets the coupon_status of this CouponHistoryM.  # noqa: E501

        1 = Active/Not canceled. -1 = Canceled   # noqa: E501

        :return: The coupon_status of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._coupon_status

    @coupon_status.setter
    def coupon_status(self, coupon_status):
        """Sets the coupon_status of this CouponHistoryM.

        1 = Active/Not canceled. -1 = Canceled   # noqa: E501

        :param coupon_status: The coupon_status of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if coupon_status is None:
            raise ValueError("Invalid value for `coupon_status`, must not be `None`")  # noqa: E501

        self._coupon_status = coupon_status

    @property
    def coupon_cancel_date(self):
        """Gets the coupon_cancel_date of this CouponHistoryM.  # noqa: E501

        Date on which the coupon was canceled for the account (if applicable).   # noqa: E501

        :return: The coupon_cancel_date of this CouponHistoryM.  # noqa: E501
        :rtype: str
        """
        return self._coupon_cancel_date

    @coupon_cancel_date.setter
    def coupon_cancel_date(self, coupon_cancel_date):
        """Sets the coupon_cancel_date of this CouponHistoryM.

        Date on which the coupon was canceled for the account (if applicable).   # noqa: E501

        :param coupon_cancel_date: The coupon_cancel_date of this CouponHistoryM.  # noqa: E501
        :type: str
        """
        if coupon_cancel_date is None:
            raise ValueError("Invalid value for `coupon_cancel_date`, must not be `None`")  # noqa: E501

        self._coupon_cancel_date = coupon_cancel_date

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
        if not isinstance(other, CouponHistoryM):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
