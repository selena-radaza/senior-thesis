#Writes state values based off of what is heard from a rosbag.
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from state import State
states_list = []


def callback(data):
    cur_state = State(data.position, data.velocity, data.effort)
    states_list.append(cur_state)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s %s %s\n\n\n",
    data.position, data.velocity, data.effort)



def first_move_listener():
    rospy.init_node('first_move_listener', anonymous=True)
    rospy.Subscriber('/joint_states', JointState, callback)

    rospy.spin()


# Format:
# Position
# Velocity
# Effort
# (newline)
def file_master_movement():
    f = open("state_values.txt", "w")


    for i in states_list:

        # Write position values
        for p in i.position:
            f.write(str(p))
            f.write(" ")
        f.write("\n")

        # Write velocity values
        if i.velocity:
            for v in i.velocity:
                f.write(str(v))
                f.write(" ")
            f.write("\n")
        else:
            f.write(str(0))
            f.write("\n")

        # Write EVs
        for e in i.effort:
            f.write(str(e))
            f.write(" ")
        f.write("\nend\n")
    f.close()

def print_states_list():
    for i in states_list:
        print(i)


if __name__ == '__main__':
    try:
        first_move_listener()
        file_master_movement()
    except rospy.ROSInterruptException:
        pass
