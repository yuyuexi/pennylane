# Copyright 2018-2020 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This module contains the AutogradBox implementation of the TensorBox API.
"""
# pylint: disable=no-member
import pennylane as qml
from pennylane import numpy as np


class AutogradBox(qml.proc.TensorBox):
    """Implements the :class:`~.TensorBox` API for ``pennylane.numpy`` tensors.

    For more details, please refer to the :class:`~.TensorBox` documentation.
    """

    def abs(self):
        return AutogradBox(np.abs(self.data))

    def angle(self):
        return AutogradBox(np.angle(self.data))

    arcsin = qml.proc.tensorbox.wrap_output(lambda self: np.arcsin(self.data))

    @staticmethod
    def astensor(tensor):
        return np.tensor(tensor)

    def cast(self, dtype):
        return AutogradBox(np.tensor(self.data, dtype=dtype))

    @staticmethod
    def concatenate(values, axis=0):
        return AutogradBox(np.concatenate(AutogradBox.unbox_list(values), axis=axis))

    def dot(self, other):
        if other.ndim == 2 and self.data.ndim == 2:
            return AutogradBox(self.data @ other)

        if other.ndim == 0 and self.data.ndim == 0:
            return AutogradBox(self.data * other)

        return AutogradBox(np.dot(self.data, other))

    def expand_dims(self, axis):
        return AutogradBox(np.expand_dims(self.data, axis=axis))

    @property
    def interface(self):
        return "autograd"

    def numpy(self):
        if hasattr(self.data, "_value"):
            return self.data._value

        return self.data.numpy()

    def ones_like(self):
        return AutogradBox(np.ones_like(self.data))

    @property
    def requires_grad(self):
        return self.data.requires_grad

    @property
    def shape(self):
        return self.data.shape

    def sqrt(self):
        return AutogradBox(np.sqrt(self.data))

    @staticmethod
    def stack(values, axis=0):
        return AutogradBox(np.stack(AutogradBox.unbox_list(values), axis=axis))

    def sum(self, axis=None, keepdims=False):
        return AutogradBox(np.sum(self.data, axis=axis, keepdims=keepdims))

    def take(self, indices, axis=None):
        if isinstance(indices, qml.proc.TensorBox):
            indices = indices.numpy()

        indices = self.astensor(indices)

        if axis is None:
            return AutogradBox(self.data.flatten()[indices])

        fancy_indices = [slice(None)] * axis + [indices]
        return AutogradBox(self.data[fancy_indices])

    @property
    def T(self):
        return AutogradBox(self.data.T)

    @staticmethod
    def where(condition, x, y):
        return AutogradBox(np.where(condition, *AutogradBox.unbox_list([x, y])))