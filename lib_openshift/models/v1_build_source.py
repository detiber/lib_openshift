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


class V1BuildSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'type': 'str',
        'binary': 'V1BinaryBuildSource',
        'dockerfile': 'str',
        'git': 'V1GitBuildSource',
        'images': 'list[V1ImageSource]',
        'context_dir': 'str',
        'source_secret': 'V1LocalObjectReference',
        'secrets': 'list[V1SecretBuildSource]'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'type': 'type',
        'binary': 'binary',
        'dockerfile': 'dockerfile',
        'git': 'git',
        'images': 'images',
        'context_dir': 'contextDir',
        'source_secret': 'sourceSecret',
        'secrets': 'secrets'
    }

    def __init__(self, type=None, binary=None, dockerfile=None, git=None, images=None, context_dir=None, source_secret=None, secrets=None):
        """
        V1BuildSource - a model defined in Swagger

        """

        self._type = type
        self._binary = binary
        self._dockerfile = dockerfile
        self._git = git
        self._images = images
        self._context_dir = context_dir
        self._source_secret = source_secret
        self._secrets = secrets

    @property
    def type(self):
        """
        Gets the type of this V1BuildSource.
        Type of build input to accept

        :return: The type of this V1BuildSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1BuildSource.
        Type of build input to accept

        :param type: The type of this V1BuildSource.
        :type: str
        """

        self._type = type

    @property
    def binary(self):
        """
        Gets the binary of this V1BuildSource.
        Binary builds accept a binary as their input. The binary is generally assumed to be a tar, gzipped tar, or zip file depending on the strategy. For Docker builds, this is the build context and an optional Dockerfile may be specified to override any Dockerfile in the build context. For Source builds, this is assumed to be an archive as described above. For Source and Docker builds, if binary.asFile is set the build will receive a directory with a single file. contextDir may be used when an archive is provided. Custom builds will receive this binary as input on STDIN.

        :return: The binary of this V1BuildSource.
        :rtype: V1BinaryBuildSource
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this V1BuildSource.
        Binary builds accept a binary as their input. The binary is generally assumed to be a tar, gzipped tar, or zip file depending on the strategy. For Docker builds, this is the build context and an optional Dockerfile may be specified to override any Dockerfile in the build context. For Source builds, this is assumed to be an archive as described above. For Source and Docker builds, if binary.asFile is set the build will receive a directory with a single file. contextDir may be used when an archive is provided. Custom builds will receive this binary as input on STDIN.

        :param binary: The binary of this V1BuildSource.
        :type: V1BinaryBuildSource
        """

        self._binary = binary

    @property
    def dockerfile(self):
        """
        Gets the dockerfile of this V1BuildSource.
        Dockerfile is the raw contents of a Dockerfile which should be built. When this option is specified, the FROM may be modified based on your strategy base image and additional ENV stanzas from your strategy environment will be added after the FROM, but before the rest of your Dockerfile stanzas. The Dockerfile source type may be used with other options like git - in those cases the Git repo will have any innate Dockerfile replaced in the context dir.

        :return: The dockerfile of this V1BuildSource.
        :rtype: str
        """
        return self._dockerfile

    @dockerfile.setter
    def dockerfile(self, dockerfile):
        """
        Sets the dockerfile of this V1BuildSource.
        Dockerfile is the raw contents of a Dockerfile which should be built. When this option is specified, the FROM may be modified based on your strategy base image and additional ENV stanzas from your strategy environment will be added after the FROM, but before the rest of your Dockerfile stanzas. The Dockerfile source type may be used with other options like git - in those cases the Git repo will have any innate Dockerfile replaced in the context dir.

        :param dockerfile: The dockerfile of this V1BuildSource.
        :type: str
        """

        self._dockerfile = dockerfile

    @property
    def git(self):
        """
        Gets the git of this V1BuildSource.
        Git contains optional information about git build source

        :return: The git of this V1BuildSource.
        :rtype: V1GitBuildSource
        """
        return self._git

    @git.setter
    def git(self, git):
        """
        Sets the git of this V1BuildSource.
        Git contains optional information about git build source

        :param git: The git of this V1BuildSource.
        :type: V1GitBuildSource
        """

        self._git = git

    @property
    def images(self):
        """
        Gets the images of this V1BuildSource.
        Images describes a set of images to be used to provide source for the build

        :return: The images of this V1BuildSource.
        :rtype: list[V1ImageSource]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this V1BuildSource.
        Images describes a set of images to be used to provide source for the build

        :param images: The images of this V1BuildSource.
        :type: list[V1ImageSource]
        """

        self._images = images

    @property
    def context_dir(self):
        """
        Gets the context_dir of this V1BuildSource.
        ContextDir specifies the sub-directory where the source code for the application exists. This allows to have buildable sources in directory other than root of repository.

        :return: The context_dir of this V1BuildSource.
        :rtype: str
        """
        return self._context_dir

    @context_dir.setter
    def context_dir(self, context_dir):
        """
        Sets the context_dir of this V1BuildSource.
        ContextDir specifies the sub-directory where the source code for the application exists. This allows to have buildable sources in directory other than root of repository.

        :param context_dir: The context_dir of this V1BuildSource.
        :type: str
        """

        self._context_dir = context_dir

    @property
    def source_secret(self):
        """
        Gets the source_secret of this V1BuildSource.
        SourceSecret is the name of a Secret that would be used for setting up the authentication for cloning private repository. The secret contains valid credentials for remote repository, where the data's key represent the authentication method to be used and value is the base64 encoded credentials. Supported auth methods are: ssh-privatekey.

        :return: The source_secret of this V1BuildSource.
        :rtype: V1LocalObjectReference
        """
        return self._source_secret

    @source_secret.setter
    def source_secret(self, source_secret):
        """
        Sets the source_secret of this V1BuildSource.
        SourceSecret is the name of a Secret that would be used for setting up the authentication for cloning private repository. The secret contains valid credentials for remote repository, where the data's key represent the authentication method to be used and value is the base64 encoded credentials. Supported auth methods are: ssh-privatekey.

        :param source_secret: The source_secret of this V1BuildSource.
        :type: V1LocalObjectReference
        """

        self._source_secret = source_secret

    @property
    def secrets(self):
        """
        Gets the secrets of this V1BuildSource.
        Secrets represents a list of secrets and their destinations that will be used only for the build.

        :return: The secrets of this V1BuildSource.
        :rtype: list[V1SecretBuildSource]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """
        Sets the secrets of this V1BuildSource.
        Secrets represents a list of secrets and their destinations that will be used only for the build.

        :param secrets: The secrets of this V1BuildSource.
        :type: list[V1SecretBuildSource]
        """

        self._secrets = secrets

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1BuildSource.swagger_types):
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
