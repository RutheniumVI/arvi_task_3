#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('command', String, queue_size=10)
	rospy.init_node('commander', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	while not rospy.is_shutdown():
		user_in = input("type something")
		hello_str = user_in
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
	

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
