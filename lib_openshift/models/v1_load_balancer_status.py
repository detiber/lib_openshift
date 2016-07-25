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


class V1LoadBalancerStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ingress=None):
        """
        V1LoadBalancerStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ingress': 'list[V1LoadBalancerIngress]'
        }

        self.attribute_map = {
            'ingress': 'ingress'
        }

        self._ingress = ingress

    @property
    def ingress(self):
        """
        Gets the ingress of this V1LoadBalancerStatus.
        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.

        :return: The ingress of this V1LoadBalancerStatus.
        :rtype: list[V1LoadBalancerIngress]
        """
        return self._ingress

    @ingress.setter
    def ingress(self, ingress):
        """
        Sets the ingress of this V1LoadBalancerStatus.
        Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.

        :param ingress: The ingress of this V1LoadBalancerStatus.
        :type: list[V1LoadBalancerIngress]
        """

        self._ingress = ingress


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
