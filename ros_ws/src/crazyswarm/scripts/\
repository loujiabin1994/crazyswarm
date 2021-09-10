#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import tf
import airsim
import geometry_msgs.msg
if __name__ == '__main__':
    rospy.init_node('tf_airsim')

    listener = tf.TransformListener()  # TransformListener创建后就开始接受tf广播信息，最多可以缓存10s
    client = airsim.VehicleClient(ip="192.168.0.111")
    dronelist = []

    rate = rospy.Rate(60.0)
    (trans, rot) = listener.lookupTransform("world", "cf10", rospy.Time(0))
    pos = airsim.Pose(airsim.Vector3r(x_val=trans[1], y_val=trans[0], z_val=-trans[2]),
                      airsim.Quaternionr(x_val=rot[0], y_val=rot[1], z_val=rot[2], w_val=rot[3]))
    client.simAddVehicle('cf' + str(10), "simpleflight", pos)
    dronelist.append('cf' + str(10))
    while not rospy.is_shutdown():
        for each in dronelist:
            try:
                (trans, rot) = listener.lookupTransform('world', each, rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
            pos = airsim.Pose(airsim.Vector3r(x_val=trans[1], y_val=trans[0], z_val=-trans[2]),
                              airsim.Quaternionr(x_val=rot[0], y_val=rot[1], z_val=rot[2], w_val=rot[3]))
            client.simSetVehiclePose(pos,True,each)
        # for i in range(99):
            # try:
            #    # listener.waitForTransform("/cf10", "/world", now, rospy.Duration(1.0))
            #     (trans, rot) = listener.lookupTransform("world", "cf10", rospy.Time(0))
            #     print(10)
            # except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            #      continue
        # if i not in dronelist:

        # print(10)
        # else:
        #     continue




        # angular = 4 * math.atan2(trans[1], trans[0])
        # linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        # turtle_vel.publish(turtlesim.msg.Velocity(linear, angular))

        rate.sleep()
