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

from __future__ import absolute_import

import os
import sys
import unittest

import api_v1
from api_v1.rest import ApiException
from api_v1.models.v1_env_var import V1EnvVar


class TestV1EnvVar(unittest.TestCase):
    """ V1EnvVar unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1EnvVar(self):
        """
        Test V1EnvVar
        """
        model = api_v1.models.v1_env_var.V1EnvVar()


if __name__ == '__main__':
    unittest.main()
