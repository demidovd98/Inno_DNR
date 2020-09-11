#!/usr/bin/env python
# Making sure the script is executed as a Python script


### Imports:
# Python libs
import rospy

# Ros messages types (classes)
from sensor_msgs.msg import JointState
from std_msgs.msg import Header


### Body:
def talker():
    ## Initialise node:
	# init_node('node_name',
	   # anonymous = True/False [create unique name by adding 	  		   #random numbers to the end of 'node_name'] )
    rospy.init_node('joint_state_publisher')

    ## Create publisher: 
	# Publisher( 'topic_name', 
	   # type [here is a class], 
	   # queue_size = amount of queued messages )    
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)

    # Rate of looping (5 times per sec)
    rate = rospy.Rate(5) # 5hz

    while not rospy.is_shutdown():
	## Variables become 0 to reset robot position:     
	x1 = 0.0 # base_to_mid joint rotation value
        y1 = 0.0 # mid_to_wrist joint rotation value
        z1 = 0.0 # wrist_to_end-effector joint rotation value
	print(x1, y1, z1) # for Debug

	## Passing message to publish:
	msg = JointState() # Create object msg
	msg.header = Header()
	# Message name(s)
	msg.name = ['base_to_mid', 'mid_to_wrist', 'wrist_to_end-effector']

	## Incremental passing of value to robot joint:
	while x1 < 1.5:
	    msg.header.stamp = rospy.Time.now() # Update msg header stamp
	    msg.position = [x1, y1, z1] # Pass value to msg
	    print(x1, y1, z1) # for Debug
	    pub.publish(msg) # Publish msg in topic

	    ## Values incrementing:
		# Sorry for this, but it works :D
            x1 += 0.05 # [0.0 ... 1.57]
            y1 += 0.025 # [0.0 ... 0.7], p.s. 2x times slower incrementing
            z1 += 0.05 # [0.0 ... 1.57]
            
	    rate.sleep() # Delay


### Main  (??? in case of the script is opened from outside):
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
