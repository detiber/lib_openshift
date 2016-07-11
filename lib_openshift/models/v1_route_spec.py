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


class V1RouteSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1RouteSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'host': 'str',
            'path': 'str',
            'to': 'V1ObjectReference',
            'port': 'V1RoutePort',
            'tls': 'V1TLSConfig'
        }

        self.attribute_map = {
            'host': 'host',
            'path': 'path',
            'to': 'to',
            'port': 'port',
            'tls': 'tls'
        }

        self._host = None
        self._path = None
        self._to = None
        self._port = None
        self._tls = None

    @property
    def host(self):
        """
        Gets the host of this V1RouteSpec.
        Host is an alias/DNS that points to the service. Optional Must follow DNS952 subdomain conventions.

        :return: The host of this V1RouteSpec.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1RouteSpec.
        Host is an alias/DNS that points to the service. Optional Must follow DNS952 subdomain conventions.

        :param host: The host of this V1RouteSpec.
        :type: str
        """
        self._host = host

    @property
    def path(self):
        """
        Gets the path of this V1RouteSpec.
        Path that the router watches for, to route traffic for to the service. Optional

        :return: The path of this V1RouteSpec.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1RouteSpec.
        Path that the router watches for, to route traffic for to the service. Optional

        :param path: The path of this V1RouteSpec.
        :type: str
        """
        self._path = path

    @property
    def to(self):
        """
        Gets the to of this V1RouteSpec.
        To is an object the route points to. Only the Service kind is allowed, and it will be defaulted to Service.

        :return: The to of this V1RouteSpec.
        :rtype: V1ObjectReference
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this V1RouteSpec.
        To is an object the route points to. Only the Service kind is allowed, and it will be defaulted to Service.

        :param to: The to of this V1RouteSpec.
        :type: V1ObjectReference
        """
        self._to = to

    @property
    def port(self):
        """
        Gets the port of this V1RouteSpec.
        If specified, the port to be used by the router. Most routers will use all endpoints exposed by the service by default - set this value to instruct routers which port to use.

        :return: The port of this V1RouteSpec.
        :rtype: V1RoutePort
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1RouteSpec.
        If specified, the port to be used by the router. Most routers will use all endpoints exposed by the service by default - set this value to instruct routers which port to use.

        :param port: The port of this V1RouteSpec.
        :type: V1RoutePort
        """
        self._port = port

    @property
    def tls(self):
        """
        Gets the tls of this V1RouteSpec.
        TLS provides the ability to configure certificates and termination for the route

        :return: The tls of this V1RouteSpec.
        :rtype: V1TLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """
        Sets the tls of this V1RouteSpec.
        TLS provides the ability to configure certificates and termination for the route

        :param tls: The tls of this V1RouteSpec.
        :type: V1TLSConfig
        """
        self._tls = tls

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

