import rospy
import scipy
import numpy as np
import random
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, Transform
from arm import RightArm

from scipy.spatial.transform import Rotation as R

pub_upper_r = rospy.Publisher('/user_upper_arm_r', Pose, queue_size=10)
pub_lower_r = rospy.Publisher('/user_lower_arm_r', Pose, queue_size=10)
pub_wrist_r = rospy.Publisher('/user_wrist_r', Pose, queue_size=10)

rospy.init_node('human', anonymous=True)
rate = rospy.Rate(10)
error_val = 0.1

def shoulder_callback(msg):
    # Random value for human error

    p = Pose()
    p.orientation.x = msg.orientation.x
    p.orientation.y = msg.orientation.y
    p.orientation.z = msg.orientation.z + error_val

    p.position.x = msg.position.x
    p.position.y = msg.position.y
    p.position.z = msg.position.z

    pub_upper_r.publish(p)

def elbow_callback(msg):
    val1 = random.random()
    val2 = random.random()

    p = Pose()
    p.orientation.x = msg.orientation.x
    p.orientation.y = msg.orientation.y
    p.orientation.z = msg.orientation.z

    p.position.x = msg.position.x + val1
    p.position.y = msg.position.y + val1
    p.position.z = msg.position.z + val1
    pub_lower_r.publish(p)

def wrist_callback(msg):
    val1 = random.random()
    val2 = random.random()

    p = Pose()
    p.orientation.x = msg.orientation.x + val2
    p.orientation.y = msg.orientation.y + val2
    p.orientation.z = msg.orientation.z + val2

    p.position.x = msg.position.x + val1
    p.position.y = msg.position.y + val1
    p.position.z = msg.position.z + val1
    pub_wrist_r.publish(p)



def listener():
    sub_shoulder = rospy.Subscriber('/upper_arm_r', Pose, shoulder_callback)
    sub_elbow = rospy.Subscriber('/lower_arm_r', Pose, elbow_callback)
    sub_wrist = rospy.Subscriber('/wrist_r', Pose, wrist_callback)

    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
