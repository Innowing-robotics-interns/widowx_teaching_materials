#!/usr/bin/env python3

import sys

from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

"""
This script makes the end-effector perform pick, pour, and place tasks.
Note that this script may not work for every arm as it was designed for the wx250.
Make sure to adjust commanded joint positions and poses as necessary.

To get started, open a terminal and type:

    ros2 launch interbotix_xsarm_control xsarm_control.launch.py robot_model:=wx250s

Then change to this directory and type:

    python3 00_set_ee_goal.py
"""

def main():
    bot = InterbotixManipulatorXS(
        robot_model='wx250s',
        group_name='arm',
        gripper_name='gripper',
    )

    robot_startup()

    if (bot.arm.group_info.num_joints < 5):
        bot.get_node().logfatal(
            'This demo requires the robot to have at least 5 joints!'
        )
        robot_shutdown()
        sys.exit()
    
    ##########################################################
    # Set the end-effector goal to a desired pose
    # e.g. x=0.3, z=0.3
    ##########################################################
    # YOUR CODE HERE

    bot.arm.set_ee_pose_components(x=0.3, z=0.3)

    ##########################################################

    robot_shutdown()


if __name__ == '__main__':
    main()
