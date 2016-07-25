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


class V1RepositoryImportSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, import_policy=None, include_manifest=None):
        """
        V1RepositoryImportSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'V1ObjectReference',
            'import_policy': 'V1TagImportPolicy',
            'include_manifest': 'bool'
        }

        self.attribute_map = {
            '_from': 'from',
            'import_policy': 'importPolicy',
            'include_manifest': 'includeManifest'
        }

        self.__from = _from
        self._import_policy = import_policy
        self._include_manifest = include_manifest

    @property
    def _from(self):
        """
        Gets the _from of this V1RepositoryImportSpec.
        From is the source for the image repository to import; only kind DockerImage and a name of a Docker image repository is allowed

        :return: The _from of this V1RepositoryImportSpec.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1RepositoryImportSpec.
        From is the source for the image repository to import; only kind DockerImage and a name of a Docker image repository is allowed

        :param _from: The _from of this V1RepositoryImportSpec.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def import_policy(self):
        """
        Gets the import_policy of this V1RepositoryImportSpec.
        ImportPolicy is the policy controlling how the image is imported

        :return: The import_policy of this V1RepositoryImportSpec.
        :rtype: V1TagImportPolicy
        """
        return self._import_policy

    @import_policy.setter
    def import_policy(self, import_policy):
        """
        Sets the import_policy of this V1RepositoryImportSpec.
        ImportPolicy is the policy controlling how the image is imported

        :param import_policy: The import_policy of this V1RepositoryImportSpec.
        :type: V1TagImportPolicy
        """

        self._import_policy = import_policy

    @property
    def include_manifest(self):
        """
        Gets the include_manifest of this V1RepositoryImportSpec.
        IncludeManifest determines if the manifest for each image is returned in the response

        :return: The include_manifest of this V1RepositoryImportSpec.
        :rtype: bool
        """
        return self._include_manifest

    @include_manifest.setter
    def include_manifest(self, include_manifest):
        """
        Sets the include_manifest of this V1RepositoryImportSpec.
        IncludeManifest determines if the manifest for each image is returned in the response

        :param include_manifest: The include_manifest of this V1RepositoryImportSpec.
        :type: bool
        """

        self._include_manifest = include_manifest


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
