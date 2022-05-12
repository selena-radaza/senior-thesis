# Used for testing purposes.  Checking to see if Float32MultiArray
# values are being sent to the proper topics.
import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Vector3, Quaternion


def increment(p):

    for i in range(0, len(p.data)):
        p.data[i] += 0.1
    return p

def decrement(p):

    for i in range(0, len(p.data)):
        p.data[i] -= 0.1
    return p

def log_pub(tf, publisher, rate):
    rospy.loginfo(tf)
    publisher.publish(tf)
    #rate.sleep()


def talker():
    pub_upper_r = rospy.Publisher('/upper_r_transform', Float32MultiArray, queue_size=10) # Only one updating
    pub_lower_r = rospy.Publisher('/lower_r_transform', Float32MultiArray, queue_size=10)
    pub_wrist_r = rospy.Publisher('/wrist_r_transform', Float32MultiArray, queue_size=10)

    pub_upper_l = rospy.Publisher('/upper_l_transform', Float32MultiArray, queue_size=10)
    pub_lower_l = rospy.Publisher('/lower_l_transform', Float32MultiArray, queue_size=10)
    pub_wrist_l = rospy.Publisher('/wrist_l_transform', Float32MultiArray, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    generic = [0.0] * 16

    upper_arm_r = Float32MultiArray()
    upper_arm_r.data = generic

    lower_arm_r = Float32MultiArray()
    lower_arm_r.data = generic

    wrist_r = Float32MultiArray()
    wrist_r.data = generic

    upper_arm_l = Float32MultiArray()
    upper_arm_l.data = generic

    lower_arm_l = Float32MultiArray()
    lower_arm_l.data = generic

    wrist_l = Float32MultiArray()
    lower_arm_l.data = generic

    while not rospy.is_shutdown():

        upper_arm_r = increment(upper_arm_r)
        lower_arm_r = increment(lower_arm_r)
        wrist_r = increment(wrist_r)

        upper_arm_l = decrement(upper_arm_l)
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
