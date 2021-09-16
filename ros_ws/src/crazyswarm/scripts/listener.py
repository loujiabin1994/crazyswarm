#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import tf
import airsim
import geometry_msgs.msg




if __name__ == '__main__':
    rospy.init_node('tf_airsim')
    listener = tf.TransformListener()  # TransformListener创建后就开始接受tf广播信息，最多可以缓存10s
    client = airsim.VehicleClient(ip="192.168.0.102")
    rate = rospy.Rate(100.0)
    while not rospy.is_shutdown():
        each = 'cf2'
        try:
            (trans, rot) = listener.lookupTransform('world', each, rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        pos = airsim.Pose(airsim.Vector3r(x_val=trans[1], y_val=trans[0], z_val=-trans[2]-0.01),
                          airsim.Quaternionr(x_val=rot[0], y_val=rot[1], z_val=rot[2], w_val=rot[3]))
        client.simSetVehiclePose(pos, True, each)
        rate.sleep()
