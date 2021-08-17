"""
Author: Jade Cong
Date: 2021-05-13 11:52:14
LastEditTime: 2021-05-13 16:00:54
LastEditors: Jade Cong
Description: Tests ultrasound probe gripper on body contact scanning.
FilePath: /Workflows/Doing/PycharmProjects/aisono-robosuite/tests/test_grippers/test_ultrasound_probe_gripper.py
"""

"""
Tests aisono scanner on body contact scanning.
"""

import sys
sys.path.append("/home/jade/Documents/JadeCloud/Works/Aisono/Projects/Workflows/Doing/PycharmProjects/aisono-robosuite")

from robosuite.models.grippers import (
    UltrasoundProbeGripper,
    GripperTester,
)


def test_ultrasound_probe_gripper():
    ultrasound_probe_gripper_tester(False)


def ultrasound_probe_gripper_tester(render,
                          total_iters=1,
                          test_y=True):
    gripper = UltrasoundProbeGripper()
    tester = GripperTester(
        gripper=gripper,
        pos="0 0 0.3",
        quat="0 0 1 0",
        gripper_low_pos=-0.07,
        gripper_high_pos=0.02,
        render=render,
    )
    tester.start_simulation()
    tester.loop(total_iters=total_iters,
                test_y=test_y)


if __name__ == "__main__":
    ultrasound_probe_gripper_tester(True, 20, False)
