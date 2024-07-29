import numpy as np
import matplotlib.plot as plt

from src.ConvexHull_3d import ConvexHull_3d
from collections import deque

X, Y, Z, LABEL = 0, 1, 2, 3
NUM_PTS_TRIANGLE = 3

class GiftWrapping_3d(ConvexHull_3d):
    def __init__(self, pts):
        super().__init__(pts)

        # sort points by z value, lowest first
        self.pts_labeled_sorted = self.pts_labeled(np.argsort(self.pts[Z]))

        self._base_triangle = []
        self._triangles = []

    def find_hull(self):
        self._base_triangle = self.pts_labeled_sorted[:NUM_PTS_TRIANGLE]
        self._triangles.append(self._base_triangle)

        self._hull_labels.update(list(self._base_triangle[:, LABEL])) # add base triangle to the hull

        cond = 0 # TODO: find  condition to terminate while loop

        while cond:

