# coding: utf-8

"""
    Kubernetes v1 REST API

    The Kubernetes API allows you to run containerized applications, bind persistent storage, link those applications through service discovery, and manage the cluster infrastructure.

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


class V1FlexVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, driver=None, fs_type=None, secret_ref=None, read_only=None, options=None):
        """
        V1FlexVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'driver': 'str',
            'fs_type': 'str',
            'secret_ref': 'V1LocalObjectReference',
            'read_only': 'bool',
            'options': 'object'
        }

        self.attribute_map = {
            'driver': 'driver',
            'fs_type': 'fsType',
            'secret_ref': 'secretRef',
            'read_only': 'readOnly',
            'options': 'options'
        }

        self._driver = driver
        self._fs_type = fs_type
        self._secret_ref = secret_ref
        self._read_only = read_only
        self._options = options

    @property
    def driver(self):
        """
        Gets the driver of this V1FlexVolumeSource.
        Driver is the name of the driver to use for this volume.

        :return: The driver of this V1FlexVolumeSource.
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """
        Sets the driver of this V1FlexVolumeSource.
        Driver is the name of the driver to use for this volume.

        :param driver: The driver of this V1FlexVolumeSource.
        :type: str
        """

        self._driver = driver

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1FlexVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". The default filesystem depends on FlexVolume script.

        :return: The fs_type of this V1FlexVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1FlexVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". The default filesystem depends on FlexVolume script.

        :param fs_type: The fs_type of this V1FlexVolumeSource.
        :type: str
        """

        self._fs_type = fs_type

    @property
    def secret_ref(self):
        """
        Gets the secret_ref of this V1FlexVolumeSource.
        Optional: SecretRef is reference to the authentication secret for User, default is empty.

        :return: The secret_ref of this V1FlexVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """
        Sets the secret_ref of this V1FlexVolumeSource.
        Optional: SecretRef is reference to the authentication secret for User, default is empty.

        :param secret_ref: The secret_ref of this V1FlexVolumeSource.
        :type: V1LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def read_only(self):
        """
        Gets the read_only of this V1FlexVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :return: The read_only of this V1FlexVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1FlexVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :param read_only: The read_only of this V1FlexVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    @property
    def options(self):
        """
        Gets the options of this V1FlexVolumeSource.
        Optional: Extra command options if any.

        :return: The options of this V1FlexVolumeSource.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this V1FlexVolumeSource.
        Optional: Extra command options if any.

        :param options: The options of this V1FlexVolumeSource.
        :type: object
        """

        self._options = options

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
