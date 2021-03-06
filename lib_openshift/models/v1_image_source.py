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


class V1ImageSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        '_from': 'V1ObjectReference',
        'paths': 'list[V1ImageSourcePath]',
        'pull_secret': 'V1LocalObjectReference'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        '_from': 'from',
        'paths': 'paths',
        'pull_secret': 'pullSecret'
    }

    def __init__(self, _from=None, paths=None, pull_secret=None):
        """
        V1ImageSource - a model defined in Swagger

        """

        self.__from = _from
        self._paths = paths
        self._pull_secret = pull_secret

    @property
    def _from(self):
        """
        Gets the _from of this V1ImageSource.
        From is a reference to an ImageStreamTag, ImageStreamImage, or DockerImage to copy source from.

        :return: The _from of this V1ImageSource.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1ImageSource.
        From is a reference to an ImageStreamTag, ImageStreamImage, or DockerImage to copy source from.

        :param _from: The _from of this V1ImageSource.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def paths(self):
        """
        Gets the paths of this V1ImageSource.
        Paths is a list of source and destination paths to copy from the image.

        :return: The paths of this V1ImageSource.
        :rtype: list[V1ImageSourcePath]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this V1ImageSource.
        Paths is a list of source and destination paths to copy from the image.

        :param paths: The paths of this V1ImageSource.
        :type: list[V1ImageSourcePath]
        """

        self._paths = paths

    @property
    def pull_secret(self):
        """
        Gets the pull_secret of this V1ImageSource.
        PullSecret is a reference to a secret to be used to pull the image from a registry If the image is pulled from the OpenShift registry, this field does not need to be set.

        :return: The pull_secret of this V1ImageSource.
        :rtype: V1LocalObjectReference
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """
        Sets the pull_secret of this V1ImageSource.
        PullSecret is a reference to a secret to be used to pull the image from a registry If the image is pulled from the OpenShift registry, this field does not need to be set.

        :param pull_secret: The pull_secret of this V1ImageSource.
        :type: V1LocalObjectReference
        """

        self._pull_secret = pull_secret

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1ImageSource.swagger_types):
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
