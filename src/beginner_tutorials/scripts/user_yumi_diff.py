import rospy
import scipy
import threading
import numpy as np
from arm import RightArm
import time
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, Transform

from scipy.spatial.transform import Rotation as R

yumi_arm = RightArm('/upper_arm_r', '/lower_arm_r', '/wrist_r')
user_arm = RightArm('/user_upper_arm_r', '/user_lower_arm_r', '/user_wrist_r')

def calc_shoulder_diff(yumi_arm, user_arm):

    shoulder_diff_pos_x = yumi_arm.cur_pose_upper_r.position.x - user_arm.cur_pose_upper_r.position.x
    shoulder_diff_pos_y = yumi_arm.cur_pose_upper_r.position.y - user_arm.cur_pose_upper_r.position.y
    shoulder_diff_pos_z = yumi_arm.cur_pose_upper_r.position.z - user_arm.cur_pose_upper_r.position.z

    shoulder_diff_or_x = yumi_arm.cur_pose_upper_r.orientation.x - user_arm.cur_pose_upper_r.orientation.x
    shoulder_diff_or_y = yumi_arm.cur_pose_upper_r.orientation.y - user_arm.cur_pose_upper_r.orientation.y
    shoulder_diff_or_z = yumi_arm.cur_pose_upper_r.orientation.z - user_arm.cur_pose_upper_r.orientation.z

    pos_diff = (shoulder_diff_pos_x, shoulder_diff_pos_y, shoulder_diff_pos_z)
    or_diff = (shoulder_diff_or_x, shoulder_diff_or_y, shoulder_diff_or_z)

    return (pos_diff, or_diff)


def calc_elbow_diff(yumi_arm, user_arm):

    elbow_diff_pos_x = yumi_arm.cur_pose_lower_r.position.x - user_arm.cur_pose_lower_r.position.x
    elbow_diff_pos_y = yumi_arm.cur_pose_lower_r.position.y - user_arm.cur_pose_lower_r.position.y
    elbow_diff_pos_z = yumi_arm.cur_pose_lower_r.position.z - user_arm.cur_pose_lower_r.position.z

    elbow_diff_or_x = yumi_arm.cur_pose_lower_r.orientation.x - user_arm.cur_pose_lower_r.orientation.x
    elbow_diff_or_y = yumi_arm.cur_pose_lower_r.orientation.y - user_arm.cur_pose_lower_r.orientation.y
    elbow_diff_or_z = yumi_arm.cur_pose_lower_r.orientation.z - user_arm.cur_pose_lower_r.orientation.z

    pos_diff = (elbow_diff_pos_x, elbow_diff_pos_y, elbow_diff_pos_z)
    or_diff = (elbow_diff_or_x, elbow_diff_or_y, elbow_diff_or_z)

    return (pos_diff, or_diff)

def calc_wrist_diff(yumi_arm, user_arm):

    wrist_diff_pos_x = yumi_arm.cur_pose_wrist_r.position.x - user_arm.cur_pose_wrist_r.position.x
    wrist_diff_pos_y = yumi_arm.cur_pose_wrist_r.position.y - user_arm.cur_pose_wrist_r.position.y
    wrist_diff_pos_z = yumi_arm.cur_pose_wrist_r.position.z - user_arm.cur_pose_wrist_r.position.z

    wrist_diff_or_x = yumi_arm.cur_pose_wrist_r.orientation.x - user_arm.cur_pose_wrist_r.orientation.x
    wrist_diff_or_y = yumi_arm.cur_pose_wrist_r.orientation.y - user_arm.cur_pose_wrist_r.orientation.y
    wrist_diff_or_z = yumi_arm.cur_pose_wrist_r.orientation.z - user_arm.cur_pose_wrist_r.orientation.z

    pos_diff = (wrist_diff_pos_x, wrist_diff_pos_y, wrist_diff_pos_z)
    or_diff = (wrist_diff_or_x, wrist_diff_or_y, wrist_diff_or_z)

    return (pos_diff, or_diff)

def calc_diff(yumi_arm, user_arm):

    shoulder_diff = calc_shoulder_diff(yumi_arm, user_arm)
    elbow_diff = calc_elbow_diff(yumi_arm, user_arm)
    wrist_diff = calc_elbow_diff(yumi_arm, user_arm)

    print("\nShoulder diff: ", shoulder_diff)
    print("\nElbow diff: ", elbow_diff)
    print("\nWrist diff: ", wrist_diff)


if __name__ == '__main__':
    while True:
        calc_diff(yumi_arm, user_arm)
        time.sleep(5)
