import rospy
import scipy
import threading
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, Transform

class RightArm:


    def get_first_update_upper_r():
        return firstUpdateUpperR

    def set_first_update_upper_r(b):
        global firstUpdateUpperR
        firstUpdateUpperR = b

    def get_first_update_lower_r():
        return firstUpdateLowerR

    def set_first_update_lower_r(b):
        firstUpdateLowerR = b

    def get_first_update_wrist_r():
        return firstUpdateWristR

    def set_first_update_wrist_r(b):
        firstUpdateWristR = b

    def get_cur_pose_upper_r():
        return cur_pose_upper_r

    def get_cur_pose_lower_r():
        return cur_pose_lower_r

    def get_cur_pose_wrist_r():
        return cur_pose_wrist_r



    def __init__(self, shoulder_pose_topic, elbow_pose_topic, wrist_pose_topic):


        self.cur_pose_upper_r = Pose()
        self.cur_pose_lower_r = Pose()
        self.cur_pose_wrist_r = Pose()

        self.firstUpdateUpperR = True
        self.firstUpdateLowerR = True
        self.firstUpdateWristR = True

        rospy.init_node('arm', anonymous=True)
        rate = rospy.Rate(10)

        def shoulder_callback(msg):
            self.cur_pose_upper_r = msg

        def elbow_callback(msg):
            self.cur_pose_lower_r = msg

        def wrist_callback(msg):
            self.cur_pose_wrist_r = msg

        self.sub_shoulder_pose = rospy.Subscriber(shoulder_pose_topic, Pose, shoulder_callback)
        self.sub_elbow_pose = rospy.Subscriber(elbow_pose_topic, Pose, elbow_callback)
        self.sub_wrist_pose = rospy.Subscriber(wrist_pose_topic, Pose, wrist_callback)
