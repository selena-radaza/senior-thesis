# Transform publishing for testing purposes.
import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Transform, Vector3, Quaternion


def increment(p):
    p.rotation.x += 0.1
    p.rotation.y += 0.1
    p.rotation.z += 0.1

    p.translation.x += 0.1;
    p.translation.y += 0.1;
    p.translation.z += 0.1;
    return p

def log_pub(tf, publisher, rate):
    rospy.loginfo(tf)
    publisher.publish(tf)
    rate.sleep()

def talker():
    pub_upper_r = rospy.Publisher('/upper_r_transform', Transform, queue_size=10)
    pub_lower_r = rospy.Publisher('/lower_r_transform', Transform, queue_size=10)
    pub_wrist_r = rospy.Publisher('/wrist_r_transform', Transform, queue_size=10)

    pub_upper_l = rospy.Publisher('/upper_l_transform', Transform, queue_size=10)
    pub_lower_l = rospy.Publisher('/lower_l_transform', Transform, queue_size=10)
    pub_wrist_l = rospy.Publisher('/wrist_l_transform', Transform, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    upper_arm_r = Transform()
    upper_arm_r.translation = Vector3(0.0, 0.0, 0.0)
    upper_arm_r.rotation = Quaternion(0.0, 0.0, 0.0, 1)

    lower_arm_r = Transform()
    lower_arm_r.translation = Vector3(0.0, 0.0, 0.0)
    lower_arm_r.rotation = Quaternion(0.0, 0.0, 0.0, 1)

    wrist_r = Transform()
    wrist_r.translation = Vector3(0.0, 0.0, 0.0)
    wrist_r.rotation = Quaternion(0.0, 0.0, 0.0, 1)

    upper_arm_l = Transform()
    upper_arm_l.translation = Vector3(0.0, 0.0, 0.0)
    upper_arm_l.rotation = Quaternion(0.0, 0.0, 0.0, 1)

    lower_arm_l = Transform()
    lower_arm_l.translation = Vector3(0.0, 0.0, 0.0)
    lower_arm_l.rotation = Quaternion(0.0, 0.0, 0.0, 1)

    wrist_l = Transform()
    wrist_l.translation = Vector3(0.0, 0.0, 0.0)
    wrist_l.rotation = Quaternion(0.0, 0.0, 0.0, 1)

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
