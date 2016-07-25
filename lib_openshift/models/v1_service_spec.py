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


class V1ServiceSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ports=None, selector=None, portal_ip=None, cluster_ip=None, type=None, external_i_ps=None, deprecated_public_i_ps=None, session_affinity=None, load_balancer_ip=None):
        """
        V1ServiceSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ports': 'list[V1ServicePort]',
            'selector': 'object',
            'portal_ip': 'str',
            'cluster_ip': 'str',
            'type': 'str',
            'external_i_ps': 'list[str]',
            'deprecated_public_i_ps': 'list[str]',
            'session_affinity': 'str',
            'load_balancer_ip': 'str'
        }

        self.attribute_map = {
            'ports': 'ports',
            'selector': 'selector',
            'portal_ip': 'portalIP',
            'cluster_ip': 'clusterIP',
            'type': 'type',
            'external_i_ps': 'externalIPs',
            'deprecated_public_i_ps': 'deprecatedPublicIPs',
            'session_affinity': 'sessionAffinity',
            'load_balancer_ip': 'loadBalancerIP'
        }

        self._ports = ports
        self._selector = selector
        self._portal_ip = portal_ip
        self._cluster_ip = cluster_ip
        self._type = type
        self._external_i_ps = external_i_ps
        self._deprecated_public_i_ps = deprecated_public_i_ps
        self._session_affinity = session_affinity
        self._load_balancer_ip = load_balancer_ip

    @property
    def ports(self):
        """
        Gets the ports of this V1ServiceSpec.
        The list of ports that are exposed by this service. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :return: The ports of this V1ServiceSpec.
        :rtype: list[V1ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1ServiceSpec.
        The list of ports that are exposed by this service. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :param ports: The ports of this V1ServiceSpec.
        :type: list[V1ServicePort]
        """

        self._ports = ports

    @property
    def selector(self):
        """
        Gets the selector of this V1ServiceSpec.
        This service will route traffic to pods having labels matching this selector. Label keys and values that must match in order to receive traffic for this service. If empty, all pods are selected, if not specified, endpoints must be manually specified. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#overview

        :return: The selector of this V1ServiceSpec.
        :rtype: object
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1ServiceSpec.
        This service will route traffic to pods having labels matching this selector. Label keys and values that must match in order to receive traffic for this service. If empty, all pods are selected, if not specified, endpoints must be manually specified. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#overview

        :param selector: The selector of this V1ServiceSpec.
        :type: object
        """

        self._selector = selector

    @property
    def portal_ip(self):
        """
        Gets the portal_ip of this V1ServiceSpec.
        The IP Address of the service. Deprecated: Use clusterIP instead.

        :return: The portal_ip of this V1ServiceSpec.
        :rtype: str
        """
        return self._portal_ip

    @portal_ip.setter
    def portal_ip(self, portal_ip):
        """
        Sets the portal_ip of this V1ServiceSpec.
        The IP Address of the service. Deprecated: Use clusterIP instead.

        :param portal_ip: The portal_ip of this V1ServiceSpec.
        :type: str
        """

        self._portal_ip = portal_ip

    @property
    def cluster_ip(self):
        """
        Gets the cluster_ip of this V1ServiceSpec.
        ClusterIP is usually assigned by the master and is the IP address of the service. If specified, it will be allocated to the service if it is unused or else creation of the service will fail. Valid values are None, empty string (\"\"), or a valid IP address. 'None' can be specified for a headless service when proxying is not required. Cannot be updated. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :return: The cluster_ip of this V1ServiceSpec.
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """
        Sets the cluster_ip of this V1ServiceSpec.
        ClusterIP is usually assigned by the master and is the IP address of the service. If specified, it will be allocated to the service if it is unused or else creation of the service will fail. Valid values are None, empty string (\"\"), or a valid IP address. 'None' can be specified for a headless service when proxying is not required. Cannot be updated. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :param cluster_ip: The cluster_ip of this V1ServiceSpec.
        :type: str
        """

        self._cluster_ip = cluster_ip

    @property
    def type(self):
        """
        Gets the type of this V1ServiceSpec.
        Type of exposed service. Must be ClusterIP, NodePort, or LoadBalancer. Defaults to ClusterIP. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#external-services

        :return: The type of this V1ServiceSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ServiceSpec.
        Type of exposed service. Must be ClusterIP, NodePort, or LoadBalancer. Defaults to ClusterIP. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#external-services

        :param type: The type of this V1ServiceSpec.
        :type: str
        """

        self._type = type

    @property
    def external_i_ps(self):
        """
        Gets the external_i_ps of this V1ServiceSpec.
        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field.

        :return: The external_i_ps of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._external_i_ps

    @external_i_ps.setter
    def external_i_ps(self, external_i_ps):
        """
        Sets the external_i_ps of this V1ServiceSpec.
        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  A previous form of this functionality exists as the deprecatedPublicIPs field.  When using this field, callers should also clear the deprecatedPublicIPs field.

        :param external_i_ps: The external_i_ps of this V1ServiceSpec.
        :type: list[str]
        """

        self._external_i_ps = external_i_ps

    @property
    def deprecated_public_i_ps(self):
        """
        Gets the deprecated_public_i_ps of this V1ServiceSpec.
        deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used.

        :return: The deprecated_public_i_ps of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._deprecated_public_i_ps

    @deprecated_public_i_ps.setter
    def deprecated_public_i_ps(self, deprecated_public_i_ps):
        """
        Sets the deprecated_public_i_ps of this V1ServiceSpec.
        deprecatedPublicIPs is deprecated and replaced by the externalIPs field with almost the exact same semantics.  This field is retained in the v1 API for compatibility until at least 8/20/2016.  It will be removed from any new API revisions.  If both deprecatedPublicIPs *and* externalIPs are set, deprecatedPublicIPs is used.

        :param deprecated_public_i_ps: The deprecated_public_i_ps of this V1ServiceSpec.
        :type: list[str]
        """

        self._deprecated_public_i_ps = deprecated_public_i_ps

    @property
    def session_affinity(self):
        """
        Gets the session_affinity of this V1ServiceSpec.
        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :return: The session_affinity of this V1ServiceSpec.
        :rtype: str
        """
        return self._session_affinity

    @session_affinity.setter
    def session_affinity(self, session_affinity):
        """
        Sets the session_affinity of this V1ServiceSpec.
        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: http://releases.k8s.io/release-1.2/docs/user-guide/services.md#virtual-ips-and-service-proxies

        :param session_affinity: The session_affinity of this V1ServiceSpec.
        :type: str
        """

        self._session_affinity = session_affinity

    @property
    def load_balancer_ip(self):
        """
        Gets the load_balancer_ip of this V1ServiceSpec.
        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        :return: The load_balancer_ip of this V1ServiceSpec.
        :rtype: str
        """
        return self._load_balancer_ip

    @load_balancer_ip.setter
    def load_balancer_ip(self, load_balancer_ip):
        """
        Sets the load_balancer_ip of this V1ServiceSpec.
        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

        :param load_balancer_ip: The load_balancer_ip of this V1ServiceSpec.
        :type: str
        """

        self._load_balancer_ip = load_balancer_ip


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
