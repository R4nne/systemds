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
# Autogenerated From : scripts/builtin/randomForest.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES

def randomForest(X: OperationNode, Y: OperationNode, R: OperationNode, **kwargs: Dict[str, VALID_INPUT_TYPES]) -> OperationNode:
    """
    :param X: Feature matrix X; note that X needs to be both recoded and dummy coded
    :param Y: Label matrix Y; note that Y needs to be both recoded and dummy coded
    :param R: "          Matrix which for each feature in X contains the following information
    :param If: not provided by default all variables are assumed to be scale
    :param bins: Number of equiheight bins per scale feature to choose thresholds
    :param depth: Maximum depth of the learned tree
    :param num_leaf: Number of samples when splitting stops and a leaf node is added
    :param num_samples: Number of samples at which point we switch to in-memory subtree building
    :param num_trees: Number of trees to be learned in the random forest model
    :param subsamp_rate: Parameter controlling the size of each tree in the forest; samples are selected from a
    :param Poisson: parameter subsamp_rate (the default value is 1.0)
    :param feature_subset: Parameter that controls the number of feature used as candidates for splitting at each tree node
    :param as: of number of features in the dataset;
    :param by: root of features (i.e., feature_subset = 0.5) are used at each tree node
    :param impurity: Impurity measure: entropy or Gini (the default)
    :return: 'OperationNode' containing tree and each row contains the following information: & that leaf node j is supposed to predict & 7,8,... if j is categorical & chosen for j is categorical rows 7,8,... depict the value subset chosen for j & c containing the number of times samples are chosen in each tree of the random forest & from scale feature ids to global feature ids & from categorical feature ids to global feature ids 
    """
    
    X._check_matrix_op()
    Y._check_matrix_op()
    R._check_matrix_op()
    params_dict = {'X':X, 'Y':Y, 'R':R}
    params_dict.update(kwargs)
    return OperationNode(X.sds_context, 'randomForest', named_input_nodes=params_dict, output_type=OutputType.LIST, number_of_outputs=4, output_types=[OutputType.MATRIX, OutputType.MATRIX, OutputType.MATRIX, OutputType.MATRIX])


    