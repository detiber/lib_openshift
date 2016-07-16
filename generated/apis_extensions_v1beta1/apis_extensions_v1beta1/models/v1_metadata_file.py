# coding: utf-8

"""
    

    

    OpenAPI spec version: extensions/v1beta1
    
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


class V1MetadataFile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, field_ref=None):
        """
        V1MetadataFile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'field_ref': 'V1ObjectFieldSelector'
        }

        self.attribute_map = {
            'name': 'name',
            'field_ref': 'fieldRef'
        }

        self._name = name
        self._field_ref = field_ref

    @property
    def name(self):
        """
        Gets the name of this V1MetadataFile.
        Name of the file to be created

        :return: The name of this V1MetadataFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1MetadataFile.
        Name of the file to be created

        :param name: The name of this V1MetadataFile.
        :type: str
        """

        self._name = name

    @property
    def field_ref(self):
        """
        Gets the field_ref of this V1MetadataFile.
        Selects a field of the pod. Supported fields: metadata.annotations, metadata.labels, metadata.name, metadata.namespace

        :return: The field_ref of this V1MetadataFile.
        :rtype: V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """
        Sets the field_ref of this V1MetadataFile.
        Selects a field of the pod. Supported fields: metadata.annotations, metadata.labels, metadata.name, metadata.namespace

        :param field_ref: The field_ref of this V1MetadataFile.
        :type: V1ObjectFieldSelector
        """

        self._field_ref = field_ref

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
