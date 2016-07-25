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


class V1ServicePort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, protocol=None, port=None, target_port=None, node_port=None):
        """
        V1ServicePort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'protocol': 'str',
            'port': 'int',
            'target_port': 'str',
            'node_port': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'protocol': 'protocol',
            'port': 'port',
            'target_port': 'targetPort',
            'node_port': 'nodePort'
        }

        self._name = name
        self._protocol = protocol
        self._port = port
        self._target_port = target_port
        self._node_port = node_port

    @property
    def name(self):
        """
        Gets the name of this V1ServicePort.
        The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.

        :return: The name of this V1ServicePort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ServicePort.
        The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.

        :param name: The name of this V1ServicePort.
        :type: str
        """

        self._name = name

    @property
    def protocol(self):
        """
        Gets the protocol of this V1ServicePort.
        The IP protocol for this port. Supports \"TCP\" and \"UDP\". Default is TCP.

        :return: The protocol of this V1ServicePort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V1ServicePort.
        The IP protocol for this port. Supports \"TCP\" and \"UDP\". Default is TCP.

        :param protocol: The protocol of this V1ServicePort.
        :type: str
        """

        self._protocol = protocol

    @property
    def port(self):
        """
        Gets the port of this V1ServicePort.
        The port that will be exposed by this service.

        :return: The port of this V1ServicePort.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1ServicePort.
        The port that will be exposed by this service.

        :param port: The port of this V1ServicePort.
        :type: int
        """

        self._port = port

    @property
    def target_port(self):
        """
        Gets the target_port of this V1ServicePort.
        Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#defining-a-service

        :return: The target_port of this V1ServicePort.
        :rtype: str
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """
        Sets the target_port of this V1ServicePort.
        Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#defining-a-service

        :param target_port: The target_port of this V1ServicePort.
        :type: str
        """

        self._target_port = target_port

    @property
    def node_port(self):
        """
        Gets the node_port of this V1ServicePort.
        The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#type--nodeport

        :return: The node_port of this V1ServicePort.
        :rtype: int
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        """
        Sets the node_port of this V1ServicePort.
        The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#type--nodeport

        :param node_port: The node_port of this V1ServicePort.
        :type: int
        """

        self._node_port = node_port


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
