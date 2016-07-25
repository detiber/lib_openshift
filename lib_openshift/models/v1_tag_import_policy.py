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


class V1TagImportPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, insecure=None, scheduled=None):
        """
        V1TagImportPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'insecure': 'bool',
            'scheduled': 'bool'
        }

        self.attribute_map = {
            'insecure': 'insecure',
            'scheduled': 'scheduled'
        }

        self._insecure = insecure
        self._scheduled = scheduled

    @property
    def insecure(self):
        """
        Gets the insecure of this V1TagImportPolicy.
        Insecure is true if the server may bypass certificate verification or connect directly over HTTP during image import.

        :return: The insecure of this V1TagImportPolicy.
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """
        Sets the insecure of this V1TagImportPolicy.
        Insecure is true if the server may bypass certificate verification or connect directly over HTTP during image import.

        :param insecure: The insecure of this V1TagImportPolicy.
        :type: bool
        """

        self._insecure = insecure

    @property
    def scheduled(self):
        """
        Gets the scheduled of this V1TagImportPolicy.
        Scheduled indicates to the server that this tag should be periodically checked to ensure it is up to date, and imported

        :return: The scheduled of this V1TagImportPolicy.
        :rtype: bool
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """
        Sets the scheduled of this V1TagImportPolicy.
        Scheduled indicates to the server that this tag should be periodically checked to ensure it is up to date, and imported

        :param scheduled: The scheduled of this V1TagImportPolicy.
        :type: bool
        """

        self._scheduled = scheduled


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
