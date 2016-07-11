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


class V1TagReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1TagReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'annotations': 'object',
            '_from': 'V1ObjectReference',
            'reference': 'bool',
            'generation': 'int',
            'import_policy': 'V1TagImportPolicy'
        }

        self.attribute_map = {
            'name': 'name',
            'annotations': 'annotations',
            '_from': 'from',
            'reference': 'reference',
            'generation': 'generation',
            'import_policy': 'importPolicy'
        }

        self._name = None
        self._annotations = None
        self.__from = None
        self._reference = None
        self._generation = None
        self._import_policy = None

    @property
    def name(self):
        """
        Gets the name of this V1TagReference.
        Name of the tag

        :return: The name of this V1TagReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1TagReference.
        Name of the tag

        :param name: The name of this V1TagReference.
        :type: str
        """
        self._name = name

    @property
    def annotations(self):
        """
        Gets the annotations of this V1TagReference.
        Annotations associated with images using this tag

        :return: The annotations of this V1TagReference.
        :rtype: object
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this V1TagReference.
        Annotations associated with images using this tag

        :param annotations: The annotations of this V1TagReference.
        :type: object
        """
        self._annotations = annotations

    @property
    def _from(self):
        """
        Gets the _from of this V1TagReference.
        From is a reference to an image stream tag or image stream this tag should track

        :return: The _from of this V1TagReference.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1TagReference.
        From is a reference to an image stream tag or image stream this tag should track

        :param _from: The _from of this V1TagReference.
        :type: V1ObjectReference
        """
        self.__from = _from

    @property
    def reference(self):
        """
        Gets the reference of this V1TagReference.
        Reference states if the tag will be imported. Default value is false, which means the tag will be imported.

        :return: The reference of this V1TagReference.
        :rtype: bool
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this V1TagReference.
        Reference states if the tag will be imported. Default value is false, which means the tag will be imported.

        :param reference: The reference of this V1TagReference.
        :type: bool
        """
        self._reference = reference

    @property
    def generation(self):
        """
        Gets the generation of this V1TagReference.
        Generation is the image stream generation that updated this tag - setting it to 0 is an indication that the generation must be updated. Legacy clients will send this as nil, which means the client doesn't know or care.

        :return: The generation of this V1TagReference.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """
        Sets the generation of this V1TagReference.
        Generation is the image stream generation that updated this tag - setting it to 0 is an indication that the generation must be updated. Legacy clients will send this as nil, which means the client doesn't know or care.

        :param generation: The generation of this V1TagReference.
        :type: int
        """
        self._generation = generation

    @property
    def import_policy(self):
        """
        Gets the import_policy of this V1TagReference.
        Import is information that controls how images may be imported by the server.

        :return: The import_policy of this V1TagReference.
        :rtype: V1TagImportPolicy
        """
        return self._import_policy

    @import_policy.setter
    def import_policy(self, import_policy):
        """
        Sets the import_policy of this V1TagReference.
        Import is information that controls how images may be imported by the server.

        :param import_policy: The import_policy of this V1TagReference.
        :type: V1TagImportPolicy
        """
        self._import_policy = import_policy

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

