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


class V1HostSubnet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_hostsubnet',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'update',
            'method': 'replace_hostsubnet',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'delete',
            'method': 'delete_hostsubnet',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'read',
            'method': 'get_hostsubnet',
            'namespaced': False
        },
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'V1ObjectMeta',
        'host': 'str',
        'host_ip': 'str',
        'subnet': 'str'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'host': 'host',
        'host_ip': 'hostIP',
        'subnet': 'subnet'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, host=None, host_ip=None, subnet=None):
        """
        V1HostSubnet - a model defined in Swagger

        """

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._host = host
        self._host_ip = host_ip
        self._subnet = subnet

    @property
    def kind(self):
        """
        Gets the kind of this V1HostSubnet.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1HostSubnet.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1HostSubnet.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1HostSubnet.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1HostSubnet.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1HostSubnet.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1HostSubnet.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1HostSubnet.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1HostSubnet.
        Standard object's metadata.

        :return: The metadata of this V1HostSubnet.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1HostSubnet.
        Standard object's metadata.

        :param metadata: The metadata of this V1HostSubnet.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def host(self):
        """
        Gets the host of this V1HostSubnet.
        Host is the name of the host that is registered at the master. May just be an IP address, resolvable hostname or a complete DNS. A lease will be sought after this name.

        :return: The host of this V1HostSubnet.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this V1HostSubnet.
        Host is the name of the host that is registered at the master. May just be an IP address, resolvable hostname or a complete DNS. A lease will be sought after this name.

        :param host: The host of this V1HostSubnet.
        :type: str
        """

        self._host = host

    @property
    def host_ip(self):
        """
        Gets the host_ip of this V1HostSubnet.
        HostIP is the IP address to be used as vtep by other hosts in the overlay network

        :return: The host_ip of this V1HostSubnet.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """
        Sets the host_ip of this V1HostSubnet.
        HostIP is the IP address to be used as vtep by other hosts in the overlay network

        :param host_ip: The host_ip of this V1HostSubnet.
        :type: str
        """

        self._host_ip = host_ip

    @property
    def subnet(self):
        """
        Gets the subnet of this V1HostSubnet.
        Subnet is the actual subnet CIDR lease assigned to the host

        :return: The subnet of this V1HostSubnet.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """
        Sets the subnet of this V1HostSubnet.
        Subnet is the actual subnet CIDR lease assigned to the host

        :param subnet: The subnet of this V1HostSubnet.
        :type: str
        """

        self._subnet = subnet

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1HostSubnet.swagger_types):
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
