# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1SupplementalGroupsStrategyOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1SupplementalGroupsStrategyOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'ranges': 'list[V1IDRange]'
        }

        self.attribute_map = {
            'type': 'type',
            'ranges': 'ranges'
        }

        self._type = None
        self._ranges = None

    @property
    def type(self):
        """
        Gets the type of this V1SupplementalGroupsStrategyOptions.
        Type is the strategy that will dictate what supplemental groups is used in the SecurityContext.

        :return: The type of this V1SupplementalGroupsStrategyOptions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1SupplementalGroupsStrategyOptions.
        Type is the strategy that will dictate what supplemental groups is used in the SecurityContext.

        :param type: The type of this V1SupplementalGroupsStrategyOptions.
        :type: str
        """
        self._type = type

    @property
    def ranges(self):
        """
        Gets the ranges of this V1SupplementalGroupsStrategyOptions.
        Ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end.

        :return: The ranges of this V1SupplementalGroupsStrategyOptions.
        :rtype: list[V1IDRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """
        Sets the ranges of this V1SupplementalGroupsStrategyOptions.
        Ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end.

        :param ranges: The ranges of this V1SupplementalGroupsStrategyOptions.
        :type: list[V1IDRange]
        """
        self._ranges = ranges

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

