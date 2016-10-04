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


class V1HorizontalPodAutoscalerSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    operations = [
    ]

    # The key is attribute name
    # and the value is attribute type.
    swagger_types = {
        'scale_target_ref': 'V1CrossVersionObjectReference',
        'min_replicas': 'int',
        'max_replicas': 'int',
        'target_cpu_utilization_percentage': 'int'
    }

    # The key is attribute name
    # and the value is json key in definition.
    attribute_map = {
        'scale_target_ref': 'scaleTargetRef',
        'min_replicas': 'minReplicas',
        'max_replicas': 'maxReplicas',
        'target_cpu_utilization_percentage': 'targetCPUUtilizationPercentage'
    }

    def __init__(self, scale_target_ref=None, min_replicas=None, max_replicas=None, target_cpu_utilization_percentage=None):
        """
        V1HorizontalPodAutoscalerSpec - a model defined in Swagger

        """

        self._scale_target_ref = scale_target_ref
        self._min_replicas = min_replicas
        self._max_replicas = max_replicas
        self._target_cpu_utilization_percentage = target_cpu_utilization_percentage

    @property
    def scale_target_ref(self):
        """
        Gets the scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.

        :return: The scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        :rtype: V1CrossVersionObjectReference
        """
        return self._scale_target_ref

    @scale_target_ref.setter
    def scale_target_ref(self, scale_target_ref):
        """
        Sets the scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.

        :param scale_target_ref: The scale_target_ref of this V1HorizontalPodAutoscalerSpec.
        :type: V1CrossVersionObjectReference
        """

        self._scale_target_ref = scale_target_ref

    @property
    def min_replicas(self):
        """
        Gets the min_replicas of this V1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :return: The min_replicas of this V1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._min_replicas

    @min_replicas.setter
    def min_replicas(self, min_replicas):
        """
        Sets the min_replicas of this V1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :param min_replicas: The min_replicas of this V1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._min_replicas = min_replicas

    @property
    def max_replicas(self):
        """
        Gets the max_replicas of this V1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :return: The max_replicas of this V1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._max_replicas

    @max_replicas.setter
    def max_replicas(self, max_replicas):
        """
        Sets the max_replicas of this V1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :param max_replicas: The max_replicas of this V1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._max_replicas = max_replicas

    @property
    def target_cpu_utilization_percentage(self):
        """
        Gets the target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.

        :return: The target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._target_cpu_utilization_percentage

    @target_cpu_utilization_percentage.setter
    def target_cpu_utilization_percentage(self, target_cpu_utilization_percentage):
        """
        Sets the target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.

        :param target_cpu_utilization_percentage: The target_cpu_utilization_percentage of this V1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._target_cpu_utilization_percentage = target_cpu_utilization_percentage

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(V1HorizontalPodAutoscalerSpec.swagger_types):
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
