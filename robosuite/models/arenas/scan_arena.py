"""
Author: Jade Cong
Date: 2021-07-05 09:00:00
LastEditTime: 2021-07-06 10:00:00
LastEditors: Jade Cong
Description: Class of Scan Arena.
FilePath: /PycharmProjects/aisono-robosuite/robosuite/models/arenas/scan_arena.py
"""

import numpy as np
from robosuite.models.arenas import Arena
from robosuite.utils.mjcf_utils import xml_path_completion
from robosuite.utils.mjcf_utils import array_to_string, string_to_array


class ScanArena(Arena):
    """
    Workspace that contains host machine, bed body and bed mat.

    Args:
        bed_full_size (3-tuple): (L,W,H) full dimensions of the bed
        bed_friction (3-tuple): (sliding, torsional, rolling) friction parameters of the bed
        bed_offset (3-tuple): (x,y,z) offset from center of arena when placing bed.
        xml (str): xml file to load arena
    """
    def __init__(
        self,
        bed_full_size=(1.6, 0.6, 0.6),
        bed_friction=(1, 0.005, 0.0001),
        bed_offset=(0, 0, 0.125),
        xml="arenas/scan_arena.xml",
    ):
        super().__init__(xml_path_completion(xml))

        self.bed_full_size = np.array(bed_full_size)
        self.bed_half_size = self.bed_full_size / 2
        self.bed_friction = bed_friction
        self.bed_offset = bed_offset
        self.center_pos = self.bottom_pos + np.array([0, 0, self.bed_full_size[2]]) - self.bed_offset

        self.configure_location()

    def configure_location(self):
        """Configures correct locations for this arena"""
        self.floor.set("pos", array_to_string(self.bottom_pos))

    @property
    def bed_top_abs(self):
        """
        Grabs the absolute position of bed top

        Returns:
            np.array: (x,y,z) bed position
        """
        return string_to_array(self.floor.get("pos")) + np.array([0, 0, self.bed_full_size[2]])
