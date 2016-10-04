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


class V1NamespaceStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'phase': 'str'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'phase': 'phase'
    }

    def __init__(self, phase=None):
        """
        V1NamespaceStatus - a model defined in Swagger

        """

        self._phase = phase

    @property
    def phase(self):
        """
        Gets the phase of this V1NamespaceStatus.
        Phase is the current lifecycle phase of the namespace. More info: http://releases.k8s.io/release-1.2/docs/design/namespaces.md#phases

        :return: The phase of this V1NamespaceStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1NamespaceStatus.
        Phase is the current lifecycle phase of the namespace. More info: http://releases.k8s.io/release-1.2/docs/design/namespaces.md#phases

        :param phase: The phase of this V1NamespaceStatus.
        :type: str
        """

        self._phase = phase

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1NamespaceStatus.swagger_types):
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
