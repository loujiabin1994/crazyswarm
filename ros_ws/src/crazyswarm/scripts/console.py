from pycrazyswarm import *
import airsim
import rospy
# from tf import TransformListener
# import tf
import geometry_msgs.msg
import numpy as np
from scipy.spatial import distance
from pyquaternion import Quaternion
from sensor_msgs.msg import PointCloud2, PointField
import pcl
from pcl import pcl_visualization
from std_msgs.msg import Header


class Console:
    def __init__(self, sim_ip='', sim_port=41451, crazyflies_yaml=None):
        """
            Create A console to control all UAVs, including simulation and real drones.
        Args:
            sim_ip: the ip of airsim server.
            sim_port: port of airsim server
            crazyflies_yaml: information of crazyflie swarm.
        """
        # self.real_server=Crazyswarm(crazyflies_yaml)
        self.sim_server = airsim.client.MultirotorClient(sim_ip, sim_port)
        self.sim_list = ['cf101', 'cf102', 'cf103', 'cf104', 'cf105']
        self.init_position = {}
        for each in self.sim_list:
            self.init_position[each] = self.position(each)
        self.r = np.array([[0, 1, 0],
                           [1, 0, 0],
                           [0, 0, -1]])
        self.p = np.array([])
        rospy.init_node('console')
        self.tf = TransformListener()
        self.pub_pcl = rospy.Publisher("sim_pc", PointCloud2, queue_size=1)
        # listener = tf.TransformListener()
        # rate = rospy.Rate(60.0)
        # while not rospy.is_shutdown():
        #     # (trans, rot) = listener.lookupTransform('world', 'cf10', rospy.Time(0))
        #     # print(10)
        #     try:
        #         (trans, rot) = listener.lookupTransform('world', 'cf10', rospy.Time(0))
        #         print(1)
        #     except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        #         continue
        #     rate.sleep()

    def position_enu_to_ned(self, position):
        return np.dot(self.r, position)

    def tf_listenner(self):

        return
        # TODO

    def position(self, drone_id):
        """
        Args:
            drone_id: the drone_id you want to query

        Returns: the position and quaternion of that drone

        """
        if isinstance(drone_id, int):
            drone_id = 'cf' + str(drone_id)
        self.tf.waitForTransform("/world",  str(drone_id) + "/odom_local_ned", rospy.Time(0), rospy.Duration(10))
        position, quaternion = self.tf.lookupTransform("/world",  str(drone_id) + "/odom_local_ned", rospy.Time(0))
        return np.array(position), quaternion

    def emergency(self):
        """Emergency stop. Cuts power; causes future commands to be ignored.

        This command is useful if the operator determines that the control
        script is flawed, and that continuing to follow it will cause wrong/
        self-destructive behavior from the robots. In addition to cutting
        power to the motors, it ensures that any future commands, both high-
        level and streaming, will have no effect.

        The only ways to reset the firmware after an emergency stop has occurred
        are a physical hard reset or an nRF51 Reboot command.
        """
        self.real_server.allcfs.emergency()

    def takeoff(self, duration, group=0, individual=0, height=0.5, group_mask=0):
        """Broadcasted takeoff - fly straight up, then hover indefinitely.

             Broadcast version of :meth:`Crazyflie.takeoff()`. All robots that match the
             groupMask take off at exactly the same time. Use for synchronized
             movement. Asynchronous command; returns immediately.

             Args:

                 duration (float): How long until the height is reached. Seconds.
                 group_mask (int): Group mask bits. See :meth:`setGroupMask()` doc.
                 height (float): The z-coordinate at which to hover.
                 group(int): 0 for all, 1 for Real, 2 for virtual.
                 individual(int): 0 for None, others for the id.
         """
        if individual == 0:
            if group < 2:
                self.real_server.allcfs.takeoff(height, duration, group_mask)
            if group != 1:
                # Airsim
                commandque = []
                for drone in self.sim_list:
                    commandque.append(self.sim_server.moveToZAsync(-height, height / duration, vehicle_name=drone))
                for c in commandque:
                    c.join()

        else:
            if individual < 100:
                for each in self.real_server.allcfs:
                    if each.id == individual:
                        each.takeoff(height, duration)
                        break
            else:
                # self.sim_server.takeoffAsync(timeout_sec=duration, vehicle_name='cf' + str(individual))
                self.sim_server.moveToZAsync(-height, height / duration, vehicle_name='cf' + str(individual)).join()

    def land(self, height=0.1, duration=2, group=0, individual=0, group_mask=0):
        """Broadcasted landing - fly straight down. User must cut power after.
        Broadcast version of :meth:`Crazyflie.land()`. All robots that match the
        groupMask land at exactly the same time. Use for synchronized
        movement. Asynchronous command; returns immediately.

        Args:
            height (float): The z-coordinate at which to land. Meters.
                Usually should be a few centimeters above the initial position
                to ensure that the controller does not try to penetrate the
                floor if the mocap coordinate origin is not perfect.
            duration (float): How long until the height is reached. Seconds.
            group_mask (int): Group mask bits. See :meth:`Crazyflie.setGroupMask()` doc.
            group(int): 0 for all, 1 for Real, 2 for virtual.
            individual(int): 0 for None, others for the id.
        """
        if individual == 0:
            if group < 2:
                self.real_server.allcfs.land(height, duration, group_mask)
            if group != 1:
                commandque = []
                for drone in self.sim_list:
                    commandque.append(self.sim_server.landAsync(timeout_sec=duration, vehicle_name=drone))
                for c in commandque:
                    c.join()
        else:
            if individual < 100:
                for each in self.real_server.allcfs:
                    if each.id == individual:
                        each.land(height, duration)
                        break
            else:
                self.sim_server.landAsync(timeout_sec=duration, vehicle_name='cf' + str(individual)).joint()

    def goTo(self, goal, duration, yaw=0, group_mask=0, group=0, individual=0, relative=True):
        """Broadcasted goTo - Move smoothly to goal, then hover indefinitely.

        Broadcast version of :meth:`Crazyflie.goTo()`. All robots that match the
        groupMask start moving at exactly the same time. Use for synchronized
        movement. Asynchronous command; returns immediately.

        While the individual goTo() supports both relative and absolute
        coordinates, the broadcasted goTo only makes sense with relative
        coordinates (since absolute broadcasted goTo() would cause a collision).
        Therefore, there is no `relative` kwarg.

        See docstring of :meth:`Crazyflie.goTo()` for additional details.

        Args:
            goal (iterable of 3 floats): The goal offset. Meters.
            yaw (float): The goal yaw angle (heading). Radians.
            duration (float): How long until the goal is reached. Seconds.
            group_mask (int): Group mask bits. See :meth:`Crazyflie.setGroupMask()` doc.
            group(int): 0 for all, 1 for Real, 2 for virtual.
            individual(int): 0 for None, others for the id.
            relative(int): Ture for relative, False for absolute.
        """
        if individual == 0:
            if group < 2:
                self.real_server.allcfs.goTo(goal, yaw, duration, group_mask)
                # Just Relative
            if group != 1:
                dis = distance.euclidean(goal, np.array([0, 0, 0]))
                commandque = []
                for drone in self.sim_list:
                    target = goal + self.position(drone)[0]
                    velocity = dis / duration
                    target = self.position_enu_to_ned(target) - self.init_position[drone]
                    c=self.sim_server.moveToPositionAsync(target[0], target[1], target[2], velocity, vehicle_name=drone)
                rate = rospy.Rate(0.2)
                rate.sleep()
                   # c.join()
              # for c in commandque:
                #    c.join()
        else:
            if individual < 100:
                for each in self.real_server.allcfs:
                    if each.id == individual:
                        each.goTo(goal, yaw, duration, relative)
                        break
            else:
                if relative is True:
                    goal += self.position(individual)[0]
                dis = distance.euclidean(goal, self.position(individual)[0])
                velocity = dis / duration
                goal = self.position_enu_to_ned(goal) - self.init_position['cf'+str(individual)]
                self.sim_server.moveToPositionAsync(goal[0], goal[1], goal[2], velocity,
                                                    vehicle_name='cf' + str(individual))


    def publish_pcl(self, r=10, flagHaveColor=True, colorMaxDist=None):
        # br = tf.TransformBroadcaster()
        rate = rospy.Rate(r)
        while not rospy.is_shutdown():
            center = airsim.Vector3r(0, 0, -3)
            self.p = np.array(self.sim_server.simCreateVoxelGrid(center, 5, 5, 8, 0.1, "111")) * 0.1
            header = Header()
            header.stamp = rospy.Time().now()
            header.frame_id = "world"
            msg = PointCloud2()
            msg.header = header

            if len(self.p.shape) == 3:
                msg.height = self.p.shape[1]
                msg.width = self.p.shape[0]
            else:
                msg.height = 1
                msg.width = self.p.shape[0]

            msg.fields = [
                PointField('x', 0, PointField.FLOAT32, 1),
                PointField('y', 4, PointField.FLOAT32, 1),
                PointField('z', 8, PointField.FLOAT32, 1)]

            msg.is_bigendian = False
            msg.point_step = 12
            msg.row_step = msg.point_step * self.p.shape[0]
            msg.is_dense = int(np.isfinite(self.p).all())
            msg.data = np.asarray(self.p, np.float32).tostring()

            self.pub_pcl.publish(msg)
            rospy.loginfo("pc %s published. ")
            rate.sleep()

        rospy.loginfo("All point clouds published.")


