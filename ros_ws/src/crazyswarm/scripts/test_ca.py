import numpy as np
import threading
from pycrazyswarm import *
from time import sleep, ctime
import scipy as sp

radii = 0.7

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


def obstacle_avoidance(cfs, tello, radii):
    while(1):
        for cf in cfs:
            dist = np.sqrt((cf.state.pos.x - tello.state.pos.x)**2 + (cf.state.pos.y - tello.state.pos.y)**2 + (cf.state.pos.z - tello.state.pos.z)**2)
            if dist < radii:
                pos = [cf.state.pos.x, cf.state.pos.y, cf.state.pos.z + 1.0]
                cf.goTo(pos, 0, 1.0)


if __name__ == "__main__":
    waypoints = load_waypoint("waypoints6.csv")
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cf6 = allcfs.crazyfliesById[7]
    cf6.setLEDColor(1,0.5,0.5)

    # collision avoidance
    cfs = allcfs.crazyflies
    cfs_ca = cfs[:-1]
    other = cfs[-1]
    thread_ca = threading.Thread(target = obstacle_avoidance, args = (cfs_ca, other, radii))
    thread_ca.start()
    # thread_ca.join()

    # patrol
    allcfs.takeoff(targetHeight=1.0, duration=2.0)
    timeHelper.sleep(2.0)
    lastTime = 0.0

    while (1):
        for waypoint in waypoints:
            if waypoint.arrival == 0:
                pos = [waypoint.x, waypoint.y, waypoint.z]
                cf = allcfs.crazyfliesById[waypoint.agent]
                cf.goTo(pos, 0, 2.0)
            elif waypoint.duration > 0:
                timeHelper.sleep(waypoint.arrival - lastTime)
                lastTime = waypoint.arrival
                pos = [waypoint.x, waypoint.y, waypoint.z]
                cf = allcfs.crazyfliesById[waypoint.agent]
                cf.goTo(pos, 0, waypoint.duration)
            waypoint.arrival = waypoint.arrival + 20.0

    # land
    allcfs.land(targetHeight=0.02, duration=2.0)
    timeHelper.sleep(2.0)
