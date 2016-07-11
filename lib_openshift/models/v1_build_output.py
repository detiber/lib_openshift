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


class V1BuildOutput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1BuildOutput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'to': 'V1ObjectReference',
            'push_secret': 'V1LocalObjectReference'
        }

        self.attribute_map = {
            'to': 'to',
            'push_secret': 'pushSecret'
        }

        self._to = None
        self._push_secret = None

    @property
    def to(self):
        """
        Gets the to of this V1BuildOutput.
        To defines an optional location to push the output of this build to. Kind must be one of 'ImageStreamTag' or 'DockerImage'. This value will be used to look up a Docker image repository to push to. In the case of an ImageStreamTag, the ImageStreamTag will be looked for in the namespace of the build unless Namespace is specified.

        :return: The to of this V1BuildOutput.
        :rtype: V1ObjectReference
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this V1BuildOutput.
        To defines an optional location to push the output of this build to. Kind must be one of 'ImageStreamTag' or 'DockerImage'. This value will be used to look up a Docker image repository to push to. In the case of an ImageStreamTag, the ImageStreamTag will be looked for in the namespace of the build unless Namespace is specified.

        :param to: The to of this V1BuildOutput.
        :type: V1ObjectReference
        """
        self._to = to

    @property
    def push_secret(self):
        """
        Gets the push_secret of this V1BuildOutput.
        PushSecret is the name of a Secret that would be used for setting up the authentication for executing the Docker push to authentication enabled Docker Registry (or Docker Hub).

        :return: The push_secret of this V1BuildOutput.
        :rtype: V1LocalObjectReference
        """
        return self._push_secret

    @push_secret.setter
    def push_secret(self, push_secret):
        """
        Sets the push_secret of this V1BuildOutput.
        PushSecret is the name of a Secret that would be used for setting up the authentication for executing the Docker push to authentication enabled Docker Registry (or Docker Hub).

        :param push_secret: The push_secret of this V1BuildOutput.
        :type: V1LocalObjectReference
        """
        self._push_secret = push_secret

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

