import rospy
import scipy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, Transform
from joint import Joint
from joint_matrix_math import Joint_Math
from scipy.spatial.transform import Rotation as R

rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10)

def listener():
    shoulder = Joint_Math('/j1r', '/j2r', '/upper_arm_r', 'shoulder', False)
    human_shoulder = Joint_Math('/j1r', '/j2r', '/human_upper_arm_r', 'human_shoulder', True)

    elbow = Joint_Math('/j4r', '', '/lower_arm_r', 'elbow', False)
    human_elbow = Joint_Math('/j4r', '', '/human_lower_arm_r', 'human_elbow', True)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
