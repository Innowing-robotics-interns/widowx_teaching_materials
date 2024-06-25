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
    # Control a single joint to rotate
    # Search for the appropriate function under `src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/interbotix_xs_modules/xs_robot/arm.py`
    # Hint: joint names are [waist, shoulder, elbow, forearm_roll, wrist_angle, wrist_rotate, gripper]
    ##########################################################
    # YOUR CODE HERE
    bot.arm.go_to_home_pose()
    
    bot.arm.set_single_joint_position(joint_name='waist', position=deg2rad(-90))
    bot.arm.set_single_joint_position(joint_name='forearm_roll', position=deg2rad(-45))
    bot.arm.set_single_joint_position(joint_name='wrist_angle', position=deg2rad(45))

    bot.arm.set_single_joint_position(joint_name='forearm_roll', position=deg2rad(0))

    bot.arm.go_to_sleep_pose()
    ##########################################################

    robot_shutdown()


if __name__ == '__main__':
    main()
