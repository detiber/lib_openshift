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


class V1ImageChangeTrigger(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'last_triggered_image_id': 'str',
        '_from': 'V1ObjectReference'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'last_triggered_image_id': 'lastTriggeredImageID',
        '_from': 'from'
    }

    def __init__(self, last_triggered_image_id=None, _from=None):
        """
        V1ImageChangeTrigger - a model defined in Swagger

        """

        self._last_triggered_image_id = last_triggered_image_id
        self.__from = _from

    @property
    def last_triggered_image_id(self):
        """
        Gets the last_triggered_image_id of this V1ImageChangeTrigger.
        LastTriggeredImageID is used internally by the ImageChangeController to save last used image ID for build

        :return: The last_triggered_image_id of this V1ImageChangeTrigger.
        :rtype: str
        """
        return self._last_triggered_image_id

    @last_triggered_image_id.setter
    def last_triggered_image_id(self, last_triggered_image_id):
        """
        Sets the last_triggered_image_id of this V1ImageChangeTrigger.
        LastTriggeredImageID is used internally by the ImageChangeController to save last used image ID for build

        :param last_triggered_image_id: The last_triggered_image_id of this V1ImageChangeTrigger.
        :type: str
        """

        self._last_triggered_image_id = last_triggered_image_id

    @property
    def _from(self):
        """
        Gets the _from of this V1ImageChangeTrigger.
        From is a reference to an ImageStreamTag that will trigger a build when updated It is optional. If no From is specified, the From image from the build strategy will be used. Only one ImageChangeTrigger with an empty From reference is allowed in a build configuration.

        :return: The _from of this V1ImageChangeTrigger.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1ImageChangeTrigger.
        From is a reference to an ImageStreamTag that will trigger a build when updated It is optional. If no From is specified, the From image from the build strategy will be used. Only one ImageChangeTrigger with an empty From reference is allowed in a build configuration.

        :param _from: The _from of this V1ImageChangeTrigger.
        :type: V1ObjectReference
        """

        self.__from = _from

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1ImageChangeTrigger.swagger_types):
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
