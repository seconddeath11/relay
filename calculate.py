import matplotlib.pyplot as plt


def sign(x):
    return -1 if x < 0 else (1 if x > 0 else (0 if x == 0 else None))


# def run(a, b, h0, n):
#     points = []
#     t0 = h0 / a + h0
#     T0 = 2 * h0 + h0 / a + h0 * a
#     h1 = (T0 * n + (n - 1) * T0 + t0 + h0) / 2
#
#     x0 = 0
#     σ = 0.6
#     # -σ < t < 0
#     points.append((-σ, -σ))
#     points.append((h0, h0))
#     k = 0
#     while True:
#         # // h0 < t < t0 + h0
#         if h0 + t0 + k * T0 > h1:
#             x0 = h0 - a * (h1 - h0 - k * T0)
#             points.append((h1, h0 - a * (h1 - h0 - k * T0)))
#             break
#
#         points.append((h0 + t0 + k * T0, h0 - a * t0))
#
#         # // t0 + h0 < t < T0 + h0
#         if h0 + T0 + k * T0 > h1:
#             x0 = (h1 - k * T0) - T0
#             points.append((h1, (h1 - k * T0) - T0))
#             break
#
#         points.append((h0 + T0 + k * T0, h0))
#         k += 1
#
#     t = h1
#     u = x0
#     k = 0
#     has_null = False
#     while t < 3 * h1 or not has_null and k < 1000:
#         inerval0 = get_interval(points, t - h0)
#         inerval1 = get_interval(points, t - h1)
#
#         offset = min(inerval0[0], inerval1[0])
#
#         if inerval0[1]:
#             if inerval1[1]:
#                 u += -(a + b) * offset
#             else:
#                 u += -a * offset
#         else:
#             if inerval1[1]:
#                 u += (1 - b) * offset
#             else:
#                 u += offset
#         t += offset
#         if u >= 0:
#             has_null = True
#         points.append((t, u))
#         k += 1
#     return points

def run(a, b, n):
    points = []
    t0 = 1 / a + 1
    T0 = 2 + 1 / a + a
    h = (n - 1) * T0 + t0 + 1

    points.append((-0.6, -0.6))
    points.append((1, 1))
    k = -1
    while True:
        k += 1
        # // 1 < t < t0 + 1
        if 1 + t0 > h - k * T0:
            x0 = 1 - a * (h - k * T0 - 1)
            points.append((h, 1 - a * (h - k * T0 - 1)))
            break

        points.append((1 + t0 + k * T0, 1 - a * t0))  # Нижние

        # // t0 + 1 < t < T0 + 1
        if 1 + T0 > h - k * T0:
            x0 = h - k * T0 - T0
            points.append((h, h - k * T0 - T0))
            break

        points.append((1 + T0 + k * T0, 1))  # верхние

    t = h
    u = x0
    k = 0
    has_null = False
    while t < 3 * h or not has_null and k < 1000:
        interval_0 = get_interval(points, t - 1)
        interval_1 = get_interval(points, t - h)

        offset = min(interval_0[0], interval_1[0])

        if interval_0[1]:
            if interval_1[1]:
                u += -(a + b) * offset
            else:
                u += -a * offset
        else:
            if interval_1[1]:
                u += (1 - b) * offset
            else:
                u += offset
        t += offset
        if u >= 0:
            has_null = True
        points.append((t, u))
        k += 1
    return points


def get_interval(points, t):
    it = 0

    for idx, p in enumerate(points):
        if t < p[0]:
            it = idx
            break

    start_it = it - 1

    if sign(points[it][1]) != sign(points[start_it][1]):
        w = points[it][0] - points[start_it][0]
        h = points[it][1] - points[start_it][1]

        x = points[start_it][0] - points[start_it][1] * w / h

        if t + 0.0001 < x:
            return x - t, points[start_it][1] > 0

        start_it += 1

    while it < len(points) - 2 and sign(points[it][1]) == sign(points[start_it][1]):
        it += 1

    if sign(points[it][1]) != sign(points[start_it][1]):
        prev_it = it - 1

        w = points[it][0] - points[prev_it][0]
        h = points[it][1] - points[prev_it][1]

        x = points[prev_it][0] - points[prev_it][1] * w / h

        return x - t, points[prev_it][1] > 0

    return points[it][0] - t, points[it][1] > 0



