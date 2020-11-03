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
"""This module contains the NumpyBox implementation of the TensorBox API.
"""
import numpy as np

from .tensorbox import TensorBox


class NumpyBox(TensorBox):
    """Implements the :class:`~.TensorBox` API for ``numpy.ndarray``.

    For more details, please refer to the :class:`~.TensorBox` documentation.
    """

    def expand_dims(self, axis):
        return NumpyBox(np.expand_dims(self.unbox(), axis=axis))

    def numpy(self):
        return self.unbox()

    def ones_like(self):
        return NumpyBox(np.ones_like(self.unbox()))

    @staticmethod
    def stack(values, axis=0):
        return NumpyBox(np.stack(NumpyBox.unbox_list(values), axis=axis))

    @property
    def shape(self):
        return self.unbox().shape

    @property
    def T(self):
        return NumpyBox(self.unbox().T)
