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
# Autogenerated From : scripts/builtin/km.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES

def km(X: OperationNode, TE: OperationNode, GI: OperationNode, SI: OperationNode, **kwargs: Dict[str, VALID_INPUT_TYPES]) -> OperationNode:
    """
    :param X: Input matrix X containing the survival data: 
    :param number: (categorical features) for grouping and/or stratifying 
    :param TE: Column indices of X which contain timestamps (first entry) and event
    :param GI: Column indices of X corresponding to the factors to be used for grouping
    :param SI: Column indices of X corresponding to the factors to be used for stratifying
    :param alpha: Parameter to compute 100*(1-alpha)% confidence intervals for the survivor
    :param function: median 
    :param err_type: Parameter to specify the error type according to "greenwood" (the default) or "peto"
    :param conf_type: Parameter to modify the confidence interval; "plain" keeps the lower and 
    :param upper: the confidence interval unmodified, "log" (the default)
    :param corresponds: transformation and "log-log" corresponds to the
    :param test_type: If survival data for multiple groups is available specifies which test to
    :param perform: survival data across multiple groups: "none" (the default)
    :return: 'OperationNode' containing 7 consecutive columns in km corresponds to a unique combination of groups and strata in the data  & schema & whose dimension depends on the number of groups (g) and strata (s) in the data (k denotes the number  & for grouping  ,i.e., ncol(gi) and l denotes the number of factors used for stratifying, i.e., ncol(si)) & of groups and strata is equal to 1, m will have 4 columns with  & data from multiple groups available and ttype=log-rank or wilcoxon, a 1 x 4 matrix t and an g x 5 matrix t_groups_oe with 
    """
    
    X._check_matrix_op()
    TE._check_matrix_op()
    GI._check_matrix_op()
    SI._check_matrix_op()
    params_dict = {'X':X, 'TE':TE, 'GI':GI, 'SI':SI}
    params_dict.update(kwargs)
    return OperationNode(X.sds_context, 'km', named_input_nodes=params_dict, output_type=OutputType.LIST, number_of_outputs=4, output_types=[OutputType.MATRIX, OutputType.MATRIX, OutputType.MATRIX, OutputType.MATRIX])


    