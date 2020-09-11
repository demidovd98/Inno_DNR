#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState
from std_msgs.msg import Header


def talker():
    rospy.init_node('joint_state_publisher')
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rate = rospy.Rate(5) # 10hz


    while not rospy.is_shutdown():
        x1 = 0.0
        y1 = 0.0
        z1 = 0.0
	print(x1, y1, z1)
	msg = JointState()
	msg.header = Header()
	msg.header = Header()
	msg.name = ['base_to_mid', 'mid_to_wrist', 'wrist_to_end-effector']

	while x1 < 1.5:
	    msg.header.stamp = rospy.Time.now()
	    msg.position = [x1, y1, z1]
	    print(x1, y1, z1)
	    pub.publish(msg)
            x1 += 0.05
            y1 += 0.025
            z1 += 0.05
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
