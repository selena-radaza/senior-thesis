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
from scipy.spatial.transform import Rotation as R

class Joint:
    def __init__(self, sub_topic, sub_topic2, pub_topic, joint_name, is_human):

        # Set current Pose and transformation matrix
        self.cur_pose = Pose()
        self.cur_transform = np.reshape(np.zeros(16), (4, 4))
        self.cur_transform2 = np.reshape(np.zeros(16), (4, 4))

        # If joint has not been yet
        self.firstUpdate = True

        # Set publisher
        self.pub = rospy.Publisher(pub_topic, Pose, queue_size=10)

        # Call back for singular joint
        def callback(msg):
            data = msg.data

            if (len(data) != 0):
                T = np.reshape(np.array(data, dtype=Float32), (4, 4))
                p = Pose()

                pose = T[:4, 3]
                rot = T[:3, :3]
                rq = R.from_matrix(rot)
                rq  = rq.as_quat()

                p.orientation.x = rq[0]
                p.orientation.y = rq[1]
                p.orientation.z = rq[2]
                p.orientation.w = rq[3]

                # if not self.firstUpdate:
                #     if self.movement_too_big(p):
                #         return

                # p.position.x = pose[0]
                # p.position.y = pose[1]
                # p.position.z = pose[2]

                self.cur_pose = p
                self.firstUpdate = False
                self.pub.publish(p)

        # Callbacks for multiple joints
        def j1_callback(msg):
            data = msg.data
            if (len(data) != 0):
                T = np.reshape(np.array(data, dtype=Float32), (4, 4))
                self.cur_transform = T

        def j2_callback(msg):
            data = msg.data
            if (len(data) != 0):
                T = np.reshape(np.array(data, dtype=Float32), (4, 4))
                self.cur_transform2 = T
                callback_combine()

        def callback_combine():

            p = Pose()

            # Matrix of joint 1 rotation
            j1_matrix = self.cur_transform[:3, :3]
            j1_rot = R.from_matrix(j1_matrix)

            # Matrix of joint 2 rotation
            j2_matrix = self.cur_transform2[:3, :3]
            j2_rot = R.from_matrix(j2_matrix)

            # Apply both rotations
            rotation = j2_rot * j1_rot
            rq = rotation.as_quat()

            p.orientation.x = rq[0]
            p.orientation.y = rq[1]
            p.orientation.z = rq[2]
            p.orientation.w = rq[3]

            # Fake human difference
            # if is_human:
                # p.orientation.z += 0.2

            self.cur_pose = p
            self.firstUpdate = False
            self.pub.publish(p)

        # Check if it is a shouler joint, set subscribers
        if (sub_topic2 != ''):
            self.sub_j1 = rospy.Subscriber(sub_topic, Float32MultiArray, j1_callback)
            self.sub_j2 = rospy.Subscriber(sub_topic2, Float32MultiArray, j2_callback)
        else:
            self.sub = rospy.Subscriber(sub_topic, Float32MultiArray, callback)



    def movement_too_big(self, new_pose):
        or_inc = 0.1

        if (abs(abs(self.cur_pose.orientation.x) - abs(new_pose.orientation.x)) > or_inc):
            return True

        if (abs(abs(self.cur_pose.orientation.y) - abs(new_pose.orientation.y)) > or_inc):
            return True

        if (abs(abs(self.cur_pose.orientation.z) - abs(new_pose.orientation.z)) > or_inc):
            return True

        if (abs(abs(new_pose.orientation.x) - abs(self.cur_pose.orientation.x)) > or_inc):
            return True

        if (abs(abs(new_pose.orientation.y) - abs(self.cur_pose.orientation.y)) > or_inc):
            return True

        if (abs(abs(new_pose.orientation.z) - abs(self.cur_pose.orientation.z)) > or_inc):
            return True

        return False

    def get_cur_pose():
        return self.cur_pose

    def get_transform():
        return self.cur_transform

    def get_transform_2():
        return self.cur_transform2
