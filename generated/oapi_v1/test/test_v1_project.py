# coding: utf-8

"""
    OpenShift v1 REST API

    The OpenShift API exposes operations for managing an enterprise Kubernetes cluster, including security and user management, application deployments, image and source builds, HTTP(s) routing, and project management.

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

import oapi_v1
from oapi_v1.rest import ApiException
from oapi_v1.models.v1_project import V1Project


class TestV1Project(unittest.TestCase):
    """ V1Project unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Project(self):
        """
        Test V1Project
        """
        model = oapi_v1.models.v1_project.V1Project()


if __name__ == '__main__':
    unittest.main()
