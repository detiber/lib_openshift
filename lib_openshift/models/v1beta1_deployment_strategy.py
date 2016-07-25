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


class V1beta1DeploymentStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, rolling_update=None):
        """
        V1beta1DeploymentStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'rolling_update': 'V1beta1RollingUpdateDeployment'
        }

        self.attribute_map = {
            'type': 'type',
            'rolling_update': 'rollingUpdate'
        }

        self._type = type
        self._rolling_update = rolling_update

    @property
    def type(self):
        """
        Gets the type of this V1beta1DeploymentStrategy.
        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.

        :return: The type of this V1beta1DeploymentStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1beta1DeploymentStrategy.
        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.

        :param type: The type of this V1beta1DeploymentStrategy.
        :type: str
        """

        self._type = type

    @property
    def rolling_update(self):
        """
        Gets the rolling_update of this V1beta1DeploymentStrategy.
        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

        :return: The rolling_update of this V1beta1DeploymentStrategy.
        :rtype: V1beta1RollingUpdateDeployment
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update):
        """
        Sets the rolling_update of this V1beta1DeploymentStrategy.
        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

        :param rolling_update: The rolling_update of this V1beta1DeploymentStrategy.
        :type: V1beta1RollingUpdateDeployment
        """

        self._rolling_update = rolling_update


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
