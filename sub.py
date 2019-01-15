#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	if data.data =="ON":
		print("Turned on LED")
	elif data.data =="OFF":
		print("Turned off LED")

def listener():
	rospy.init_node('actuator', anonymous=True)
	rospy.Subscriber('command', String, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
