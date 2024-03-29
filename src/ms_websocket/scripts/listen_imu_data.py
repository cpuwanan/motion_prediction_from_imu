#!/usr/bin/env python
import rospy
from ms_msgs.msg import IMUData

def callback(data):
    print("[Frame: {}] ax: {}, ay: {}".format(data.header.frame_id, len(data.ax), len(data.ay)))
    
def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("imu_data", IMUData, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
