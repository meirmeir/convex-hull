import numpy as np
import matplotlib.pyplot as plt
from collections import deque

from src.ConvexHull2d import ConvexHull2d

X, Y, LABEL, ANGLE = range(4)


class GrahamScan(ConvexHull2d):
    def __init__(self, pts):
        super().__init__(pts)
        self._source, self._source_idx = self._find_source()
        self.__travel_pts_with_angle = self._find_travel_pts()
        self._hull = None
        self._find_hull()

    def _find_hull(self):
        self._hull = deque()

        self._hull.append(self._source)

        # initiate the hull with the first pt in travel points, it is the rightmost point that we turn left to
        self._hull.append(self.__travel_pts_with_angle[0, :ANGLE])

        for pt in self.__travel_pts_with_angle[1:]:
            v1 = self._hull[-1] - self._hull[-2]
            v2 = pt[:ANGLE] - self._hull[-1]

            while GrahamScan._is_right_turn(v1, v2):
                self._hull.pop()

                v1 = self._hull[-1] - self._hull[-2]
                v2 = pt[:ANGLE] - self._hull[-1]

            self._hull.append(pt[:ANGLE])

            if self._hull[-1][LABEL] == self._source[LABEL]:
                break

        self._hull = np.array(self._hull)



    def _find_source(self):
        """

        :return:
        """
        source_idx = np.argmin(self.pts_labeled[:, Y])  # the bottom point
        source = self.pts_labeled[source_idx]

        return source, source_idx

    def _find_travel_pts(self):
        """

        :return:
        """
        travel_pts = np.append(self.pts_labeled, np.zeros((self.num_pts, 1)), axis=1)
        travel_pts[:, ANGLE] = np.arctan2(travel_pts[:, Y] - self._source[Y], travel_pts[:, X] - self._source[X])  # angle in rads
        travel_pts[self._source_idx, ANGLE] = np.inf

        # now sort by angle. note that source will be in the end of the list
        travel_pts = travel_pts[np.argsort(travel_pts[:, ANGLE])]
        return travel_pts

    @staticmethod
    def _is_right_turn(vec1, vec2):
        """

        :param vec1:
        :param vec2:
        :return:
        """

        x1, y1, *_ = vec1
        x2, y2, *_ = vec2
        return (x1 * y2 - y1 * x2) < 0


    @staticmethod
    def _is_left_turn(vec1, vec2):
        """

        :param vec1:
        :param vec2:
        :return:
        """
        return not GrahamScan._is_right_turn(vec1, vec2)

    def get_hull(self):
        return self._hull

    def get_pts_with_labels(self):
        return self.pts_labeled