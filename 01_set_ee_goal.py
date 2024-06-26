#!/usr/bin/env python3

import sys

from interbotix_common_modules.common_robot.robot import robot_shutdown, robot_startup
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
import numpy as np

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
    # Set the end-effector goal to two desired poses
    # e.g. (x=0.3, z=0.3) then (x=0.4, z=0.2)
    ##########################################################
    # YOUR CODE HERE
    bot.arm.go_to_sleep_pose()

    bot.arm.set_ee_pose_components(x=0.3, z=0.3)

    bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.1)
    ##########################################################

    robot_shutdown()


if __name__ == '__main__':
    main()
