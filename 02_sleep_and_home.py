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
    # Move back and forth between home and sleep pose, for 3 cycles.
    # Search for the appropriate function for home and sleep pose under: 
    # `src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/interbotix_xs_modules/xs_robot/arm.py`
    ##########################################################
    # YOUR CODE HERE
    for _ in range(3):
        bot.arm.go_to_home_pose()
        bot.arm.go_to_sleep_pose()
    ##########################################################

    robot_shutdown()


if __name__ == '__main__':
    main()
