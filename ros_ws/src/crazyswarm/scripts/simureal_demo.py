import numpy as np
from console import *
from pycrazyswarm import *
import threading

class Waypoint:
    def __init__(self, agent, x, y, z, arrival, duration):
        self.agent = agent
        self.x = x
        self.y = y
        self.z = z
        self.arrival = arrival
        self.duration = duration

    def __lt__(self, other):
        return self.arrival < other.arrival

    def __repr__(self):
        return "Ag {} at {} s. [{}, {}, {}]".format(self.agent, self.arrival, self.x, self.y, self.z)


def load_waypoint(filepath):
    # load csv file
    data = np.loadtxt(filepath, skiprows=1, delimiter=',')
    data[data[:, 0].argsort()]
    # convert to internal data structure
    waypoints = []
    lastAgent = None
    for row in data:
        if lastAgent is None or lastAgent != row[0]:
            lastTime = 0.0
        waypoints.append(Waypoint(int(row[0]), row[1], row[2], row[3], row[4], row[4] - lastTime))
        lastTime = row[4]
        lastAgent = int(row[0])

    # sort waypoints by arrival time
    waypoints.sort()
    return waypoints


def tf_listenner(console):
    rate = rospy.Rate(60.0)
    while not rospy.is_shutdown():
        for each in console.real_list:
            try:
                (trans, rot) = console.listener.lookupTransform('world', each, rospy.Time(0))
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
            pos = airsim.Pose(airsim.Vector3r(x_val=trans[1], y_val=trans[0], z_val=-trans[2] - 0.005),
                              airsim.Quaternionr(x_val=rot[0], y_val=rot[1], z_val=rot[2], w_val=rot[3]))
            console.sim_server.simSetVehiclePose(pos, True, each)
        rate.sleep()


if __name__ == "__main__":
    waypoints = load_waypoint('waypoint6.csv')
    con = Console(sim_ip='192.168.0.102')
    timeHelper = con.real_server.timeHelper
    # t1 = threading.Thread(target=tf_listenner, args=[con])
    # t1.start()
    con.takeoff(duration=4.0, group=0, height=1.0)
    while 1:
        lastTime = 0.0
        queue_goto = []

        for waypoint in waypoints:
            if waypoint.arrival - lastTime > 0:
                for c in queue_goto:
                    c.join()
                queue_goto = []
                # timeHelper.sleep(waypoint.arrival - lastTime)
                lastTime = waypoint.arrival
            if waypoint.arrival == lastTime:
                pos = np.array([waypoint.x, waypoint.y, waypoint.z])
                if waypoint.agent > 100:
                    queue_goto.append(con.goTo(pos, 3.0, 0, individual=waypoint.agent, relative=False))
                else:
                    con.goTo(pos, 3.0, 0, individual=waypoint.agent, relative=False)

            #waypoint.arrival = waypoint.arrival + 5.0