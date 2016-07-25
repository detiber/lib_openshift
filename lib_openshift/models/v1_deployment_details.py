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


class V1DeploymentDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message=None, causes=None):
        """
        V1DeploymentDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'causes': 'list[V1DeploymentCause]'
        }

        self.attribute_map = {
            'message': 'message',
            'causes': 'causes'
        }

        self._message = message
        self._causes = causes

    @property
    def message(self):
        """
        Gets the message of this V1DeploymentDetails.
        Message is the user specified change message, if this deployment was triggered manually by the user

        :return: The message of this V1DeploymentDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1DeploymentDetails.
        Message is the user specified change message, if this deployment was triggered manually by the user

        :param message: The message of this V1DeploymentDetails.
        :type: str
        """

        self._message = message

    @property
    def causes(self):
        """
        Gets the causes of this V1DeploymentDetails.
        Causes are extended data associated with all the causes for creating a new deployment

        :return: The causes of this V1DeploymentDetails.
        :rtype: list[V1DeploymentCause]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """
        Sets the causes of this V1DeploymentDetails.
        Causes are extended data associated with all the causes for creating a new deployment

        :param causes: The causes of this V1DeploymentDetails.
        :type: list[V1DeploymentCause]
        """

        self._causes = causes


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
