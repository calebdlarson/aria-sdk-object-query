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


class RelatedTransaction(object):
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
        'aria_event_no': 'int',
        'transaction_date': 'str',
        'transaction_type': 'str',
        'transaction_type_no': 'int',
        'is_charge_type': 'int',
        'type_specific_id': 'int',
        'acct_no': 'int',
        'amount': 'float',
        'currency_cd': 'str',
        'aria_statement_no': 'int',
        'total_amount_applied': 'float',
        'related_amount_applied': 'float',
        'update_date': 'str',
        'void_date': 'str',
        'fully_applied_date': 'str',
        'master_plan_instance_no': 'int',
        'related_amount': 'float'
    }

    attribute_map = {
        'aria_event_no': 'aria_event_no',
        'transaction_date': 'transaction_date',
        'transaction_type': 'transaction_type',
        'transaction_type_no': 'transaction_type_no',
        'is_charge_type': 'is_charge_type',
        'type_specific_id': 'type_specific_id',
        'acct_no': 'acct_no',
        'amount': 'amount',
        'currency_cd': 'currency_cd',
        'aria_statement_no': 'aria_statement_no',
        'total_amount_applied': 'total_amount_applied',
        'related_amount_applied': 'related_amount_applied',
        'update_date': 'update_date',
        'void_date': 'void_date',
        'fully_applied_date': 'fully_applied_date',
        'master_plan_instance_no': 'master_plan_instance_no',
        'related_amount': 'related_amount'
    }

    def __init__(self, aria_event_no=None, transaction_date=None, transaction_type=None, transaction_type_no=None, is_charge_type=None, type_specific_id=None, acct_no=None, amount=None, currency_cd=None, aria_statement_no=None, total_amount_applied=None, related_amount_applied=None, update_date=None, void_date=None, fully_applied_date=None, master_plan_instance_no=None, related_amount=None):  # noqa: E501
        """RelatedTransaction - a model defined in Swagger"""  # noqa: E501

        self._aria_event_no = None
        self._transaction_date = None
        self._transaction_type = None
        self._transaction_type_no = None
        self._is_charge_type = None
        self._type_specific_id = None
        self._acct_no = None
        self._amount = None
        self._currency_cd = None
        self._aria_statement_no = None
        self._total_amount_applied = None
        self._related_amount_applied = None
        self._update_date = None
        self._void_date = None
        self._fully_applied_date = None
        self._master_plan_instance_no = None
        self._related_amount = None
        self.discriminator = None

        self.aria_event_no = aria_event_no
        self.transaction_date = transaction_date
        if transaction_type is not None:
            self.transaction_type = transaction_type
        self.transaction_type_no = transaction_type_no
        if is_charge_type is not None:
            self.is_charge_type = is_charge_type
        if type_specific_id is not None:
            self.type_specific_id = type_specific_id
        self.acct_no = acct_no
        if amount is not None:
            self.amount = amount
        if currency_cd is not None:
            self.currency_cd = currency_cd
        if aria_statement_no is not None:
            self.aria_statement_no = aria_statement_no
        if total_amount_applied is not None:
            self.total_amount_applied = total_amount_applied
        if related_amount_applied is not None:
            self.related_amount_applied = related_amount_applied
        self.update_date = update_date
        if void_date is not None:
            self.void_date = void_date
        self.fully_applied_date = fully_applied_date
        if master_plan_instance_no is not None:
            self.master_plan_instance_no = master_plan_instance_no
        if related_amount is not None:
            self.related_amount = related_amount

    @property
    def aria_event_no(self):
        """Gets the aria_event_no of this RelatedTransaction.  # noqa: E501

        The Aria assigned ID for the event.  # noqa: E501

        :return: The aria_event_no of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._aria_event_no

    @aria_event_no.setter
    def aria_event_no(self, aria_event_no):
        """Sets the aria_event_no of this RelatedTransaction.

        The Aria assigned ID for the event.  # noqa: E501

        :param aria_event_no: The aria_event_no of this RelatedTransaction.  # noqa: E501
        :type: int
        """
        if aria_event_no is None:
            raise ValueError("Invalid value for `aria_event_no`, must not be `None`")  # noqa: E501

        self._aria_event_no = aria_event_no

    @property
    def transaction_date(self):
        """Gets the transaction_date of this RelatedTransaction.  # noqa: E501

          # noqa: E501

        :return: The transaction_date of this RelatedTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this RelatedTransaction.

          # noqa: E501

        :param transaction_date: The transaction_date of this RelatedTransaction.  # noqa: E501
        :type: str
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def transaction_type(self):
        """Gets the transaction_type of this RelatedTransaction.  # noqa: E501

          # noqa: E501

        :return: The transaction_type of this RelatedTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this RelatedTransaction.

          # noqa: E501

        :param transaction_type: The transaction_type of this RelatedTransaction.  # noqa: E501
        :type: str
        """

        self._transaction_type = transaction_type

    @property
    def transaction_type_no(self):
        """Gets the transaction_type_no of this RelatedTransaction.  # noqa: E501

          # noqa: E501

        :return: The transaction_type_no of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._transaction_type_no

    @transaction_type_no.setter
    def transaction_type_no(self, transaction_type_no):
        """Sets the transaction_type_no of this RelatedTransaction.

          # noqa: E501

        :param transaction_type_no: The transaction_type_no of this RelatedTransaction.  # noqa: E501
        :type: int
        """
        if transaction_type_no is None:
            raise ValueError("Invalid value for `transaction_type_no`, must not be `None`")  # noqa: E501

        self._transaction_type_no = transaction_type_no

    @property
    def is_charge_type(self):
        """Gets the is_charge_type of this RelatedTransaction.  # noqa: E501

          # noqa: E501

        :return: The is_charge_type of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._is_charge_type

    @is_charge_type.setter
    def is_charge_type(self, is_charge_type):
        """Sets the is_charge_type of this RelatedTransaction.

          # noqa: E501

        :param is_charge_type: The is_charge_type of this RelatedTransaction.  # noqa: E501
        :type: int
        """

        self._is_charge_type = is_charge_type

    @property
    def type_specific_id(self):
        """Gets the type_specific_id of this RelatedTransaction.  # noqa: E501

        e.g. payment_id for electronic payments, invoice_no for invoices, etc   # noqa: E501

        :return: The type_specific_id of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._type_specific_id

    @type_specific_id.setter
    def type_specific_id(self, type_specific_id):
        """Sets the type_specific_id of this RelatedTransaction.

        e.g. payment_id for electronic payments, invoice_no for invoices, etc   # noqa: E501

        :param type_specific_id: The type_specific_id of this RelatedTransaction.  # noqa: E501
        :type: int
        """

        self._type_specific_id = type_specific_id

    @property
    def acct_no(self):
        """Gets the acct_no of this RelatedTransaction.  # noqa: E501

        The Aria assigned ID of the account.  # noqa: E501

        :return: The acct_no of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._acct_no

    @acct_no.setter
    def acct_no(self, acct_no):
        """Sets the acct_no of this RelatedTransaction.

        The Aria assigned ID of the account.  # noqa: E501

        :param acct_no: The acct_no of this RelatedTransaction.  # noqa: E501
        :type: int
        """
        if acct_no is None:
            raise ValueError("Invalid value for `acct_no`, must not be `None`")  # noqa: E501

        self._acct_no = acct_no

    @property
    def amount(self):
        """Gets the amount of this RelatedTransaction.  # noqa: E501

          # noqa: E501

        :return: The amount of this RelatedTransaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RelatedTransaction.

          # noqa: E501

        :param amount: The amount of this RelatedTransaction.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency_cd(self):
        """Gets the currency_cd of this RelatedTransaction.  # noqa: E501

          # noqa: E501

        :return: The currency_cd of this RelatedTransaction.  # noqa: E501
        :rtype: str
        """
        return self._currency_cd

    @currency_cd.setter
    def currency_cd(self, currency_cd):
        """Sets the currency_cd of this RelatedTransaction.

          # noqa: E501

        :param currency_cd: The currency_cd of this RelatedTransaction.  # noqa: E501
        :type: str
        """

        self._currency_cd = currency_cd

    @property
    def aria_statement_no(self):
        """Gets the aria_statement_no of this RelatedTransaction.  # noqa: E501

        Aria assigned ID of the statement related to this transaction   # noqa: E501

        :return: The aria_statement_no of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._aria_statement_no

    @aria_statement_no.setter
    def aria_statement_no(self, aria_statement_no):
        """Sets the aria_statement_no of this RelatedTransaction.

        Aria assigned ID of the statement related to this transaction   # noqa: E501

        :param aria_statement_no: The aria_statement_no of this RelatedTransaction.  # noqa: E501
        :type: int
        """

        self._aria_statement_no = aria_statement_no

    @property
    def total_amount_applied(self):
        """Gets the total_amount_applied of this RelatedTransaction.  # noqa: E501

        Total amount applied to any other transactions  # noqa: E501

        :return: The total_amount_applied of this RelatedTransaction.  # noqa: E501
        :rtype: float
        """
        return self._total_amount_applied

    @total_amount_applied.setter
    def total_amount_applied(self, total_amount_applied):
        """Sets the total_amount_applied of this RelatedTransaction.

        Total amount applied to any other transactions  # noqa: E501

        :param total_amount_applied: The total_amount_applied of this RelatedTransaction.  # noqa: E501
        :type: float
        """

        self._total_amount_applied = total_amount_applied

    @property
    def related_amount_applied(self):
        """Gets the related_amount_applied of this RelatedTransaction.  # noqa: E501

        Amount applied to this transaction  # noqa: E501

        :return: The related_amount_applied of this RelatedTransaction.  # noqa: E501
        :rtype: float
        """
        return self._related_amount_applied

    @related_amount_applied.setter
    def related_amount_applied(self, related_amount_applied):
        """Sets the related_amount_applied of this RelatedTransaction.

        Amount applied to this transaction  # noqa: E501

        :param related_amount_applied: The related_amount_applied of this RelatedTransaction.  # noqa: E501
        :type: float
        """

        self._related_amount_applied = related_amount_applied

    @property
    def update_date(self):
        """Gets the update_date of this RelatedTransaction.  # noqa: E501

        Date transaction was last updated.  # noqa: E501

        :return: The update_date of this RelatedTransaction.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this RelatedTransaction.

        Date transaction was last updated.  # noqa: E501

        :param update_date: The update_date of this RelatedTransaction.  # noqa: E501
        :type: str
        """
        if update_date is None:
            raise ValueError("Invalid value for `update_date`, must not be `None`")  # noqa: E501

        self._update_date = update_date

    @property
    def void_date(self):
        """Gets the void_date of this RelatedTransaction.  # noqa: E501

        Void date of related transactions associated with the specified event ID number. Example: Void date of a payment.   # noqa: E501

        :return: The void_date of this RelatedTransaction.  # noqa: E501
        :rtype: str
        """
        return self._void_date

    @void_date.setter
    def void_date(self, void_date):
        """Sets the void_date of this RelatedTransaction.

        Void date of related transactions associated with the specified event ID number. Example: Void date of a payment.   # noqa: E501

        :param void_date: The void_date of this RelatedTransaction.  # noqa: E501
        :type: str
        """

        self._void_date = void_date

    @property
    def fully_applied_date(self):
        """Gets the fully_applied_date of this RelatedTransaction.  # noqa: E501

        Date transaction was fully offset by another transaction  # noqa: E501

        :return: The fully_applied_date of this RelatedTransaction.  # noqa: E501
        :rtype: str
        """
        return self._fully_applied_date

    @fully_applied_date.setter
    def fully_applied_date(self, fully_applied_date):
        """Sets the fully_applied_date of this RelatedTransaction.

        Date transaction was fully offset by another transaction  # noqa: E501

        :param fully_applied_date: The fully_applied_date of this RelatedTransaction.  # noqa: E501
        :type: str
        """
        if fully_applied_date is None:
            raise ValueError("Invalid value for `fully_applied_date`, must not be `None`")  # noqa: E501

        self._fully_applied_date = fully_applied_date

    @property
    def master_plan_instance_no(self):
        """Gets the master_plan_instance_no of this RelatedTransaction.  # noqa: E501

        The Master Plan Instance assigned to the account  # noqa: E501

        :return: The master_plan_instance_no of this RelatedTransaction.  # noqa: E501
        :rtype: int
        """
        return self._master_plan_instance_no

    @master_plan_instance_no.setter
    def master_plan_instance_no(self, master_plan_instance_no):
        """Sets the master_plan_instance_no of this RelatedTransaction.

        The Master Plan Instance assigned to the account  # noqa: E501

        :param master_plan_instance_no: The master_plan_instance_no of this RelatedTransaction.  # noqa: E501
        :type: int
        """

        self._master_plan_instance_no = master_plan_instance_no

    @property
    def related_amount(self):
        """Gets the related_amount of this RelatedTransaction.  # noqa: E501

        Amount applied to this transaction. Duplicate of related_amount_applied.  # noqa: E501

        :return: The related_amount of this RelatedTransaction.  # noqa: E501
        :rtype: float
        """
        return self._related_amount

    @related_amount.setter
    def related_amount(self, related_amount):
        """Sets the related_amount of this RelatedTransaction.

        Amount applied to this transaction. Duplicate of related_amount_applied.  # noqa: E501

        :param related_amount: The related_amount of this RelatedTransaction.  # noqa: E501
        :type: float
        """

        self._related_amount = related_amount

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
        if not isinstance(other, RelatedTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
