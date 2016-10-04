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


class V1User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
        {
            'class': 'OapiV1',
            'type': 'update',
            'method': 'replace_user',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'delete',
            'method': 'delete_user',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'read',
            'method': 'get_user',
            'namespaced': False
        },
        {
            'class': 'OapiV1',
            'type': 'create',
            'method': 'create_user',
            'namespaced': False
        },
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'kind': 'str',
        'api_version': 'str',
        'metadata': 'V1ObjectMeta',
        'full_name': 'str',
        'identities': 'list[str]',
        'groups': 'list[str]'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'full_name': 'fullName',
        'identities': 'identities',
        'groups': 'groups'
    }

    def __init__(self, kind=None, api_version=None, metadata=None, full_name=None, identities=None, groups=None):
        """
        V1User - a model defined in Swagger

        """

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._full_name = full_name
        self._identities = identities
        self._groups = groups

    @property
    def kind(self):
        """
        Gets the kind of this V1User.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1User.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1User.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1User.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1User.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1User.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1User.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1User.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1User.
        Standard object's metadata.

        :return: The metadata of this V1User.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1User.
        Standard object's metadata.

        :param metadata: The metadata of this V1User.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def full_name(self):
        """
        Gets the full_name of this V1User.
        FullName is the full name of user

        :return: The full_name of this V1User.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this V1User.
        FullName is the full name of user

        :param full_name: The full_name of this V1User.
        :type: str
        """

        self._full_name = full_name

    @property
    def identities(self):
        """
        Gets the identities of this V1User.
        Identities are the identities associated with this user

        :return: The identities of this V1User.
        :rtype: list[str]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """
        Sets the identities of this V1User.
        Identities are the identities associated with this user

        :param identities: The identities of this V1User.
        :type: list[str]
        """

        self._identities = identities

    @property
    def groups(self):
        """
        Gets the groups of this V1User.
        Groups are the groups that this user is a member of

        :return: The groups of this V1User.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this V1User.
        Groups are the groups that this user is a member of

        :param groups: The groups of this V1User.
        :type: list[str]
        """

        self._groups = groups

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1User.swagger_types):
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
