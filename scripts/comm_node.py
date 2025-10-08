#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def incoming_cb(msg):
    rospy.loginfo(f"[{rospy.get_namespace()}] Received: {msg.data}")

def main():
    rospy.init_node('comm_node')
    ns = rospy.get_namespace().strip('/')
    pub = rospy.Publisher(f"/{ns}/outgoing_msg", String, queue_size=10)
    rospy.Subscriber(f"/{ns}/incoming_msg", String, incoming_cb)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(String(f"Hello from {ns}"))
        rate.sleep()

if __name__ == '__main__':
    main()
