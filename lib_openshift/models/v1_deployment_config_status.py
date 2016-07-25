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


class V1DeploymentConfigStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, latest_version=None, details=None):
        """
        V1DeploymentConfigStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'latest_version': 'int',
            'details': 'V1DeploymentDetails'
        }

        self.attribute_map = {
            'latest_version': 'latestVersion',
            'details': 'details'
        }

        self._latest_version = latest_version
        self._details = details

    @property
    def latest_version(self):
        """
        Gets the latest_version of this V1DeploymentConfigStatus.
        LatestVersion is used to determine whether the current deployment associated with a DeploymentConfig is out of sync.

        :return: The latest_version of this V1DeploymentConfigStatus.
        :rtype: int
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """
        Sets the latest_version of this V1DeploymentConfigStatus.
        LatestVersion is used to determine whether the current deployment associated with a DeploymentConfig is out of sync.

        :param latest_version: The latest_version of this V1DeploymentConfigStatus.
        :type: int
        """

        self._latest_version = latest_version

    @property
    def details(self):
        """
        Gets the details of this V1DeploymentConfigStatus.
        Details are the reasons for the update to this deployment config. This could be based on a change made by the user or caused by an automatic trigger

        :return: The details of this V1DeploymentConfigStatus.
        :rtype: V1DeploymentDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this V1DeploymentConfigStatus.
        Details are the reasons for the update to this deployment config. This could be based on a change made by the user or caused by an automatic trigger

        :param details: The details of this V1DeploymentConfigStatus.
        :type: V1DeploymentDetails
        """

        self._details = details


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
