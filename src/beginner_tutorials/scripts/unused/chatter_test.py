# Chatter test for publishing poses based on position.  Used for debugging.
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion

def talker():
    pub = rospy.Publisher('/chatter', Pose, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        for i in range(0, 1000):
            msg = Pose()
            msg.position = Point(i, i / 10, i / 100)
            msg.orientation = Quaternion(0, 0, 0, 1)
            rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
