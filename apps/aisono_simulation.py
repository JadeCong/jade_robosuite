"""
Author: Jade Cong
Date: 2021-06-23 09:00:00
LastEditTime: 2021-06-23 10:00:00
LastEditors: Jade Cong
Description: Aisono Simulation of Soft Object Manipulation in MuJoCo.
FilePath: /PycharmProjects/aisono-robosuite/apps/aisono_simulation.py
"""

import sys
import os
import pytest
import time
import math
import numpy as np
import traceback
import glfw
import copy

from mujoco_py import ignore_mujoco_warnings as mj_ignore_warnings
from mujoco_py import MujocoException
from mujoco_py import const as mj_const
from mujoco_py import functions as mj_fn
from mujoco_py import load_model_from_path, load_model_from_mjb, load_model_from_xml
from mujoco_py import MjRenderContext, MjRenderContextOffscreen, MjRenderContextWindow, MjBatchRenderer, GlfwContext
from mujoco_py import MjSim, MjSimState
from mujoco_py import MjViewer, MjViewerBasic

from mujoco_py.cymj import PyMjModel, PyMjData
from mujoco_py.cymj import PyMjvScene, PyMjvCamera, PyMjvOption, PyMjvPerturb
from mujoco_py.cymj import PyMjUI, PyMjuiState, PyMjrContext, PyMjrRect
from mujoco_py.modder import LightModder, CameraModder, MaterialModder, TextureModder


class HMD():  # anonymous object we can set fields on
    """
    Normally global variables aren't used like this in python,
    but we want to be as close as possible to the original file.
    """
    pass


model = None
sim = None
modder = None
hmd = HMD()


def render_callback(sim, viewer):
    """
    Render callback function for update texture of scene objects.
    """
    global modder
    if modder is None:
        modder = TextureModder(sim)
    for name in sim.model.geom_names:
        modder.rand_all(name)


@pytest.mark.requires_rendering
@pytest.mark.requires_glfw
def mujoco_sim():
    """
    Simulation test function.
    """
    # Statement of global variables
    global model, sim

    # Load the simulation model
    # model = load_model_from_path("../robosuite/models/assets/grippers/ultrasound_probe_gripper.xml")
    # model = load_model_from_path("../robosuite/models/assets/robots/aubo/aisono_aubo.xml")
    # model = load_model_from_path("../robosuite/models/assets/mounts/aisono_mount.xml")
    # model = load_model_from_path("/home/jade/Documents/JadeCloud/Works/Aisono/Projects/Workflows/Doing/PycharmProjects/"
    #                              "aisono-robosuite/apps/resources/scenes/aisono_simulation.xml")
    model = load_model_from_path("./resources/scenes/aisono_simulation.xml")
    # model = load_model_from_mjb("./resources/scenes/mjmodel.mjb")

    # Construct the simulation and viewer
    # sim = MjSim(model, render_callback=render_callback)
    sim = MjSim(model)
    viewer = MjViewer(sim)

    # Simulation step update and viewer scene render
    step = 0
    while True:
        # TODO: Update the simulation scene states(robots and objects)
        # t = time.time()
        # x, y = math.cos(t), math.sin(t)
        # viewer.add_marker(type=4, pos=np.array([y, x, 0.2]), label="sphere")
        # sim.data.ctrl[0] = math.cos(t / 10.) * 0.01
        # sim.data.ctrl[1] = math.sin(t / 10.) * 0.01

        # TODO: Handle events (calls all callbacks)

        # Simulation forward and render the scene
        # sim.forward()
        sim.step()
        viewer.render()

        # Check the step whether need to stop
        step += 1
        if step > 100000 and os.getenv('TESTING') is not None:
            break

    # Delete everything we allocated
    mj_fn.mj_deleteModel(model)

    # Deactivate MuJoCo
    mj_fn.mj_deactivate()


if __name__ == "__main__":
    print("Simulation Starting...")
    mujoco_sim()
    print("Simulation Terminated!")
