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


class V1ImageImportStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'status': 'UnversionedStatus',
        'image': 'V1Image',
        'tag': 'str'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'status': 'status',
        'image': 'image',
        'tag': 'tag'
    }

    def __init__(self, status=None, image=None, tag=None):
        """
        V1ImageImportStatus - a model defined in Swagger

        """

        self._status = status
        self._image = image
        self._tag = tag

    @property
    def status(self):
        """
        Gets the status of this V1ImageImportStatus.
        Status is the status of the image import, including errors encountered while retrieving the image

        :return: The status of this V1ImageImportStatus.
        :rtype: UnversionedStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1ImageImportStatus.
        Status is the status of the image import, including errors encountered while retrieving the image

        :param status: The status of this V1ImageImportStatus.
        :type: UnversionedStatus
        """

        self._status = status

    @property
    def image(self):
        """
        Gets the image of this V1ImageImportStatus.
        Image is the metadata of that image, if the image was located

        :return: The image of this V1ImageImportStatus.
        :rtype: V1Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1ImageImportStatus.
        Image is the metadata of that image, if the image was located

        :param image: The image of this V1ImageImportStatus.
        :type: V1Image
        """

        self._image = image

    @property
    def tag(self):
        """
        Gets the tag of this V1ImageImportStatus.
        Tag is the tag this image was located under, if any

        :return: The tag of this V1ImageImportStatus.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this V1ImageImportStatus.
        Tag is the tag this image was located under, if any

        :param tag: The tag of this V1ImageImportStatus.
        :type: str
        """

        self._tag = tag

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1ImageImportStatus.swagger_types):
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
