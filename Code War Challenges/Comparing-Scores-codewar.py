def better_than_average(class_points, your_points):
    return True if your_points > sum(class_points) / len(class_points) else False

class_points = [90, 88, 50, 31, 28, 11, 90, 88, 53, 82, 53, 34, 53, 13, 36, 34, 77, 61, 94, 10, 44, 10, 46]
your_points = 64

print(better_than_average(class_points, your_points))
