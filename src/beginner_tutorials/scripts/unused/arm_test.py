import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion

# Starting Pose
upper_start = Pose()
upper_start.position = Point(-0.2, 1.18, 0)
upper_start.orientation = Quaternion(-.502, 1.635, 39.62, 1)

lower_start = Pose()
lower_start.position = Point(0, 2.12, 0)
lower_start.orientation = Quaternion(65, 0.225, 0.316, 1)

#Halfway Pose
upper_middle = Pose()
upper_middle.position = Point(-5.2, 5.6, 0)
upper_middle.orientation = Quaternion(-0.502, 0.32, -0.621, 1)

lower_middle = Pose()
lower_middle.position = Point(0, 2.12, 0)
lower_middle.orientation = Quaternion(90, 0.225, 0, 1)

# End Pose
upper_end = Pose()
upper_end.position = Point(-0.2, 1.6, 0)
upper_end.orientation = Quaternion(50, 0.225, -40, 1)

lower_end = Pose()
lower_end.position = Point(0, 2.12, 0)
lower_end.orientation = Quaternion(90, 0.225, 0, 1)

def numpy_to_point(nparray):
    ret = list(nparray)
    p = Point(ret[0], ret[1], ret[2])
    return p

def numpy_to_qt(nparray):
    ret = list(nparray)
    q = Quaternion(ret[0], ret[1], ret[2], 1)
    return q

def point_to_np(p):
    l = [p.x, p.y, p.z]
    npa = np.array(l)
    return npa

def qt_to_np(qt):
    l = [qt.x, qt.y, qt.z, qt.w]
    npa = np.array(l)
    return npa

# Start Pose:  Where limb starts
# End Pose:  Where limb is after movement
# Segment:  0 for upper, 1 for lower
# Return:  (List of Poses, Segment)
def move(start_pose, end_pose, segment):
    poses = [start_pose, end_pose]
    return (poses, segment)


def talker():

    #Publisher for upper arm
    pub_upper = rospy.Publisher('/upper_arm', Pose, queue_size=10)
    rospy.init_node('arm_talker', anonymous=True)
    #Publisher for lower arm
    pub_lower = rospy.Publisher('/lower_arm', Pose, queue_size=10)
    rate = rospy.Rate(10)
    

    # Get Poses for first part of movement
    upper_movement1 = move(upper_start, upper_middle, 0)
    lower_movement1 = move(lower_start, lower_middle, 1)

    upper_poses = upper_movement1[0]
    lower_poses = lower_movement1[0]

    for i in range(0, len(upper_poses)):
        rospy.loginfo("Upper arm: %s", upper_poses[i])
        pub_upper.publish(upper_poses[i])
        rospy.loginfo("Lower arm: %s", lower_poses[i])
        pub_lower.publish(lower_poses[i]


if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass

#GameObject.find(name of object ex upper_right)
