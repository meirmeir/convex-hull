import numpy as np
import matplotlib.pyplot as plt

class ConvexHull_2d:
    def __init__(self, pts):
        self.pts = pts
        self.num_pts = pts.shape[0]
        # self.pts_labeled = np.zeros((self.num_pts, 3))
        # self.pts_labeled[:, :2], self.pts_labeled[:, 2] = np.array(pts), np.arange(self.num_pts)

        self.pts_labeled = np.append(self.pts, np.arange(self.num_pts).reshape((self.num_pts, 1)), axis=1)

        self.hull = None

    def find_hull(self):
        pass
