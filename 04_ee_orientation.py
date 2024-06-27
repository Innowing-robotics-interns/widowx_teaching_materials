#!/usr/bin/env python3

import sys

from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

def deg2rad(deg):
    return round(deg * np.pi / 180.0, 3)

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
    # Change the end-effector orientation
    # e.g. go to (x=0.3, z=0.1) then set the orientation
    ##########################################################
    # YOUR CODE HERE
    bot.arm.go_to_home_pose(blocking=True)

    bot.arm.set_ee_pose_components(x=0.3, z=0.1, blocking=True)

    bot.arm.set_ee_cartesian_trajectory(pitch=deg2rad(89))
    bot.arm.set_ee_cartesian_trajectory(pitch=deg2rad(-89))

    bot.arm.go_to_sleep_pose(moving_time=3)
    ##########################################################

    robot_shutdown()


if __name__ == '__main__':
    main()
