# Copyright (c) 2024-2025 Ziqi Fan
# SPDX-License-Identifier: Apache-2.0

"""Configuration for Arclab robots.

The following configurations are available:

* :obj:`ARCLAB_ARCDOG_CFG`: Arcdog robot with DC motor model for the legs


Reference: https://github.com/ruihuang1124/arcdog_ros
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg
from isaaclab.assets.articulation import ArticulationCfg

from robot_lab.assets import ISAACLAB_ASSETS_DATA_DIR

##
# Configuration
##


ARCLAB_ARCDOG_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAACLAB_ASSETS_DATA_DIR}/Robots/Arclab/Arcdog/arcdog.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.35),
        joint_pos={
            "a_10": 0.0,
            "a_11": 0.0,
            "a_8": -0.0,
            "a_9": -0.0,
            "a_4": 1.57,
            "a_6": 1.57,
            "a_0": 1.57,
            "a_2": 1.57,
            "a_5": 3.57,
            "a_7": 3.57,
            "a_1": 3.57,
            "a_3": 3.57,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "legs": DCMotorCfg(
            joint_names_expr=["a_.*"],
            effort_limit=40.0,
            saturation_effort=40.0,
            velocity_limit=21.0,
            stiffness=20.0,
            damping=0.5,
            friction=0.0,
        ),
    },
)
"""Configuration of Unitree A1 using DC motor.
"""
