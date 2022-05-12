# Sending a rotation around a specified axis.  Used to determine how rotations appear in Unity.
import rospy
import scipy
import math
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, Transform
from joint import Joint
from scipy.spatial.transform import Rotation as R
import quaternion

pub = rospy.Publisher('/upper_arm_r', Pose, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10)


def rotate_x(deg):
    r_matrix_array = np.reshape(np.array([1.0, 0, 0,
                        0, math.cos(deg), -math.sin(deg),
                        0, math.sin(deg), math.cos(deg)], dtype=Float32), (3, 3))
    r_matrix = R.from_matrix(r_matrix_array)
    rq = r_matrix.as_quat()
    return rq

def rotate_y(deg):
    r_matrix_array = np.reshape(np.array([math.cos(deg), 0, math.sin(deg),
                        0, 1, 0,
                        -math.sin(deg), 0, math.cos(deg)], dtype=Float32), (3, 3))
    r_matrix = R.from_matrix(r_matrix_array)
    rq = r_matrix.as_quat()
    return rq

def rotate_z(deg):
    r_matrix_array = np.reshape(np.array([math.cos(deg), -math.sin(deg), 0,
                    math.sin(deg), math.cos(deg), 0,
                    0, 0, 1], dtype=Float32), (3, 3))
    r_matrix = R.from_matrix(r_matrix_array)
    rq = r_matrix.as_quat()

    return rq

def create_pose(quat):
    p = Pose()
    p.orientation.x = quat[0]
    p.orientation.y = quat[1]
    p.orientation.z = quat[2]
    p.orientation.w = quat[3]


    return p


if __name__ == '__main__':
    # quat = rotate_x(90)
    # quat = rotate_y(90)
    quat = rotate_z(90)
    p = create_pose(quat)
    pub.publish(p)
