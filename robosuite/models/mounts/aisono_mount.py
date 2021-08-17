"""
Author: Jade Cong
Date: 2021-05-14 14:06:44
LastEditTime: 2021-05-14 15:57:28
LastEditors: Jade Cong
Description: Aisono Mount for ultrasound scanning.
FilePath: /Workflows/Doing/PycharmProjects/aisono-robosuite/robosuite/models/mounts/aisono_mount.py
"""

import numpy as np
from robosuite.utils.mjcf_utils import xml_path_completion
from robosuite.models.mounts.mount_model import MountModel


class AisonoMount(MountModel):
    """
    Mount used for Aubo i5 Robot. Includes a host machine, a bed body and a bed mat.

    Args:
        idn (int or str): Number or some other unique identification string for this mount instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("mounts/aisono_mount.xml"), idn=idn)

    @property
    def top_offset(self):
        return np.array((0, -0.34, 0.88))

    @property
    def horizontal_radius(self):
        # TODO: This may be inaccurate; just a placeholder for now
        return 0.8
