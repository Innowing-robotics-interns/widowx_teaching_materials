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
    # Perform a series of action together with the gripper
    # Search for the appropriate function to control gripper under:
    #   `src/interbotix_ros_toolboxes/interbotix_xs_toolbox/interbotix_xs_modules/interbotix_xs_modules/xs_robot/gripper.py`
    ##########################################################
    # YOUR CODE HERE
    bot.arm.go_to_home_pose()
    bot.gripper.release()

    bot.arm.set_ee_pose_components(x=0.15, z=0.1, roll=deg2rad(90), pitch=deg2rad(90), blocking=True)
    bot.gripper.grasp(3)
    
    bot.arm.set_ee_pose_components(x=0.2, y=0.3, z=0.1, yaw=deg2rad(0), blocking=True)
    bot.gripper.release(3)
    
    bot.arm.go_to_sleep_pose(moving_time=3)
    ##########################################################

    robot_shutdown()


if __name__ == '__main__':
    main()
