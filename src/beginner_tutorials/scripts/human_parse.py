# Parse human values from TSV files
import numpy as np
from point import Point
import matplotlib
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import os
import rospy
from geometry_msgs.msg import Pose, Point, Quaternion, Transform


shoulder_pub = rospy.Publisher('/upper_arm_r', Pose, queue_size=10)
elbow_pub = rospy.Publisher('/lower_arm_r', Pose, queue_size=10)
rospy.init_node('talker', anonymous=True)



def parse(labels, vals):
    labels_list = labels.strip().split("\t")
    labels_list = labels_list[1:]

    num_labels = len(labels_list)

    tuples_list = []
    master_vals_list = []

    # Key: label.  Value:  list of tuples
    dict = {}

    for row in vals:
        row = row.strip().split("\t")
        vals_list = []
        for val in row:
            val = float(val)
            vals_list.append(val)
        master_vals_list.append(vals_list)

    for list in master_vals_list:
        for i in range(0, len(list)):
            if i % 3 == 0:
                temp = (list[i], list[i + 1], list[i + 2])
                i += 2
                tuples_list.append(temp)



    for i in range(0, len(tuples_list)):
        label = labels_list[i % num_labels - 1]
        tup = tuples_list[i]

        if label in dict:
            dict[label].append(tup)
        else:
            dict[label] = [tup]

    return dict

# For testing
def plot(dict):
    tup = dict["CV7"][0]
    print(dict)

    # Creating Figure
    fig = plt.figure(figsize = (12, 12))
    ax = plt.axes(projection="3d")

    ax.scatter3D(tup[0], tup[1], tup[2], color = "blue")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# For testing
def get_first_for_all(dict):

    first_tups = []
    labels = []
    for k in dict:
        labels.append(k)
        first_tups.append(dict[k][0])

    fig = plt.figure(figsize = (12, 12))
    ax = plt.axes(projection= "3d")

    for tup in first_tups:
        ax.scatter3D(tup[0], tup[1], tup[2])

    plt.show()
    return first_tups

def create_pose(tup):
    p = Pose()
    p.position.x = tup[0]
    p.position.y = tup[1]
    p.position.z = tup[2]

    return p

def pub_moves(dict):

    num_moves = len(dict['CV7'])
    print(num_moves)


    for i in range(0, num_moves):
        shoulder_pos_tup = dict['R_SAE'][i]
        elbow_pos_tup = dict['R_HUM'][i]
        shoulder_pose = create_pose(shoulder_pos_tup)
        elbow_pose = create_pose(elbow_pos_tup)
        shoulder_pub.publish(shoulder_pose)
        elbow_pub.publish(elbow_pose)


if __name__ == '__main__':
    file_path = 'data/Subject 11/Subject 11 Order2L0001.tsv'

    with open(os.path.join(os.path.dirname(__file__), file_path), 'r') as input_file:

        raw = input_file.readlines()[9:]
        labels = raw[0] # all labels as a single string
        vals = raw[1:]
        dict = parse(labels, vals)
        pub_moves(dict)
