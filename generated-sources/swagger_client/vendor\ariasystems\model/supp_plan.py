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

from swagger_client.vendor\ariasystems\model.supp_plan_plan_inst_field import SuppPlanPlanInstField  # noqa: F401,E501


class SuppPlan(object):
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
        'supp_plan_instance_no': 'str',
        'client_supp_plan_instance_id': 'str',
        'client_supp_plan_id': 'str',
        'supp_plan_no': 'str',
        'supp_plan_instance_description': 'str',
        'supp_plan_instance_status': 'str',
        'parent_plan_instance_no': 'str',
        'client_parent_plan_instance_id': 'str',
        'po_num': 'str',
        'supp_plan_plan_inst_fields': 'list[SuppPlanPlanInstField]'
    }

    attribute_map = {
        'supp_plan_instance_no': 'supp_plan_instance_no',
        'client_supp_plan_instance_id': 'client_supp_plan_instance_id',
        'client_supp_plan_id': 'client_supp_plan_id',
        'supp_plan_no': 'supp_plan_no',
        'supp_plan_instance_description': 'supp_plan_instance_description',
        'supp_plan_instance_status': 'supp_plan_instance_status',
        'parent_plan_instance_no': 'parent_plan_instance_no',
        'client_parent_plan_instance_id': 'client_parent_plan_instance_id',
        'po_num': 'po_num',
        'supp_plan_plan_inst_fields': 'supp_plan_plan_inst_fields'
    }

    def __init__(self, supp_plan_instance_no=None, client_supp_plan_instance_id=None, client_supp_plan_id=None, supp_plan_no=None, supp_plan_instance_description=None, supp_plan_instance_status=None, parent_plan_instance_no=None, client_parent_plan_instance_id=None, po_num=None, supp_plan_plan_inst_fields=None):  # noqa: E501
        """SuppPlan - a model defined in Swagger"""  # noqa: E501

        self._supp_plan_instance_no = None
        self._client_supp_plan_instance_id = None
        self._client_supp_plan_id = None
        self._supp_plan_no = None
        self._supp_plan_instance_description = None
        self._supp_plan_instance_status = None
        self._parent_plan_instance_no = None
        self._client_parent_plan_instance_id = None
        self._po_num = None
        self._supp_plan_plan_inst_fields = None
        self.discriminator = None

        if supp_plan_instance_no is not None:
            self.supp_plan_instance_no = supp_plan_instance_no
        if client_supp_plan_instance_id is not None:
            self.client_supp_plan_instance_id = client_supp_plan_instance_id
        if client_supp_plan_id is not None:
            self.client_supp_plan_id = client_supp_plan_id
        if supp_plan_no is not None:
            self.supp_plan_no = supp_plan_no
        if supp_plan_instance_description is not None:
            self.supp_plan_instance_description = supp_plan_instance_description
        if supp_plan_instance_status is not None:
            self.supp_plan_instance_status = supp_plan_instance_status
        if parent_plan_instance_no is not None:
            self.parent_plan_instance_no = parent_plan_instance_no
        if client_parent_plan_instance_id is not None:
            self.client_parent_plan_instance_id = client_parent_plan_instance_id
        if po_num is not None:
            self.po_num = po_num
        if supp_plan_plan_inst_fields is not None:
            self.supp_plan_plan_inst_fields = supp_plan_plan_inst_fields

    @property
    def supp_plan_instance_no(self):
        """Gets the supp_plan_instance_no of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The supp_plan_instance_no of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._supp_plan_instance_no

    @supp_plan_instance_no.setter
    def supp_plan_instance_no(self, supp_plan_instance_no):
        """Sets the supp_plan_instance_no of this SuppPlan.

          # noqa: E501

        :param supp_plan_instance_no: The supp_plan_instance_no of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._supp_plan_instance_no = supp_plan_instance_no

    @property
    def client_supp_plan_instance_id(self):
        """Gets the client_supp_plan_instance_id of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The client_supp_plan_instance_id of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._client_supp_plan_instance_id

    @client_supp_plan_instance_id.setter
    def client_supp_plan_instance_id(self, client_supp_plan_instance_id):
        """Sets the client_supp_plan_instance_id of this SuppPlan.

          # noqa: E501

        :param client_supp_plan_instance_id: The client_supp_plan_instance_id of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._client_supp_plan_instance_id = client_supp_plan_instance_id

    @property
    def client_supp_plan_id(self):
        """Gets the client_supp_plan_id of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The client_supp_plan_id of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._client_supp_plan_id

    @client_supp_plan_id.setter
    def client_supp_plan_id(self, client_supp_plan_id):
        """Sets the client_supp_plan_id of this SuppPlan.

          # noqa: E501

        :param client_supp_plan_id: The client_supp_plan_id of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._client_supp_plan_id = client_supp_plan_id

    @property
    def supp_plan_no(self):
        """Gets the supp_plan_no of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The supp_plan_no of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._supp_plan_no

    @supp_plan_no.setter
    def supp_plan_no(self, supp_plan_no):
        """Sets the supp_plan_no of this SuppPlan.

          # noqa: E501

        :param supp_plan_no: The supp_plan_no of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._supp_plan_no = supp_plan_no

    @property
    def supp_plan_instance_description(self):
        """Gets the supp_plan_instance_description of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The supp_plan_instance_description of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._supp_plan_instance_description

    @supp_plan_instance_description.setter
    def supp_plan_instance_description(self, supp_plan_instance_description):
        """Sets the supp_plan_instance_description of this SuppPlan.

          # noqa: E501

        :param supp_plan_instance_description: The supp_plan_instance_description of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._supp_plan_instance_description = supp_plan_instance_description

    @property
    def supp_plan_instance_status(self):
        """Gets the supp_plan_instance_status of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The supp_plan_instance_status of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._supp_plan_instance_status

    @supp_plan_instance_status.setter
    def supp_plan_instance_status(self, supp_plan_instance_status):
        """Sets the supp_plan_instance_status of this SuppPlan.

          # noqa: E501

        :param supp_plan_instance_status: The supp_plan_instance_status of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._supp_plan_instance_status = supp_plan_instance_status

    @property
    def parent_plan_instance_no(self):
        """Gets the parent_plan_instance_no of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The parent_plan_instance_no of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._parent_plan_instance_no

    @parent_plan_instance_no.setter
    def parent_plan_instance_no(self, parent_plan_instance_no):
        """Sets the parent_plan_instance_no of this SuppPlan.

          # noqa: E501

        :param parent_plan_instance_no: The parent_plan_instance_no of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._parent_plan_instance_no = parent_plan_instance_no

    @property
    def client_parent_plan_instance_id(self):
        """Gets the client_parent_plan_instance_id of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The client_parent_plan_instance_id of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._client_parent_plan_instance_id

    @client_parent_plan_instance_id.setter
    def client_parent_plan_instance_id(self, client_parent_plan_instance_id):
        """Sets the client_parent_plan_instance_id of this SuppPlan.

          # noqa: E501

        :param client_parent_plan_instance_id: The client_parent_plan_instance_id of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._client_parent_plan_instance_id = client_parent_plan_instance_id

    @property
    def po_num(self):
        """Gets the po_num of this SuppPlan.  # noqa: E501

        Purchase order number assigned to the account or plan instance.  # noqa: E501

        :return: The po_num of this SuppPlan.  # noqa: E501
        :rtype: str
        """
        return self._po_num

    @po_num.setter
    def po_num(self, po_num):
        """Sets the po_num of this SuppPlan.

        Purchase order number assigned to the account or plan instance.  # noqa: E501

        :param po_num: The po_num of this SuppPlan.  # noqa: E501
        :type: str
        """

        self._po_num = po_num

    @property
    def supp_plan_plan_inst_fields(self):
        """Gets the supp_plan_plan_inst_fields of this SuppPlan.  # noqa: E501

          # noqa: E501

        :return: The supp_plan_plan_inst_fields of this SuppPlan.  # noqa: E501
        :rtype: list[SuppPlanPlanInstField]
        """
        return self._supp_plan_plan_inst_fields

    @supp_plan_plan_inst_fields.setter
    def supp_plan_plan_inst_fields(self, supp_plan_plan_inst_fields):
        """Sets the supp_plan_plan_inst_fields of this SuppPlan.

          # noqa: E501

        :param supp_plan_plan_inst_fields: The supp_plan_plan_inst_fields of this SuppPlan.  # noqa: E501
        :type: list[SuppPlanPlanInstField]
        """

        self._supp_plan_plan_inst_fields = supp_plan_plan_inst_fields

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
        if not isinstance(other, SuppPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
