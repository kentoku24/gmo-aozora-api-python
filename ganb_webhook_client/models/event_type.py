# coding: utf-8

"""
    GMO Aozora Net Bank Open API

    <p>Ph2.5向けに作成したもの</p>   # noqa: E501

    OpenAPI spec version: 1.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EventType(object):
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
        'event_type': 'str'
    }

    attribute_map = {
        'event_type': 'eventType'
    }

    def __init__(self, event_type=None):  # noqa: E501
        """EventType - a model defined in Swagger"""  # noqa: E501

        self._event_type = None
        self.discriminator = None

        self.event_type = event_type

    @property
    def event_type(self):
        """Gets the event_type of this EventType.  # noqa: E501

        イベント種別 半角英数記号文字 va-deposit-transaction = 振込入金口座への入金明細通知   # noqa: E501

        :return: The event_type of this EventType.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventType.

        イベント種別 半角英数記号文字 va-deposit-transaction = 振込入金口座への入金明細通知   # noqa: E501

        :param event_type: The event_type of this EventType.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        if event_type is not None and len(event_type) > 128:
            raise ValueError("Invalid value for `event_type`, length must be less than or equal to `128`")  # noqa: E501
        if event_type is not None and len(event_type) < 1:
            raise ValueError("Invalid value for `event_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._event_type = event_type

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
        if issubclass(EventType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
