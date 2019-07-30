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


class AccountStatusHistory(object):
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
        'acct_no': 'str',
        'user_id': 'str',
        'company_name': 'str',
        'client_1': 'str',
        'promo_cd': 'str',
        'account_creation_date': 'str',
        'plan_no': 'str',
        'new_status': 'str',
        'new_status_cd': 'int',
        'old_status': 'str',
        'old_status_cd': 'int',
        'change_date': 'str',
        'comments': 'str'
    }

    attribute_map = {
        'acct_no': 'acct_no',
        'user_id': 'user_id',
        'company_name': 'company_name',
        'client_1': 'client_1',
        'promo_cd': 'promo_cd',
        'account_creation_date': 'account_creation_date',
        'plan_no': 'plan_no',
        'new_status': 'new_status',
        'new_status_cd': 'new_status_cd',
        'old_status': 'old_status',
        'old_status_cd': 'old_status_cd',
        'change_date': 'change_date',
        'comments': 'comments'
    }

    def __init__(self, acct_no=None, user_id=None, company_name=None, client_1=None, promo_cd=None, account_creation_date=None, plan_no=None, new_status=None, new_status_cd=None, old_status=None, old_status_cd=None, change_date=None, comments=None):  # noqa: E501
        """AccountStatusHistory - a model defined in Swagger"""  # noqa: E501

        self._acct_no = None
        self._user_id = None
        self._company_name = None
        self._client_1 = None
        self._promo_cd = None
        self._account_creation_date = None
        self._plan_no = None
        self._new_status = None
        self._new_status_cd = None
        self._old_status = None
        self._old_status_cd = None
        self._change_date = None
        self._comments = None
        self.discriminator = None

        self.acct_no = acct_no
        if user_id is not None:
            self.user_id = user_id
        if company_name is not None:
            self.company_name = company_name
        if client_1 is not None:
            self.client_1 = client_1
        if promo_cd is not None:
            self.promo_cd = promo_cd
        if account_creation_date is not None:
            self.account_creation_date = account_creation_date
        self.plan_no = plan_no
        if new_status is not None:
            self.new_status = new_status
        if new_status_cd is not None:
            self.new_status_cd = new_status_cd
        if old_status is not None:
            self.old_status = old_status
        if old_status_cd is not None:
            self.old_status_cd = old_status_cd
        if change_date is not None:
            self.change_date = change_date
        if comments is not None:
            self.comments = comments

    @property
    def acct_no(self):
        """Gets the acct_no of this AccountStatusHistory.  # noqa: E501

        The Aria assigned ID of the account  # noqa: E501

        :return: The acct_no of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._acct_no

    @acct_no.setter
    def acct_no(self, acct_no):
        """Sets the acct_no of this AccountStatusHistory.

        The Aria assigned ID of the account  # noqa: E501

        :param acct_no: The acct_no of this AccountStatusHistory.  # noqa: E501
        :type: str
        """
        if acct_no is None:
            raise ValueError("Invalid value for `acct_no`, must not be `None`")  # noqa: E501

        self._acct_no = acct_no

    @property
    def user_id(self):
        """Gets the user_id of this AccountStatusHistory.  # noqa: E501

        The client defined user_id for the account  # noqa: E501

        :return: The user_id of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccountStatusHistory.

        The client defined user_id for the account  # noqa: E501

        :param user_id: The user_id of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def company_name(self):
        """Gets the company_name of this AccountStatusHistory.  # noqa: E501

          # noqa: E501

        :return: The company_name of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this AccountStatusHistory.

          # noqa: E501

        :param company_name: The company_name of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def client_1(self):
        """Gets the client_1 of this AccountStatusHistory.  # noqa: E501

        Client defined field  # noqa: E501

        :return: The client_1 of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._client_1

    @client_1.setter
    def client_1(self, client_1):
        """Sets the client_1 of this AccountStatusHistory.

        Client defined field  # noqa: E501

        :param client_1: The client_1 of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._client_1 = client_1

    @property
    def promo_cd(self):
        """Gets the promo_cd of this AccountStatusHistory.  # noqa: E501

        Promotion code used for the account  # noqa: E501

        :return: The promo_cd of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._promo_cd

    @promo_cd.setter
    def promo_cd(self, promo_cd):
        """Sets the promo_cd of this AccountStatusHistory.

        Promotion code used for the account  # noqa: E501

        :param promo_cd: The promo_cd of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._promo_cd = promo_cd

    @property
    def account_creation_date(self):
        """Gets the account_creation_date of this AccountStatusHistory.  # noqa: E501

          # noqa: E501

        :return: The account_creation_date of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._account_creation_date

    @account_creation_date.setter
    def account_creation_date(self, account_creation_date):
        """Sets the account_creation_date of this AccountStatusHistory.

          # noqa: E501

        :param account_creation_date: The account_creation_date of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._account_creation_date = account_creation_date

    @property
    def plan_no(self):
        """Gets the plan_no of this AccountStatusHistory.  # noqa: E501

        Account's master plan number  # noqa: E501

        :return: The plan_no of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._plan_no

    @plan_no.setter
    def plan_no(self, plan_no):
        """Sets the plan_no of this AccountStatusHistory.

        Account's master plan number  # noqa: E501

        :param plan_no: The plan_no of this AccountStatusHistory.  # noqa: E501
        :type: str
        """
        if plan_no is None:
            raise ValueError("Invalid value for `plan_no`, must not be `None`")  # noqa: E501

        self._plan_no = plan_no

    @property
    def new_status(self):
        """Gets the new_status of this AccountStatusHistory.  # noqa: E501

        Name of the new status  # noqa: E501

        :return: The new_status of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._new_status

    @new_status.setter
    def new_status(self, new_status):
        """Sets the new_status of this AccountStatusHistory.

        Name of the new status  # noqa: E501

        :param new_status: The new_status of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._new_status = new_status

    @property
    def new_status_cd(self):
        """Gets the new_status_cd of this AccountStatusHistory.  # noqa: E501

          # noqa: E501

        :return: The new_status_cd of this AccountStatusHistory.  # noqa: E501
        :rtype: int
        """
        return self._new_status_cd

    @new_status_cd.setter
    def new_status_cd(self, new_status_cd):
        """Sets the new_status_cd of this AccountStatusHistory.

          # noqa: E501

        :param new_status_cd: The new_status_cd of this AccountStatusHistory.  # noqa: E501
        :type: int
        """

        self._new_status_cd = new_status_cd

    @property
    def old_status(self):
        """Gets the old_status of this AccountStatusHistory.  # noqa: E501

        Name of the old status  # noqa: E501

        :return: The old_status of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._old_status

    @old_status.setter
    def old_status(self, old_status):
        """Sets the old_status of this AccountStatusHistory.

        Name of the old status  # noqa: E501

        :param old_status: The old_status of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._old_status = old_status

    @property
    def old_status_cd(self):
        """Gets the old_status_cd of this AccountStatusHistory.  # noqa: E501

          # noqa: E501

        :return: The old_status_cd of this AccountStatusHistory.  # noqa: E501
        :rtype: int
        """
        return self._old_status_cd

    @old_status_cd.setter
    def old_status_cd(self, old_status_cd):
        """Sets the old_status_cd of this AccountStatusHistory.

          # noqa: E501

        :param old_status_cd: The old_status_cd of this AccountStatusHistory.  # noqa: E501
        :type: int
        """

        self._old_status_cd = old_status_cd

    @property
    def change_date(self):
        """Gets the change_date of this AccountStatusHistory.  # noqa: E501

          # noqa: E501

        :return: The change_date of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """Sets the change_date of this AccountStatusHistory.

          # noqa: E501

        :param change_date: The change_date of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._change_date = change_date

    @property
    def comments(self):
        """Gets the comments of this AccountStatusHistory.  # noqa: E501

          # noqa: E501

        :return: The comments of this AccountStatusHistory.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AccountStatusHistory.

          # noqa: E501

        :param comments: The comments of this AccountStatusHistory.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if not isinstance(other, AccountStatusHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
