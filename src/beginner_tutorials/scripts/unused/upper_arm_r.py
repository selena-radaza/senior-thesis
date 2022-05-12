import rospy
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Pose, Point, Quaternion

p = Pose()
p.position = Point(0.0, 0.0, 0.0)
p.orientation = Quaternion(0.0, 0.0, 0.0, 0.1)

def talker():
    pub = rospy.Publisher('/upper_arm_r', Pose, queue_size=10)
    rospy.init_node('arm_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        p.orientation.x += 0.1
        p.orientation.y += 0.1
        p.orientation.z += 0.1

        p.position.x += 0.1;
        p.position.y += 0.1;
        p.position.z += 0.1;
        rospy.loginfo(p)
        pub.publish(p)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
