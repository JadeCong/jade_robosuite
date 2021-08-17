"""
Tests two finger gripper and left two finger gripper on grabbing task
"""

import sys
sys.path.append("/home/jade/Documents/JadeCloud/Works/Aisono/Projects/Workflows/Doing/PycharmProjects/aisono-robosuite")

from robosuite.models.grippers import (
    RethinkGripper,
    GripperTester,
)


def test_two_finger():
    two_finger_tester(False)


def two_finger_tester(render,
                      total_iters=1,
                      test_y=True):
    gripper = RethinkGripper()
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
    two_finger_tester(True, 20, True)
