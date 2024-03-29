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


class BackupPaymentMethodInfo(object):
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
        'bkup_billing_first_name': 'str',
        'bkup_billing_middle_initial': 'str',
        'bkup_billing_last_name': 'str',
        'bkup_billing_address1': 'str',
        'bkup_billing_address2': 'str',
        'bkup_billing_city': 'str',
        'bkup_billing_state': 'str',
        'bkup_billing_locality': 'str',
        'bkup_billing_zip': 'str',
        'bkup_billing_country': 'str',
        'bkup_billing_intl_phone': 'str',
        'bkup_billing_email': 'str',
        'bkup_pay_method_type': 'int',
        'bkup_cc_expire_mm': 'str',
        'bkup_cc_expire_yyyy': 'str',
        'bkup_bank_routing_num': 'str',
        'bkup_payment_instrument_suffix': 'str',
        'backup_payment_method_name': 'str',
        'backup_payment_method_description': 'str',
        'backup_payment_method_client_defined_id': 'str'
    }

    attribute_map = {
        'bkup_billing_first_name': 'bkup_billing_first_name',
        'bkup_billing_middle_initial': 'bkup_billing_middle_initial',
        'bkup_billing_last_name': 'bkup_billing_last_name',
        'bkup_billing_address1': 'bkup_billing_address1',
        'bkup_billing_address2': 'bkup_billing_address2',
        'bkup_billing_city': 'bkup_billing_city',
        'bkup_billing_state': 'bkup_billing_state',
        'bkup_billing_locality': 'bkup_billing_locality',
        'bkup_billing_zip': 'bkup_billing_zip',
        'bkup_billing_country': 'bkup_billing_country',
        'bkup_billing_intl_phone': 'bkup_billing_intl_phone',
        'bkup_billing_email': 'bkup_billing_email',
        'bkup_pay_method_type': 'bkup_pay_method_type',
        'bkup_cc_expire_mm': 'bkup_cc_expire_mm',
        'bkup_cc_expire_yyyy': 'bkup_cc_expire_yyyy',
        'bkup_bank_routing_num': 'bkup_bank_routing_num',
        'bkup_payment_instrument_suffix': 'bkup_payment_instrument_suffix',
        'backup_payment_method_name': 'backup_payment_method_name',
        'backup_payment_method_description': 'backup_payment_method_description',
        'backup_payment_method_client_defined_id': 'backup_payment_method_client_defined_id'
    }

    def __init__(self, bkup_billing_first_name=None, bkup_billing_middle_initial=None, bkup_billing_last_name=None, bkup_billing_address1=None, bkup_billing_address2=None, bkup_billing_city=None, bkup_billing_state=None, bkup_billing_locality=None, bkup_billing_zip=None, bkup_billing_country=None, bkup_billing_intl_phone=None, bkup_billing_email=None, bkup_pay_method_type=None, bkup_cc_expire_mm=None, bkup_cc_expire_yyyy=None, bkup_bank_routing_num=None, bkup_payment_instrument_suffix=None, backup_payment_method_name=None, backup_payment_method_description=None, backup_payment_method_client_defined_id=None):  # noqa: E501
        """BackupPaymentMethodInfo - a model defined in Swagger"""  # noqa: E501

        self._bkup_billing_first_name = None
        self._bkup_billing_middle_initial = None
        self._bkup_billing_last_name = None
        self._bkup_billing_address1 = None
        self._bkup_billing_address2 = None
        self._bkup_billing_city = None
        self._bkup_billing_state = None
        self._bkup_billing_locality = None
        self._bkup_billing_zip = None
        self._bkup_billing_country = None
        self._bkup_billing_intl_phone = None
        self._bkup_billing_email = None
        self._bkup_pay_method_type = None
        self._bkup_cc_expire_mm = None
        self._bkup_cc_expire_yyyy = None
        self._bkup_bank_routing_num = None
        self._bkup_payment_instrument_suffix = None
        self._backup_payment_method_name = None
        self._backup_payment_method_description = None
        self._backup_payment_method_client_defined_id = None
        self.discriminator = None

        if bkup_billing_first_name is not None:
            self.bkup_billing_first_name = bkup_billing_first_name
        if bkup_billing_middle_initial is not None:
            self.bkup_billing_middle_initial = bkup_billing_middle_initial
        if bkup_billing_last_name is not None:
            self.bkup_billing_last_name = bkup_billing_last_name
        if bkup_billing_address1 is not None:
            self.bkup_billing_address1 = bkup_billing_address1
        if bkup_billing_address2 is not None:
            self.bkup_billing_address2 = bkup_billing_address2
        if bkup_billing_city is not None:
            self.bkup_billing_city = bkup_billing_city
        if bkup_billing_state is not None:
            self.bkup_billing_state = bkup_billing_state
        if bkup_billing_locality is not None:
            self.bkup_billing_locality = bkup_billing_locality
        if bkup_billing_zip is not None:
            self.bkup_billing_zip = bkup_billing_zip
        if bkup_billing_country is not None:
            self.bkup_billing_country = bkup_billing_country
        if bkup_billing_intl_phone is not None:
            self.bkup_billing_intl_phone = bkup_billing_intl_phone
        if bkup_billing_email is not None:
            self.bkup_billing_email = bkup_billing_email
        if bkup_pay_method_type is not None:
            self.bkup_pay_method_type = bkup_pay_method_type
        if bkup_cc_expire_mm is not None:
            self.bkup_cc_expire_mm = bkup_cc_expire_mm
        if bkup_cc_expire_yyyy is not None:
            self.bkup_cc_expire_yyyy = bkup_cc_expire_yyyy
        if bkup_bank_routing_num is not None:
            self.bkup_bank_routing_num = bkup_bank_routing_num
        if bkup_payment_instrument_suffix is not None:
            self.bkup_payment_instrument_suffix = bkup_payment_instrument_suffix
        if backup_payment_method_name is not None:
            self.backup_payment_method_name = backup_payment_method_name
        if backup_payment_method_description is not None:
            self.backup_payment_method_description = backup_payment_method_description
        if backup_payment_method_client_defined_id is not None:
            self.backup_payment_method_client_defined_id = backup_payment_method_client_defined_id

    @property
    def bkup_billing_first_name(self):
        """Gets the bkup_billing_first_name of this BackupPaymentMethodInfo.  # noqa: E501

        First name from the current address instance  # noqa: E501

        :return: The bkup_billing_first_name of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_first_name

    @bkup_billing_first_name.setter
    def bkup_billing_first_name(self, bkup_billing_first_name):
        """Sets the bkup_billing_first_name of this BackupPaymentMethodInfo.

        First name from the current address instance  # noqa: E501

        :param bkup_billing_first_name: The bkup_billing_first_name of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_first_name = bkup_billing_first_name

    @property
    def bkup_billing_middle_initial(self):
        """Gets the bkup_billing_middle_initial of this BackupPaymentMethodInfo.  # noqa: E501

        Middle name from the current address instance  # noqa: E501

        :return: The bkup_billing_middle_initial of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_middle_initial

    @bkup_billing_middle_initial.setter
    def bkup_billing_middle_initial(self, bkup_billing_middle_initial):
        """Sets the bkup_billing_middle_initial of this BackupPaymentMethodInfo.

        Middle name from the current address instance  # noqa: E501

        :param bkup_billing_middle_initial: The bkup_billing_middle_initial of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_middle_initial = bkup_billing_middle_initial

    @property
    def bkup_billing_last_name(self):
        """Gets the bkup_billing_last_name of this BackupPaymentMethodInfo.  # noqa: E501

        Last name from the current address instance  # noqa: E501

        :return: The bkup_billing_last_name of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_last_name

    @bkup_billing_last_name.setter
    def bkup_billing_last_name(self, bkup_billing_last_name):
        """Sets the bkup_billing_last_name of this BackupPaymentMethodInfo.

        Last name from the current address instance  # noqa: E501

        :param bkup_billing_last_name: The bkup_billing_last_name of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_last_name = bkup_billing_last_name

    @property
    def bkup_billing_address1(self):
        """Gets the bkup_billing_address1 of this BackupPaymentMethodInfo.  # noqa: E501

        BillingAddress1 from the current address instance  # noqa: E501

        :return: The bkup_billing_address1 of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_address1

    @bkup_billing_address1.setter
    def bkup_billing_address1(self, bkup_billing_address1):
        """Sets the bkup_billing_address1 of this BackupPaymentMethodInfo.

        BillingAddress1 from the current address instance  # noqa: E501

        :param bkup_billing_address1: The bkup_billing_address1 of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_address1 = bkup_billing_address1

    @property
    def bkup_billing_address2(self):
        """Gets the bkup_billing_address2 of this BackupPaymentMethodInfo.  # noqa: E501

        BillingAddress2 from the current address instance  # noqa: E501

        :return: The bkup_billing_address2 of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_address2

    @bkup_billing_address2.setter
    def bkup_billing_address2(self, bkup_billing_address2):
        """Sets the bkup_billing_address2 of this BackupPaymentMethodInfo.

        BillingAddress2 from the current address instance  # noqa: E501

        :param bkup_billing_address2: The bkup_billing_address2 of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_address2 = bkup_billing_address2

    @property
    def bkup_billing_city(self):
        """Gets the bkup_billing_city of this BackupPaymentMethodInfo.  # noqa: E501

        City from the current address instance  # noqa: E501

        :return: The bkup_billing_city of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_city

    @bkup_billing_city.setter
    def bkup_billing_city(self, bkup_billing_city):
        """Sets the bkup_billing_city of this BackupPaymentMethodInfo.

        City from the current address instance  # noqa: E501

        :param bkup_billing_city: The bkup_billing_city of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_city = bkup_billing_city

    @property
    def bkup_billing_state(self):
        """Gets the bkup_billing_state of this BackupPaymentMethodInfo.  # noqa: E501

        State from the current address instance  # noqa: E501

        :return: The bkup_billing_state of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_state

    @bkup_billing_state.setter
    def bkup_billing_state(self, bkup_billing_state):
        """Sets the bkup_billing_state of this BackupPaymentMethodInfo.

        State from the current address instance  # noqa: E501

        :param bkup_billing_state: The bkup_billing_state of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_state = bkup_billing_state

    @property
    def bkup_billing_locality(self):
        """Gets the bkup_billing_locality of this BackupPaymentMethodInfo.  # noqa: E501

        Locality from the current address instance  # noqa: E501

        :return: The bkup_billing_locality of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_locality

    @bkup_billing_locality.setter
    def bkup_billing_locality(self, bkup_billing_locality):
        """Sets the bkup_billing_locality of this BackupPaymentMethodInfo.

        Locality from the current address instance  # noqa: E501

        :param bkup_billing_locality: The bkup_billing_locality of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_locality = bkup_billing_locality

    @property
    def bkup_billing_zip(self):
        """Gets the bkup_billing_zip of this BackupPaymentMethodInfo.  # noqa: E501

        Zipcode from the current address instance  # noqa: E501

        :return: The bkup_billing_zip of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_zip

    @bkup_billing_zip.setter
    def bkup_billing_zip(self, bkup_billing_zip):
        """Sets the bkup_billing_zip of this BackupPaymentMethodInfo.

        Zipcode from the current address instance  # noqa: E501

        :param bkup_billing_zip: The bkup_billing_zip of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_zip = bkup_billing_zip

    @property
    def bkup_billing_country(self):
        """Gets the bkup_billing_country of this BackupPaymentMethodInfo.  # noqa: E501

        Country from the current address instance  # noqa: E501

        :return: The bkup_billing_country of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_country

    @bkup_billing_country.setter
    def bkup_billing_country(self, bkup_billing_country):
        """Sets the bkup_billing_country of this BackupPaymentMethodInfo.

        Country from the current address instance  # noqa: E501

        :param bkup_billing_country: The bkup_billing_country of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_country = bkup_billing_country

    @property
    def bkup_billing_intl_phone(self):
        """Gets the bkup_billing_intl_phone of this BackupPaymentMethodInfo.  # noqa: E501

        Intl phone from the current address instance  # noqa: E501

        :return: The bkup_billing_intl_phone of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_intl_phone

    @bkup_billing_intl_phone.setter
    def bkup_billing_intl_phone(self, bkup_billing_intl_phone):
        """Sets the bkup_billing_intl_phone of this BackupPaymentMethodInfo.

        Intl phone from the current address instance  # noqa: E501

        :param bkup_billing_intl_phone: The bkup_billing_intl_phone of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_intl_phone = bkup_billing_intl_phone

    @property
    def bkup_billing_email(self):
        """Gets the bkup_billing_email of this BackupPaymentMethodInfo.  # noqa: E501

        Email from the current address instance  # noqa: E501

        :return: The bkup_billing_email of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_billing_email

    @bkup_billing_email.setter
    def bkup_billing_email(self, bkup_billing_email):
        """Sets the bkup_billing_email of this BackupPaymentMethodInfo.

        Email from the current address instance  # noqa: E501

        :param bkup_billing_email: The bkup_billing_email of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_billing_email = bkup_billing_email

    @property
    def bkup_pay_method_type(self):
        """Gets the bkup_pay_method_type of this BackupPaymentMethodInfo.  # noqa: E501

        pay type from the current billing instance  # noqa: E501

        :return: The bkup_pay_method_type of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: int
        """
        return self._bkup_pay_method_type

    @bkup_pay_method_type.setter
    def bkup_pay_method_type(self, bkup_pay_method_type):
        """Sets the bkup_pay_method_type of this BackupPaymentMethodInfo.

        pay type from the current billing instance  # noqa: E501

        :param bkup_pay_method_type: The bkup_pay_method_type of this BackupPaymentMethodInfo.  # noqa: E501
        :type: int
        """

        self._bkup_pay_method_type = bkup_pay_method_type

    @property
    def bkup_cc_expire_mm(self):
        """Gets the bkup_cc_expire_mm of this BackupPaymentMethodInfo.  # noqa: E501

        cc expire months from the current billing instance  # noqa: E501

        :return: The bkup_cc_expire_mm of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_cc_expire_mm

    @bkup_cc_expire_mm.setter
    def bkup_cc_expire_mm(self, bkup_cc_expire_mm):
        """Sets the bkup_cc_expire_mm of this BackupPaymentMethodInfo.

        cc expire months from the current billing instance  # noqa: E501

        :param bkup_cc_expire_mm: The bkup_cc_expire_mm of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_cc_expire_mm = bkup_cc_expire_mm

    @property
    def bkup_cc_expire_yyyy(self):
        """Gets the bkup_cc_expire_yyyy of this BackupPaymentMethodInfo.  # noqa: E501

        cc expire year from the current billing instance  # noqa: E501

        :return: The bkup_cc_expire_yyyy of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_cc_expire_yyyy

    @bkup_cc_expire_yyyy.setter
    def bkup_cc_expire_yyyy(self, bkup_cc_expire_yyyy):
        """Sets the bkup_cc_expire_yyyy of this BackupPaymentMethodInfo.

        cc expire year from the current billing instance  # noqa: E501

        :param bkup_cc_expire_yyyy: The bkup_cc_expire_yyyy of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_cc_expire_yyyy = bkup_cc_expire_yyyy

    @property
    def bkup_bank_routing_num(self):
        """Gets the bkup_bank_routing_num of this BackupPaymentMethodInfo.  # noqa: E501

        bank routing num from the current billing instance  # noqa: E501

        :return: The bkup_bank_routing_num of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_bank_routing_num

    @bkup_bank_routing_num.setter
    def bkup_bank_routing_num(self, bkup_bank_routing_num):
        """Sets the bkup_bank_routing_num of this BackupPaymentMethodInfo.

        bank routing num from the current billing instance  # noqa: E501

        :param bkup_bank_routing_num: The bkup_bank_routing_num of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_bank_routing_num = bkup_bank_routing_num

    @property
    def bkup_payment_instrument_suffix(self):
        """Gets the bkup_payment_instrument_suffix of this BackupPaymentMethodInfo.  # noqa: E501

        suffix from the current billing instance  # noqa: E501

        :return: The bkup_payment_instrument_suffix of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._bkup_payment_instrument_suffix

    @bkup_payment_instrument_suffix.setter
    def bkup_payment_instrument_suffix(self, bkup_payment_instrument_suffix):
        """Sets the bkup_payment_instrument_suffix of this BackupPaymentMethodInfo.

        suffix from the current billing instance  # noqa: E501

        :param bkup_payment_instrument_suffix: The bkup_payment_instrument_suffix of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._bkup_payment_instrument_suffix = bkup_payment_instrument_suffix

    @property
    def backup_payment_method_name(self):
        """Gets the backup_payment_method_name of this BackupPaymentMethodInfo.  # noqa: E501

        Primary payment method name from the current billing instance  # noqa: E501

        :return: The backup_payment_method_name of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._backup_payment_method_name

    @backup_payment_method_name.setter
    def backup_payment_method_name(self, backup_payment_method_name):
        """Sets the backup_payment_method_name of this BackupPaymentMethodInfo.

        Primary payment method name from the current billing instance  # noqa: E501

        :param backup_payment_method_name: The backup_payment_method_name of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._backup_payment_method_name = backup_payment_method_name

    @property
    def backup_payment_method_description(self):
        """Gets the backup_payment_method_description of this BackupPaymentMethodInfo.  # noqa: E501

        primary payment method description from the current billing instance  # noqa: E501

        :return: The backup_payment_method_description of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._backup_payment_method_description

    @backup_payment_method_description.setter
    def backup_payment_method_description(self, backup_payment_method_description):
        """Sets the backup_payment_method_description of this BackupPaymentMethodInfo.

        primary payment method description from the current billing instance  # noqa: E501

        :param backup_payment_method_description: The backup_payment_method_description of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._backup_payment_method_description = backup_payment_method_description

    @property
    def backup_payment_method_client_defined_id(self):
        """Gets the backup_payment_method_client_defined_id of this BackupPaymentMethodInfo.  # noqa: E501

        Primary payment client defined id from the current billing instance  # noqa: E501

        :return: The backup_payment_method_client_defined_id of this BackupPaymentMethodInfo.  # noqa: E501
        :rtype: str
        """
        return self._backup_payment_method_client_defined_id

    @backup_payment_method_client_defined_id.setter
    def backup_payment_method_client_defined_id(self, backup_payment_method_client_defined_id):
        """Sets the backup_payment_method_client_defined_id of this BackupPaymentMethodInfo.

        Primary payment client defined id from the current billing instance  # noqa: E501

        :param backup_payment_method_client_defined_id: The backup_payment_method_client_defined_id of this BackupPaymentMethodInfo.  # noqa: E501
        :type: str
        """

        self._backup_payment_method_client_defined_id = backup_payment_method_client_defined_id

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
        if not isinstance(other, BackupPaymentMethodInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
