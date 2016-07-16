# coding: utf-8

"""
    OpenShift v1 REST API

    The OpenShift API exposes operations for managing an enterprise Kubernetes cluster, including security and user management, application deployments, image and source builds, HTTP(s) routing, and project management.

    OpenAPI spec version: v1
    
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


class V1Lifecycle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, post_start=None, pre_stop=None):
        """
        V1Lifecycle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'post_start': 'V1Handler',
            'pre_stop': 'V1Handler'
        }

        self.attribute_map = {
            'post_start': 'postStart',
            'pre_stop': 'preStop'
        }

        self._post_start = post_start
        self._pre_stop = pre_stop

    @property
    def post_start(self):
        """
        Gets the post_start of this V1Lifecycle.
        PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/release-1.2/docs/user-guide/container-environment.md#hook-details

        :return: The post_start of this V1Lifecycle.
        :rtype: V1Handler
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """
        Sets the post_start of this V1Lifecycle.
        PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/release-1.2/docs/user-guide/container-environment.md#hook-details

        :param post_start: The post_start of this V1Lifecycle.
        :type: V1Handler
        """

        self._post_start = post_start

    @property
    def pre_stop(self):
        """
        Gets the pre_stop of this V1Lifecycle.
        PreStop is called immediately before a container is terminated. The container is terminated after the handler completes. The reason for termination is passed to the handler. Regardless of the outcome of the handler, the container is eventually terminated. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/release-1.2/docs/user-guide/container-environment.md#hook-details

        :return: The pre_stop of this V1Lifecycle.
        :rtype: V1Handler
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """
        Sets the pre_stop of this V1Lifecycle.
        PreStop is called immediately before a container is terminated. The container is terminated after the handler completes. The reason for termination is passed to the handler. Regardless of the outcome of the handler, the container is eventually terminated. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/release-1.2/docs/user-guide/container-environment.md#hook-details

        :param pre_stop: The pre_stop of this V1Lifecycle.
        :type: V1Handler
        """

        self._pre_stop = pre_stop

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
