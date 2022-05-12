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

if __name__ == '__main__':
    # data = [.25, .1, .4, 0.5,
    #         .6, .3, .55, 0.6,
    #         .75, .8, .35, 0.7,
    #         0, 0, 0, 1]
    #
    # data = np.array(data, dtype=Float32)
    #
    # T = np.reshape(data, (4, 4))
    # pose = T[:4, 3] # last column, pose data
    # rot = T[:3, :3] # Rotation matrix
    # rq = R.from_matrix(rot)
    # rq = rq.as_quat()
    # print("Pose: ", pose)
    # print("Rotation matrix: ", rot)
    # print("Rotation matrix as quaternion: ", rq)
    # print("\n+++++++++++++++\n")

    rotate_z_90 = [1, 2, 3, 0,
                    4, 5, 6, 0,
                    7, 8, 9, 0,
                    0, 0, 0, 1]
    T = np.reshape(rotate_z_90, (4,4))
    rot = T[:3, :3]
    print("Rot before rot90: ", rot)
    x = np.rot90(rot)
    print("Rot after rot90: ", x)
    last = np.swapaxes(x, 0, 1)
    print("Rot after swap", last)
    #rq = R.from_matrix(rot)
    # rq = rq.as_quat()
    # print("Rotation matrix: ", rot)
    # print("Rotation matrix as quaternion: ", rq)
    # print("\n+++++++++++++++\n")
