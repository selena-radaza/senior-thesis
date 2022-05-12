# Publishing Joint State values based off of what was recorded by the parser.
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
