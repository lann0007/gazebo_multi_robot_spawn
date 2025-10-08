#!/usr/bin/python3
import rospy
from gazebo_msgs.msg import ModelStates
from rosns3_client.msg import Waypoint
# from geometry_msgs.msg import Point

# Map robot names to NS-3 node IDs
robot_name_to_ns3_id = {
    'robot_0': 'robot_1',
    'robot_1': 'robot_2',
    'robot_2': 'robot_3',
    'robot_3': 'robot_4',
    'robot_4': 'robot_5'
    # Add more as needed
}

def callback(msg):
    # The first one always references the ground plane, so we skip it
    msg.name = msg.name[1:]
    msg.pose = msg.pose[1:]

    for i, name in enumerate(msg.name):
        if name in robot_name_to_ns3_id:
            ns3_msg = Waypoint()
            # ns3_msg.node_id = robot_name_to_ns3_id[name]
            ns3_msg.position.x = msg.pose[i].position.x
            ns3_msg.position.y = msg.pose[i].position.y
            ns3_msg.position.z = msg.pose[i].position.z
        
        if robot_name_to_ns3_id[name] == 'robot_1':
            pub.publish(ns3_msg)
        elif robot_name_to_ns3_id[name] == 'robot_2':
            pub_2.publish(ns3_msg)
        elif robot_name_to_ns3_id[name] == 'robot_3':
            pub_3.publish(ns3_msg)
        elif robot_name_to_ns3_id[name] == 'robot_4':
            pub_4.publish(ns3_msg)
        elif robot_name_to_ns3_id[name] == 'robot_5':
            pub_5.publish(ns3_msg)

if __name__ == '__main__':
    rospy.set_param('/use_sim_time', True)
    rospy.init_node('gazebo_to_ns3')
    pub = rospy.Publisher('/robot_1/current_state', Waypoint, queue_size=10)
    pub_2 = rospy.Publisher('/robot_2/current_state', Waypoint, queue_size=10)
    pub_3 = rospy.Publisher('/robot_3/current_state', Waypoint, queue_size=10)
    pub_4 = rospy.Publisher('/robot_4/current_state', Waypoint, queue_size=10)
    pub_5 = rospy.Publisher('/robot_5/current_state', Waypoint, queue_size=10)
    rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
    rospy.loginfo("ns3_translator node started, translating Gazebo model states to NS-3 waypoints.")
    rospy.spin()