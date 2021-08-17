"""
Author: Jade Cong
Date: 2021-05-12 20:37:17
LastEditTime: 2021-05-13 20:33:06
LastEditors: Jade Cong
Description: Definition of Ultrasound Probe Gripper for Aubo i5 robot.
FilePath: /Workflows/Doing/PycharmProjects/aisono-robosuite/robosuite/models/grippers/ultrasound_probe_gripper.py
"""

import numpy as np
from robosuite.utils.mjcf_utils import xml_path_completion
from robosuite.models.grippers.gripper_model import GripperModel


class UltrasoundProbeGripperBase(GripperModel):
    """
    Aisono Ultrasound Probe Gripper with only one DoF(forward/backward).

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("grippers/ultrasound_probe_gripper.xml"), idn=idn)

    def format_action(self, action):
        return action

    @property
    def init_qpos(self):
        return None

    @property
    def _important_geoms(self):
        return {
            "scanner": ["geom_scanner_collision"],
            "scanner_probe": ["scanner_probe_contact_capsule"],
        }


class UltrasoundProbeGripper(UltrasoundProbeGripperBase):
    """
    Modifies UltrasoundProbeGripperBase to only take one action.
    """

    @property
    def speed(self):
        return 0.0

    @property
    def dof(self):
        return 0
