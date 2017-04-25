# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1PodDisruptionBudgetSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, min_available=None, selector=None):
        """
        V1beta1PodDisruptionBudgetSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'min_available': 'str',
            'selector': 'V1LabelSelector'
        }

        self.attribute_map = {
            'min_available': 'minAvailable',
            'selector': 'selector'
        }

        self._min_available = min_available
        self._selector = selector

    @property
    def min_available(self):
        """
        Gets the min_available of this V1beta1PodDisruptionBudgetSpec.
        An eviction is allowed if at least \"minAvailable\" pods selected by \"selector\" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying \"100%\".

        :return: The min_available of this V1beta1PodDisruptionBudgetSpec.
        :rtype: str
        """
        return self._min_available

    @min_available.setter
    def min_available(self, min_available):
        """
        Sets the min_available of this V1beta1PodDisruptionBudgetSpec.
        An eviction is allowed if at least \"minAvailable\" pods selected by \"selector\" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying \"100%\".

        :param min_available: The min_available of this V1beta1PodDisruptionBudgetSpec.
        :type: str
        """

        self._min_available = min_available

    @property
    def selector(self):
        """
        Gets the selector of this V1beta1PodDisruptionBudgetSpec.
        Label query over pods whose evictions are managed by the disruption budget.

        :return: The selector of this V1beta1PodDisruptionBudgetSpec.
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1beta1PodDisruptionBudgetSpec.
        Label query over pods whose evictions are managed by the disruption budget.

        :param selector: The selector of this V1beta1PodDisruptionBudgetSpec.
        :type: V1LabelSelector
        """

        self._selector = selector

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
