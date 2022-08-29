# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/csplineCG.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES


def csplineCG(X: Matrix,
              Y: Matrix,
              inp_x: float,
              **kwargs: Dict[str, VALID_INPUT_TYPES]):
    """
     Builtin that solves cubic spline interpolation using conjugate gradient algorithm
    
    
    
    :param X: 1-column matrix of x values knots. It is assumed that x values are
        monotonically increasing and there is no duplicates points in X
    :param Y: 1-column matrix of corresponding y values knots
    :param inp_x: the given input x, for which the cspline will find predicted y.
    :param tol: Tolerance (epsilon); conjugate graduent procedure terminates early if
        L2 norm of the beta-residual is less than tolerance * its initial norm
    :param maxi: Maximum number of conjugate gradient iterations, 0 = no maximum
    :return: Predicted value
    :return: Matrix of k parameters
    """

    params_dict = {'X': X, 'Y': Y, 'inp_x': inp_x}
    params_dict.update(kwargs)
    
    vX_0 = Matrix(X.sds_context, '')
    vX_1 = Matrix(X.sds_context, '')
    output_nodes = [vX_0, vX_1, ]

    op = MultiReturn(X.sds_context, 'csplineCG', output_nodes, named_input_nodes=params_dict)

    vX_0._unnamed_input_nodes = [op]
    vX_1._unnamed_input_nodes = [op]

    return op