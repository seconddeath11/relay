from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass
class Point:
    x: float
    y: float


def R_x(x, a):
    return -a if x else 1


def H_x(x, b):
    return -b if x else 0


class RelayEquation:
    def __init__(self, a, b, n):
        self.n = n
        self.b = b
        self.a = a
        self.points: List[Point] = []
        self.t0 = 1 / a + 1
        self.T0 = 2 + 1 / a + a
        self.h = (self.n - 1) * self.T0 + self.t0 + 1

    def run(self):
        self.points.append(Point(-0.6, -0.6))
        self.points.append(Point(1, 1))
        k = 0
        while True:
            if 1 + self.t0 > self.h - k * self.T0:
                x0 = 1 - self.a * (self.h - k * self.T0 - 1)
                self.points.append(Point(self.h, 1 - self.a * (self.h - k * self.T0 - 1)))
                break

            self.points.append(Point(1 + self.t0 + k * self.T0, 1 - self.a * self.t0))  # low

            if 1 + self.T0 > self.h - k * self.T0:
                x0 = self.h - k * self.T0 - self.T0
                self.points.append(Point(self.h, self.h - k * self.T0 - self.T0))
                break

            self.points.append(Point(1 + self.T0 + k * self.T0, 1))  # high
            k += 1

        t = self.h
        u = x0
        k = 0
        while (t < 3 * self.h or not u >= 0) and k < 100:
            r_offset, is_x_positive = self._get_offset(t - 1)
            r_x = R_x(is_x_positive, self.a)
            h_offset, is_x_positive = self._get_offset(t - self.h)
            h_x = H_x(is_x_positive, self.b)

            offset = min(r_offset, h_offset)
            u += (r_x + h_x) * offset
            t += offset
            self.points.append(Point(t, u))
            k += 1
        return self.points

    def _get_offset(self, t):
        current = 0
        for idx, p in enumerate(self.points):
            if t < p.x:
                current = idx
                break
        left = current - 1
        if self._changes_zero(current, left):
            x = self._get_x(left, current)
            if t < x:
                return x - t, self.points[left].y > 0
            left += 1

        while current < len(self.points) - 2 and not self._changes_zero(left, current):
            current += 1

        if self._changes_zero(current, left):
            left = current - 1
            x = self._get_x(left, current)
            return x - t, self.points[left].y > 0
        return self.points[current].x - t, self.points[current].y > 0

    def _get_x(self, left, current):
        w, h = self.points[current].x - self.points[left].x, self.points[current].y - self.points[left].y
        return self.points[left].x - self.points[left].y * w / h

    def _changes_zero(self, first, second):
        return np.sign(self.points[first].y) != np.sign(self.points[second].y)



if __name__ == "__main__":
    relay = RelayEquation(2, 2, 2)
    relay.run()
