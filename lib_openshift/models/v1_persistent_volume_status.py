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


class V1PersistentVolumeStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phase=None, message=None, reason=None):
        """
        V1PersistentVolumeStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phase': 'str',
            'message': 'str',
            'reason': 'str'
        }

        self.attribute_map = {
            'phase': 'phase',
            'message': 'message',
            'reason': 'reason'
        }

        self._phase = phase
        self._message = message
        self._reason = reason

    @property
    def phase(self):
        """
        Gets the phase of this V1PersistentVolumeStatus.
        Phase indicates if a volume is available, bound to a claim, or released by a claim. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#phase

        :return: The phase of this V1PersistentVolumeStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1PersistentVolumeStatus.
        Phase indicates if a volume is available, bound to a claim, or released by a claim. More info: http://releases.k8s.io/release-1.2/docs/user-guide/persistent-volumes.md#phase

        :param phase: The phase of this V1PersistentVolumeStatus.
        :type: str
        """

        self._phase = phase

    @property
    def message(self):
        """
        Gets the message of this V1PersistentVolumeStatus.
        A human-readable message indicating details about why the volume is in this state.

        :return: The message of this V1PersistentVolumeStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1PersistentVolumeStatus.
        A human-readable message indicating details about why the volume is in this state.

        :param message: The message of this V1PersistentVolumeStatus.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this V1PersistentVolumeStatus.
        Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.

        :return: The reason of this V1PersistentVolumeStatus.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1PersistentVolumeStatus.
        Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.

        :param reason: The reason of this V1PersistentVolumeStatus.
        :type: str
        """

        self._reason = reason


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
