import numpy as np
import threading
from pycrazyswarm import *
import time
import scipy as sp

# 飞控常数
TAKEOFFTIME = 2.0
RADII = 0.7
HOVERTIME = 3.0
CATIME = 1.0

# cf是否避障标志位
cf_flag = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

# 航点类
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

# 载入数据
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

# 第一版
# def obstacle_avoidance(cfs, tello, radii):
#     while(1):
#         for cf in cfs:
#             dist = np.sqrt((cf.state.pos.x - tello.state.pos.x)**2 + (cf.state.pos.y - tello.state.pos.y)**2
#             + (cf.state.pos.z - tello.state.pos.z)**2)
#             if dist < radii:
#                 pos = [cf.state.pos.x, cf.state.pos.y, cf.state.pos.z + 1.0]
#                 cf.goTo(pos, 0, 1.0)

# 避障线程函数
# 不能在避障过程中继续检测
def collision_avoidance(cf_ca, tello_ca, radii_ca):
    while(1):
        dist = np.sqrt((cf_ca.state.pos.x - tello_ca.state.pos.x)**2 + (cf_ca.state.pos.y - tello_ca.state.pos.y)**2
                       + (cf_ca.state.pos.z - tello_ca.state.pos.z)**2)
        if dist < radii_ca:
            cf_flag[cf_ca.id] = 1
            dz = 1 if tello_ca.state.pos.z <= cf_ca.state.pos.z else -1
            pos_ca = [cf_ca.state.pos.x, cf_ca.state.pos.y, cf_ca.state.pos.z + 1.0*dz]
            cf_ca.goTo(pos_ca, 0, CATIME)
            # timeHelper.sleep(CATIME)
            time.sleep(CATIME)
            dx = 1 if tello_ca.state.pos.x <= cf_ca.state.pos.x else -1
            dy = 1 if tello_ca.state.pos.y <= cf_ca.state.pos.y else -1
            pos_ca = [cf_ca.state.pos.x + 1.0*dx, cf_ca.state.pos.y + 1.0*dy, cf_ca.state.pos.z]
            # cf_ca.goTo(pos_ca, 0, CATIME)
            # timeHelper.sleep(CATIME)
            # timeHelper.sleep(HOVERTIME)
            time.sleep(HOVERTIME)
            cf_flag[cf_ca.id] = 0


if __name__ == "__main__":
    # load data
    waypoints = load_waypoint("waypoints6_high.csv")

    # load cf
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    cfs = allcfs.crazyflies
    cf1, cf2, cf3, cf4, cf5, cf6, cf7 = allcfs.crazyflies
    cf7.setLEDColor(1, 0.5, 0.5)

    # collision avoidance
    thread_ca_cf1 = threading.Thread(target=collision_avoidance, args=(cf1, cf7, RADII))
    thread_ca_cf2 = threading.Thread(target=collision_avoidance, args=(cf2, cf7, RADII))
    thread_ca_cf3 = threading.Thread(target=collision_avoidance, args=(cf3, cf7, RADII))
    thread_ca_cf4 = threading.Thread(target=collision_avoidance, args=(cf4, cf7, RADII))
    thread_ca_cf5 = threading.Thread(target=collision_avoidance, args=(cf5, cf7, RADII))
    thread_ca_cf6 = threading.Thread(target=collision_avoidance, args=(cf6, cf7, RADII))
    thread_ca_cf1.start()
    thread_ca_cf2.start()
    thread_ca_cf3.start()
    thread_ca_cf4.start()
    thread_ca_cf5.start()
    thread_ca_cf6.start()
    # thread_ca.join()

    # patrol
    allcfs.takeoff(targetHeight=1.0, duration=TAKEOFFTIME)
    timeHelper.sleep(TAKEOFFTIME)
    lastTime = 0.0

    while(1):
        for waypoint in waypoints:
            cf = allcfs.crazyfliesById[waypoint.agent]
            if cf_flag[cf.id] == 1:
                waypoint.arrival = waypoint.arrival + 10.0
                continue
            if waypoint.arrival == 0:
                pos = [waypoint.x, waypoint.y, waypoint.z]
                cf.goTo(pos, 0, 2.0)
            elif waypoint.duration > 0:
                timeHelper.sleep(waypoint.arrival - lastTime)
                lastTime = waypoint.arrival
                pos = [waypoint.x, waypoint.y, waypoint.z]
                cf.goTo(pos, 0, waypoint.duration)
            waypoint.arrival = waypoint.arrival + 10.0

    # land
    allcfs.land(targetHeight=0.02, duration=2.0)
    timeHelper.sleep(2.0)
