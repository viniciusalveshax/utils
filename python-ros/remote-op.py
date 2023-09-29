#!/usr/bin/env python
# license removed for brevity

# Feito com base em
# http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29 
# https://answers.ros.org/question/131976/subscribing-and-publishing-to-a-twist-message/

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def talker():
#    pub = rospy.Publisher('cmd_vel', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	linear = 0.1
	angular = 0.0

	while not rospy.is_shutdown():
		pub = rospy.Publisher('cmd_vel', Twist)
		#hello_str = "hello world %s" % rospy.get_time()
		msg = Twist()
		msg.linear.x = linear
		msg.angular.z = angular	
		#        rospy.loginfo(hello_str)
		pub.publish(msg)
		rate.sleep()
		command = input()
		if command == 'a':
			linear = linear + 0.1
		elif command == 'z':
			linear = linear - 0.1
		elif command == 's':
			angular = angular + 0.1
		elif command == 'x':
			angular = angular - 0.1
		elif command == 'q':
			angular = 0
			linear = 0
			msg.linear.x = linear
			msg.angular.z = angular	
			pub.publish(msg)
			quit()
		else:
			continue

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
