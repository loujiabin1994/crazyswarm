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


if __name__ == "__main__":
    #waypoints = load_waypoint('waypoints6.csv')
    con = Console(sim_ip='192.168.0.102')
    timeHelper = con.real_server.timeHelper
    con.takeoff(duration=4.0, group=2, height=1.0)
    while 1:
        queue_goto = []
        pos = np.array([0.0, 2.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=101, relative=False))
        pos = np.array([0.0, 0.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=102, relative=False))
        pos = np.array([-1.0, 1.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=103, relative=False))
        for c in queue_goto:
            c.join()
        queue_goto = []
        pos = np.array([-2.0, 2.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=101, relative=False))
        pos = np.array([-2.0, 0.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=102, relative=False))
        pos = np.array([-3.0, 1.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=103, relative=False))
        for c in queue_goto:
            c.join()
        queue_goto = []
        pos = np.array([-2.0, 0.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=101, relative=False))
        pos = np.array([-2.0, -2.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=102, relative=False))
        pos = np.array([-3.0, -1.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=103, relative=False))
        for c in queue_goto:
            c.join()
        queue_goto = []
        pos = np.array([0.0, 0.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=101, relative=False))
        pos = np.array([0.0, -2.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=102, relative=False))
        pos = np.array([-1.0, -1.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=103, relative=False))
        for c in queue_goto:
            c.join()
        queue_goto = []
        pos = np.array([0.0, 2.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=101, relative=False))
        pos = np.array([0.0, 0.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=102, relative=False))
        pos = np.array([-1.0, 1.0, 1.0])
        queue_goto.append(con.goTo(pos, 3.0, 0, individual=103, relative=False))
        for c in queue_goto:
            c.join()