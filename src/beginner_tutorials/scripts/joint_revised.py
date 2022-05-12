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
from scipy.spatial.transform import Rotation as R

class Joint_Math:

    def rotate_x(self, deg):
        r_matrix_array = np.reshape(np.array([1.0, 0, 0,
                            0, math.cos(deg), -math.sin(deg),
                            0, math.sin(deg), math.cos(deg)], dtype=Float32), (3, 3))
        r_matrix = R.from_matrix(r_matrix_array)
        return r_matrix

    def rotate_y(self, deg):
        r_matrix_array = np.reshape(np.array([math.cos(deg), 0, math.sin(deg),
                            0, 1, 0,
                            -math.sin(deg), 0, math.cos(deg)], dtype=Float32), (3, 3))
        r_matrix = R.from_matrix(r_matrix_array)
        return r_matrix

    def rotate_z(self, deg):
        r_matrix_array = np.reshape(np.array([math.cos(deg), -math.sin(deg), 0,
                        math.sin(deg), math.cos(deg), 0,
                        0, 0, 1], dtype=Float32), (3, 3))
        r_matrix = R.from_matrix(r_matrix_array)
        return r_matrix


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

                # Elbow rotation at home position
                yumi_elbow_as_matrix = R.from_quat([0.0332, -0.554673, 0.721133, -0.413763])

                # Go back to zero rotation
                yumi_elbow_as_matrix_inverse = yumi_elbow_as_matrix.inv()

                T = np.reshape(np.array(data, dtype=Float32), (4, 4))
                p = Pose()

                pose = T[:4, 3]
                rot = T[:3, :3]
                rq = R.from_matrix(rot)

                rq = rq * yumi_elbow_as_matrix_inverse * self.rotate_x(90) * self.rotate_y(90)
                rq  = rq.as_quat()

                p.orientation.x = rq[0]
                p.orientation.y = rq[1]
                p.orientation.z = rq[2]
                p.orientation.w = rq[3]


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
            j1_as_matrix = R.from_quat([.271905, -0.4372, 0.699496, -0.49561])
            j2_as_matrix = R.from_quat([-0.236319, -0.0463, -0.868148, 0.432317])

            j1_as_matrix_inverse = j1_as_matrix.inv()
            j2_as_matrix_inverse = j2_as_matrix.inv()

            # Matrix of joint 1 rotation
            j1_matrix = self.cur_transform[:3, :3]
            j1_rot = self.rotate_x(90) * self.rotate_y(90) * R.from_matrix(j1_matrix)

            # Matrix of joint 2 rotation
            j2_matrix = self.cur_transform2[:3, :3]
            j2_rot = self.rotate_x(90) * self.rotate_y(90) * R.from_matrix(j2_matrix)



            # Apply both rotations
            rotation = j2_rot * j1_rot
            rq = rotation.as_quat()

            p.orientation.x = rq[0]
            p.orientation.y = rq[1]
            p.orientation.z = rq[2]
            p.orientation.w = rq[3]

            # Fake human difference
            if is_human:
                p.orientation.z += 0.1

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
