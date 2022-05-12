import rospy
import scipy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion, Transform

from scipy.spatial.transform import Rotation as R

pub_upper_r = rospy.Publisher('/user_upper_arm_r', Pose, queue_size=10)
pub_lower_r = rospy.Publisher('/user_lower_arm_r', Pose, queue_size=10)
pub_wrist_r = rospy.Publisher('/user_wrist_r', Pose, queue_size=10)

pub_upper_l = rospy.Publisher('/user_upper_arm_l', Pose, queue_size=10)
pub_lower_l = rospy.Publisher('/user_lower_arm_l', Pose, queue_size=10)
pub_wrist_l = rospy.Publisher('/user_wrist_l', Pose, queue_size=10)

cur_pose_upper_r = Pose()
cur_pose_lower_r = Pose()
cur_pose_wrist_r = Pose()

firstUpdateUpperR = True
firstUpdateLowerR = True
firstUpdateWristR = True

rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10)

def get_first_update_upper_r():
    return firstUpdateUpperR

def set_first_update_upper_r(b):
    global firstUpdateUpperR
    firstUpdateUpperR = b

def get_first_update_lower_r():
    return firstUpdateLowerR

def set_first_update_lower_r(b):
    global firstUpdateLowerR
    firstUpdateLowerR = b

def get_first_update_wrist_r():
    return firstUpdateWristR

def set_first_update_wrist_r(b):
    global firstUpdateWristR
    firstUpdateWristR = b


##################################


def get_cur_pose_upper_r():
    return cur_pose_upper_r

def set_cur_pose_upper_r(p):
    global cur_pose_upper_r
    cur_pose_upper_r = p

def get_cur_pose_lower_r():
    return cur_pose_lower_r

def set_cur_pose_lower_r(p):
    global cur_pose_lower_r
    cur_pose_lower_r = p

def get_cur_pose_wrist_r():
    return cur_pose_wrist_r

def set_cur_pose_wrist_r(p):
    global cur_pose_wrist_r
    cur_pose_wrist_r = p

def transform_to_pose(tf):
    p = Pose()
    p.position = tf.translation
    p.orientation = tf.rotation
    return p

def movement_too_big(cur_pose, new_pose):
    pos_inc = 0.3
    or_inc = 0.1

    if (cur_pose.position.x + pos_inc < new_pose.position.x):
        return True

    if (cur_pose.position.y + pos_inc < new_pose.position.y):
        return True

    if (cur_pose.position.z + pos_inc < new_pose.position.z):
        return True

    if (abs(abs(cur_pose.orientation.x) - abs(new_pose.orientation.x)) > or_inc):
        #print("I'm hit x\n")
        return True

    if (abs(abs(cur_pose.orientation.y) - abs(new_pose.orientation.y)) > or_inc):
        return True

    if (abs(abs(cur_pose.orientation.z) - abs(new_pose.orientation.z)) > or_inc):
        return True

    if (abs(abs(new_pose.orientation.x) - abs(cur_pose.orientation.x)) > or_inc):
        #print("I'm hit other x\n")
        return True

    if (abs(abs(new_pose.orientation.y) - abs(cur_pose.orientation.y)) > or_inc):
        return True

    if (abs(abs(new_pose.orientation.z) - abs(cur_pose.orientation.z)) > or_inc):
        return True

    return False

## RIGHT ARM ##
def upper_r_callback(msg):
    data = msg.data

    if (len(data) != 0):
        T = np.reshape(np.array(data, dtype=Float32), (4, 4))
        pose = T[:4,3] # First three rows, fourth column
        p = Pose()

        rot = T[:3, :3] # first 3, first 3 #numpy.ndarray changed from :4, :4
        rq = R.from_matrix(rot)
        rq = rq.as_quat()
        p.orientation.x = rq[0]
        p.orientation.y = rq[1]
        p.orientation.z = rq[2]
        p.orientation.w = rq[3]


        if not get_first_update_upper_r():
            if movement_too_big(get_cur_pose_upper_r(), p):
                return

        p.position.x = pose[0]
        p.position.y = pose[1]
        p.position.z = pose[2]

        set_cur_pose_upper_r(p)
        pub_upper_r.publish(p)
        set_first_update_upper_r(False)



def lower_r_callback(msg):
    data = msg.data
    if (len(data) != 0):
        T = np.reshape(np.array(data, dtype=Float32), (4, 4))
        pose = T[:4,3] # First three rows, fourth column
        p = Pose()

        rot = T[:3, :3] # first 3, first 3 #numpy.ndarray changed from :4, :4
        rq = R.from_matrix(rot)
        rq = rq.as_quat()
        p.orientation.x = rq[0]
        p.orientation.y = rq[1]
        p.orientation.z = rq[2]
        p.orientation.w = rq[3]

        if not get_first_update_lower_r():
            if movement_too_big(get_cur_pose_lower_r(), p):
                return
        p.position.x = pose[0]
        p.position.y = pose[1]
        p.position.z = pose[2]

        set_cur_pose_lower_r(p)
        pub_lower_r.publish(p)
        set_first_update_lower_r(False)

def wrist_r_callback(msg):
    data = msg.data
    if (len(data) != 0):
        T = np.reshape(np.array(data, dtype=Float32), (4, 4))
        pose = T[:4,3] # First three rows, fourth column
        p = Pose()

        rot = T[:3, :3] # first 3, first 3 #numpy.ndarray changed from :4, :4
        rq = R.from_matrix(rot)
        rq = rq.as_quat()
        p.orientation.x = rq[0]
        p.orientation.y = rq[1]
        p.orientation.z = rq[2]
        p.orientation.w = rq[3]

        if not get_first_update_wrist_r():
            if movement_too_big(get_cur_pose_wrist_r(), p):
                return

        p.position.x = pose[0]
        p.position.y = pose[1]
        p.position.z = pose[2]

        set_cur_pose_wrist_r(p)
        pub_wrist_r.publish(p)
        set_first_update_wrist_r(False)

## LEFT ARM ##
def upper_l_callback(msg):
    data = msg.data
    if (len(data) != 0):
        T = np.reshape(np.array(data, dtype=Float32), (4, 4))
        pose = T[:4,3] # First three rows, fourth column
        p = Pose()
        p.position.x = pose[0]
        p.position.y = pose[1]
        p.position.z = pose[2]

        rot = T[:3, :3] # first 3, first 3 #numpy.ndarray changed from :4, :4
        rq = R.from_matrix(rot)
        rq = rq.as_quat()
        p.orientation.x = rq[0]
        p.orientation.y = rq[1]
        p.orientation.z = rq[2]
        p.orientation.w = rq[3]
        pub_upper_l.publish(p)

def lower_l_callback(msg):
    data = msg.data
    if (len(data) != 0):
        T = np.reshape(np.array(data, dtype=Float32), (4, 4))
        pose = T[:4,3] # First three rows, fourth column
        p = Pose()
        p.position.x = pose[0]
        p.position.y = pose[1]
        p.position.z = pose[2]

        rot = T[:3, :3] # first 3, first 3 #numpy.ndarray changed from :4, :4
        rq = R.from_matrix(rot)
        rq = rq.as_quat()
        p.orientation.x = rq[0]
        p.orientation.y = rq[1]
        p.orientation.z = rq[2]
        p.orientation.w = rq[3]
        pub_lower_l.publish(p)

def wrist_l_callback(msg):
    data = msg.data
    if (len(data) != 0):
        T = np.reshape(np.array(data, dtype=Float32), (4, 4))
        pose = T[:4,3] # First three rows, fourth column
        p = Pose()
        p.position.x = pose[0]
        p.position.y = pose[1]
        p.position.z = pose[2]

        rot = T[:3, :3] # first 3, first 3 #numpy.ndarray changed from :4, :4
        rq = R.from_matrix(rot)
        rq = rq.as_quat()
        p.orientation.x = rq[0]
        p.orientation.y = rq[1]
        p.orientation.z = rq[2]
        p.orientation.w = rq[3]

        pub_wrist_l.publish(p)


def listener():

    sub_upper_r = rospy.Subscriber('/user_upper_r_transform', Float32MultiArray, upper_r_callback)
    sub_lower_r = rospy.Subscriber('/user_lower_r_transform', Float32MultiArray, lower_r_callback)
    sub_wrist_r = rospy.Subscriber('/user_wrist_r_transform', Float32MultiArray, wrist_r_callback)

    sub_upper_l = rospy.Subscriber('/user_upper_l_transform', Float32MultiArray, upper_l_callback)
    sub_lower_l = rospy.Subscriber('/user_lower_l_transform', Float32MultiArray, lower_l_callback)
    sub_wrist_l = rospy.Subscriber('/user_wrist_l_transform', Float32MultiArray, wrist_l_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
