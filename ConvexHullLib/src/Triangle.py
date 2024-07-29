import numpy as np

LABEL = 3
LEN_WITH_LABEL = 4
MAX_NUM_NEIGHBORS = 3


class Triangle:
    def __init__(self, pt1, pt2, pt3, label=-1):
        """

        :param pt1:
        :param pt2:
        :param pt3:
        """

        self._base = Triangle._add_label_column(np.array(pt1))
        self.pt1 = Triangle._add_label_column(self._base)
        self.pt2 = Triangle._add_label_column(np.array(pt2))
        self.pt3 = Triangle._add_label_column(np.array(pt3))
        self.pts = [self.pt1, self.pt2, self.pt3]
        self.spanning_plane = [(self.pt2 - self._base)[: LABEL],
                               (self.pt3 - self._base)[: LABEL]]
        self._neighbors = []
        self.cross_p = np.cross(self.spanning_plane[0], self.spanning_plane[1])
        # self._have_labels = sum([len(pt) for pt in self.pts]) == 3 * LEN_WITH_LABEL



    def get_point_labels(self):
        return [pt[LABEL] for pt in self.pts]
        # if self._have_labels:
        #     return [pt[LABEL] for pt in self.pts]
        # else:
        #     return [None] * 3

    def pt_is_above(self, pt):
        """
        checks if the given pt is above the plane spanned by the two vectors pt2 - base, pt3 - base
        :param pt:
        :return:
        """

        pt_rel = Triangle._add_label_column(np.array(pt)) - self._base
        return np.dot(pt_rel[: LABEL], self.cross_p) > 0

    def get_neighbors(self):
        return self._neighbors

    def add_neighbor(self, neighbor_label):
        if len(self._neighbors) < MAX_NUM_NEIGHBORS:
            self._neighbors.append(neighbor_label)
            return True
        else:
            return False

    @staticmethod
    def _add_label_column(pt):
        if len(pt) >= LEN_WITH_LABEL:
            return pt
        else:
            return np.concatenate((np.array(pt), [-1]))
