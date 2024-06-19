import math

points = [(1, 2), (4, 6), (7, 8), (2, 1), (3, 3)]

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

min_distance = float('inf')
min_points = (None, None)

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        print(f"{points[i]} ve {points[j]} arasındaki mesafe: {distance:.2f}")
        if distance < min_distance:
            min_distance = distance
            min_points = (points[i], points[j])

print(f"Minimum Mesafe: {min_distance:.2f} ({min_points[0]} ve {min_points[1]} arasında)")
