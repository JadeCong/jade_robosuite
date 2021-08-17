"""
Author: Jade Cong
Date: 2021-05-13 11:53:01
LastEditTime: 2021-05-13 16:22:17
LastEditors: Jade Cong
Description: Tests the basic interface of aubo i5 robot.
FilePath: /Workflows/Doing/PycharmProjects/aisono-robosuite/tests/test_robots/test_aubo_robot.py
"""

"""
Tests the basic interface of aubo i5 robot.

This runs some basic sanity checks on the robots, namely, checking that:
    - Verifies that aubo i5 single-arm robots has properly defined contact geoms.

Obviously, if an environment crashes during runtime, that is considered a failure as well.
"""

import sys
sys.path.append("/home/jade/Documents/JadeCloud/Works/Aisono/Projects/Workflows/Doing/PycharmProjects/aisono-robosuite")

from robosuite.robots import ROBOT_CLASS_MAPPING
from robosuite.robots import SingleArm


def test_aubo_single_arm_robot():
    for name, robot in ROBOT_CLASS_MAPPING.items():
        if name == "Aubo":
            if robot == SingleArm:
                print(f'Testing {name}')
                _test_contact_geoms(robot(name))


def _test_contact_geoms(robot):
    robot.load_model()
    contact_geoms = robot.robot_model._contact_geoms
    for geom in contact_geoms:
        assert isinstance(geom, str), f"The geom {geom} is of type {type(geom)}, but should be {type('placeholder')}"


if __name__ == "__main__":
    test_aubo_single_arm_robot()
    print("Aubo i5 robot tests completed.")
