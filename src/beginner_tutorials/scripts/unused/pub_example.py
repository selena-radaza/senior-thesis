import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from state import State
import sys

pub = None
states_list = []
i = 0


def convert_to_float(str_list):
    res = []
    for s in str_list:
        f = float(s)
        res.append(f)
    return res

def parse_lines(lines):
    i = 0
    while i < len(lines):
        pos = []
        vel = []
        eff = []
        if i % 4 == 0: # Position line
            pos_str = lines[i].split()
            pos = convert_to_float(pos_str)
            i += 1
        if i % 4 == 1: # Velocity line
            vel_str = lines[i].split()
            vel = convert_to_float(vel_str)
            i += 1
        if i % 4 == 2: # Effort line
            eff_str = lines[i].split()
            eff = convert_to_float(eff_str)
            i += 1
        if i % 4 == 3: # End line
            s = State(pos, vel, eff)
            states_list.append(s)
            i += 1


# Based on code from
# https://answers.ros.org/question/213075/publish-joint_state-with-python-to-rviz/
# Only need to publish velocity, not position and effort
def pub_movement(msg):

    global pub, i

    velocity = []
    vel_msg = Float32MultiArray()

    if (i >= len(states_list)):
        for j, _ in enumerate(msg.position):
            velocity.append(0)
    else:

        st = states_list[i]
        i += 1

        for j, _ in enumerate(msg.position):
            diff = msg.position[j] - st.position[j]
            diff *= 0.1
            velocity.append(-diff)

    vel_msg.data = velocity

    pub.publish(vel_msg)

        # js_msg = JointState()
        # js_msg.header = Header()
        # js_msg.header.stamp = rospy.Time.now()
        # js_msg.name = ['yumi_joint_1_r', 'yumi_joint_2_r', 'yumi_joint_7_r',
        # 'yumi_joint_3_r', 'yumi_joint_4_r', 'yumi_joint_5_r', 'yumi_joint_6_r',
        # 'gripper_r_joint', 'yumi_joint_1_l', 'yumi_joint_2_l', 'yumi_joint_7_l',
        # 'yumi_joint_3_l', 'yumi_joint_4_l', 'yumi_joint_5_l', 'yumi_joint_6_l',
        # 'gripper_l_joint']
        # js_msg.position = st.position
        # js_msg.velocity = st.velocity
        # js_msg.effort = st.effort
        # pub.publish(js_msg)
        # rate.sleep()

# def callback(data):
#     cur_state = State(data.position, data.velocity, data.effort)
#     states_list.append(cur_state)
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s %s %s\n\n\n",
#     data.position, data.velocity, data.effort)

if __name__ == '__main__':

    rospy.init_node('velocity_control')
    pub = rospy.Publisher('/joint_velocity_command_R', Float32MultiArray, queue_size = 10)
    rate = rospy.Rate(10)

    try:
        file_name = sys.argv[1]
        f = open(file_name, "r")
        lines = f.readlines()
        parse_lines(lines)
        js_subscriber = rospy.Subscriber('/joint_state_R', JointState, pub_movement)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
