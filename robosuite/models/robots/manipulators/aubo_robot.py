"""
Author: Jade Cong
Date: 2021-05-12 20:06:44
LastEditTime: 2021-05-16 17:39:51
LastEditors: Jade Cong
Description: Definition of Aubo Robot.
FilePath: /Workflows/Doing/PycharmProjects/aisono-robosuite/robosuite/models/robots/manipulators/aubo_robot.py
"""

import numpy as np
from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion


class Aubo(ManipulatorModel):
    """
    Aubo(type:i5) is a collaborate robot designed by Aubo Inc. in china.

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("robots/aubo/robot.xml"), idn=idn)

        # Set joint damping
        self.set_joint_attribute(attrib="damping", values=np.array((50, 50, 50, 50, 50, 50)))

    @property
    def default_mount(self):
        # return "RethinkMount"
        return "AisonoMount"

    @property
    def default_gripper(self):
        # return "PandaGripper"
        return "UltrasoundProbeGripper"

    @property
    def default_controller_config(self):
        return "default_aubo"

    @property
    def init_qpos(self):
        # return np.array([0, -np.pi / 4.0, np.pi / 4.0, -np.pi / 2.0 - np.pi / 3.0, 0.00, np.pi - 0.2])
        return np.array([0, 0, 0, 0, 0])

    @property
    def base_xpos_offset(self):
        # return {
        #     "bins": (-0.5, -0.1, 0),
        #     "empty": (-0.6, 0, 0),
        #     "table": lambda table_length: (-0.16 - table_length / 2, 0, 0)
        # }
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
            "scan": (0, -0.95, 0.58)
        }

    @property
    def top_offset(self):
        return np.array((0, 0, 0.8))

    @property
    def _horizontal_radius(self):
        return 0.8

    @property
    def arm_type(self):
        return "single"
