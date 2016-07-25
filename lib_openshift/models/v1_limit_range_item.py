# coding: utf-8

"""
    

    

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1LimitRangeItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, max=None, min=None, default=None, default_request=None, max_limit_request_ratio=None):
        """
        V1LimitRangeItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'max': 'object',
            'min': 'object',
            'default': 'object',
            'default_request': 'object',
            'max_limit_request_ratio': 'object'
        }

        self.attribute_map = {
            'type': 'type',
            'max': 'max',
            'min': 'min',
            'default': 'default',
            'default_request': 'defaultRequest',
            'max_limit_request_ratio': 'maxLimitRequestRatio'
        }

        self._type = type
        self._max = max
        self._min = min
        self._default = default
        self._default_request = default_request
        self._max_limit_request_ratio = max_limit_request_ratio

    @property
    def type(self):
        """
        Gets the type of this V1LimitRangeItem.
        Type of resource that this limit applies to.

        :return: The type of this V1LimitRangeItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1LimitRangeItem.
        Type of resource that this limit applies to.

        :param type: The type of this V1LimitRangeItem.
        :type: str
        """

        self._type = type

    @property
    def max(self):
        """
        Gets the max of this V1LimitRangeItem.
        Max usage constraints on this kind by resource name.

        :return: The max of this V1LimitRangeItem.
        :rtype: object
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this V1LimitRangeItem.
        Max usage constraints on this kind by resource name.

        :param max: The max of this V1LimitRangeItem.
        :type: object
        """

        self._max = max

    @property
    def min(self):
        """
        Gets the min of this V1LimitRangeItem.
        Min usage constraints on this kind by resource name.

        :return: The min of this V1LimitRangeItem.
        :rtype: object
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this V1LimitRangeItem.
        Min usage constraints on this kind by resource name.

        :param min: The min of this V1LimitRangeItem.
        :type: object
        """

        self._min = min

    @property
    def default(self):
        """
        Gets the default of this V1LimitRangeItem.
        Default resource requirement limit value by resource name if resource limit is omitted.

        :return: The default of this V1LimitRangeItem.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this V1LimitRangeItem.
        Default resource requirement limit value by resource name if resource limit is omitted.

        :param default: The default of this V1LimitRangeItem.
        :type: object
        """

        self._default = default

    @property
    def default_request(self):
        """
        Gets the default_request of this V1LimitRangeItem.
        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.

        :return: The default_request of this V1LimitRangeItem.
        :rtype: object
        """
        return self._default_request

    @default_request.setter
    def default_request(self, default_request):
        """
        Sets the default_request of this V1LimitRangeItem.
        DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.

        :param default_request: The default_request of this V1LimitRangeItem.
        :type: object
        """

        self._default_request = default_request

    @property
    def max_limit_request_ratio(self):
        """
        Gets the max_limit_request_ratio of this V1LimitRangeItem.
        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.

        :return: The max_limit_request_ratio of this V1LimitRangeItem.
        :rtype: object
        """
        return self._max_limit_request_ratio

    @max_limit_request_ratio.setter
    def max_limit_request_ratio(self, max_limit_request_ratio):
        """
        Sets the max_limit_request_ratio of this V1LimitRangeItem.
        MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.

        :param max_limit_request_ratio: The max_limit_request_ratio of this V1LimitRangeItem.
        :type: object
        """

        self._max_limit_request_ratio = max_limit_request_ratio


#{}"

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
