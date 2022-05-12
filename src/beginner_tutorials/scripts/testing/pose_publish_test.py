# Testing pose publishing with Unity.
import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion

def increment(p):
    p.orientation.x += 0.1
    p.orientation.y += 0.1
    p.orientation.z += 0.1

    p.position.x += 0.1;
    p.position.y += 0.1;
    p.position.z += 0.1;
    return p

def log_pub(pose, publisher, rate):
    rospy.loginfo(pose)
    publisher.publish(pose)
    rate.sleep()

def talker():
    pub_upper_r = rospy.Publisher('/upper_arm_r', Pose, queue_size=10)
    pub_lower_r = rospy.Publisher('/lower_arm_r', Pose, queue_size=10)
    pub_wrist_r = rospy.Publisher('/wrist_r', Pose, queue_size=10)

    pub_upper_l = rospy.Publisher('/upper_arm_l', Pose, queue_size=10)
    pub_lower_l = rospy.Publisher('/lower_arm_l', Pose, queue_size=10)
    pub_wrist_l = rospy.Publisher('/wrist_l', Pose, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    upper_arm_r = Pose()
    upper_arm_r.position = Point(0.0, 0.0, 0.0)
    upper_arm_r.orientation = Quaternion(0.0, 0.0, 0.0, 1)

    lower_arm_r = Pose()
    lower_arm_r.position = Point(0.0, 0.0, 0.0)
    lower_arm_r.orientation = Quaternion(0.0, 0.0, 0.0, 1)

    wrist_r = Pose()
    wrist_r.position = Point(0.0, 0.0, 0.0)
    wrist_r.orientation = Quaternion(0.0, 0.0, 0.0, 1)

    upper_arm_l = Pose()
    upper_arm_l.position = Point(0.0, 0.0, 0.0)
    upper_arm_l.orientation = Quaternion(0.0, 0.0, 0.0, 1)

    lower_arm_l = Pose()
    lower_arm_l.position = Point(0.0, 0.0, 0.0)
    lower_arm_l.orientation = Quaternion(0.0, 0.0, 0.0, 1)

    wrist_l = Pose()
    wrist_l.position = Point(0.0, 0.0, 0.0)
    wrist_l.orientation = Quaternion(0.0, 0.0, 0.0, 1)

    while not rospy.is_shutdown():

        upper_arm_r = increment(upper_arm_r)
        lower_arm_r = increment(lower_arm_r)
        wrist_r = increment(wrist_r)

        upper_arm_l = increment(upper_arm_l)
        lower_arm_l = increment(lower_arm_l)
        wrist_l = increment(wrist_l)

        log_pub(upper_arm_r, pub_upper_r, rate)
        log_pub(upper_arm_l, pub_upper_l, rate)

        log_pub(lower_arm_r, pub_lower_r, rate)
        log_pub(lower_arm_l, pub_lower_l, rate)

        log_pub(wrist_l, pub_wrist_l, rate)
        log_pub(wrist_r, pub_wrist_r, rate)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
