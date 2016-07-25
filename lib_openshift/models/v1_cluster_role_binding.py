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


class V1ClusterRoleBinding(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, kind=None, api_version=None, metadata=None, user_names=None, group_names=None, subjects=None, role_ref=None):
        """
        V1ClusterRoleBinding - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'user_names': 'list[str]',
            'group_names': 'list[str]',
            'subjects': 'list[V1ObjectReference]',
            'role_ref': 'V1ObjectReference'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'user_names': 'userNames',
            'group_names': 'groupNames',
            'subjects': 'subjects',
            'role_ref': 'roleRef'
        }

        self._kind = kind
        self._api_version = api_version
        self._metadata = metadata
        self._user_names = user_names
        self._group_names = group_names
        self._subjects = subjects
        self._role_ref = role_ref

    @property
    def kind(self):
        """
        Gets the kind of this V1ClusterRoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ClusterRoleBinding.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ClusterRoleBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ClusterRoleBinding.
        :type: str
        """

        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ClusterRoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ClusterRoleBinding.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ClusterRoleBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ClusterRoleBinding.
        :type: str
        """

        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ClusterRoleBinding.
        Standard object's metadata.

        :return: The metadata of this V1ClusterRoleBinding.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ClusterRoleBinding.
        Standard object's metadata.

        :param metadata: The metadata of this V1ClusterRoleBinding.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def user_names(self):
        """
        Gets the user_names of this V1ClusterRoleBinding.
        UserNames holds all the usernames directly bound to the role

        :return: The user_names of this V1ClusterRoleBinding.
        :rtype: list[str]
        """
        return self._user_names

    @user_names.setter
    def user_names(self, user_names):
        """
        Sets the user_names of this V1ClusterRoleBinding.
        UserNames holds all the usernames directly bound to the role

        :param user_names: The user_names of this V1ClusterRoleBinding.
        :type: list[str]
        """

        self._user_names = user_names

    @property
    def group_names(self):
        """
        Gets the group_names of this V1ClusterRoleBinding.
        GroupNames holds all the groups directly bound to the role

        :return: The group_names of this V1ClusterRoleBinding.
        :rtype: list[str]
        """
        return self._group_names

    @group_names.setter
    def group_names(self, group_names):
        """
        Sets the group_names of this V1ClusterRoleBinding.
        GroupNames holds all the groups directly bound to the role

        :param group_names: The group_names of this V1ClusterRoleBinding.
        :type: list[str]
        """

        self._group_names = group_names

    @property
    def subjects(self):
        """
        Gets the subjects of this V1ClusterRoleBinding.
        Subjects hold object references to authorize with this rule

        :return: The subjects of this V1ClusterRoleBinding.
        :rtype: list[V1ObjectReference]
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """
        Sets the subjects of this V1ClusterRoleBinding.
        Subjects hold object references to authorize with this rule

        :param subjects: The subjects of this V1ClusterRoleBinding.
        :type: list[V1ObjectReference]
        """

        self._subjects = subjects

    @property
    def role_ref(self):
        """
        Gets the role_ref of this V1ClusterRoleBinding.
        RoleRef can only reference the current namespace and the global namespace If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role

        :return: The role_ref of this V1ClusterRoleBinding.
        :rtype: V1ObjectReference
        """
        return self._role_ref

    @role_ref.setter
    def role_ref(self, role_ref):
        """
        Sets the role_ref of this V1ClusterRoleBinding.
        RoleRef can only reference the current namespace and the global namespace If the ClusterRoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role

        :param role_ref: The role_ref of this V1ClusterRoleBinding.
        :type: V1ObjectReference
        """

        self._role_ref = role_ref


#{patch&#x3D;{fileName&#x3D;oapi_v1.py, method&#x3D;patch_clusterrolebinding, className&#x3D;OapiV1}, replace&#x3D;{fileName&#x3D;oapi_v1.py, method&#x3D;replace_clusterrolebinding, className&#x3D;OapiV1}, create&#x3D;{fileName&#x3D;oapi_v1.py, method&#x3D;create_clusterrolebinding, className&#x3D;OapiV1}, delete&#x3D;{fileName&#x3D;oapi_v1.py, method&#x3D;delete_clusterrolebinding, className&#x3D;OapiV1}}"

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
