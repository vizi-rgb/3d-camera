class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Line:
    def __init__(self, point_a, point_b):
        self.start = point_a
        self.end = point_b


class Wireframe:
    def __init__(self):
        self.points = set()
        self.lines = []

    @staticmethod
    def from_file(file):
        try:
            with open(file, 'r') as f:
                wireframe = Wireframe()
                points = []
                lines = []
                for line in f:
                    cords = line.split()
                    if len(cords) != 6:
                        continue

                    for i in range(0, len(cords), 3):
                        a = float(cords[i])
                        b = float(cords[i + 1])
                        c = float(cords[i + 2])
                        points.append(Point(a, b, c))

                    point_a = points[-2]
                    point_b = points[-1]
                    lines.append(Line(point_a, point_b))

                f.close()
                wireframe.add_points(points)
                wireframe.add_lines(lines)
                return wireframe

        except FileNotFoundError:
            print(f"{type(Wireframe).__name__}: File not found: {file}")
            return

    def add_points(self, points):
        for point in points:
            self.points.add(point)

    def add_lines(self, lines):
        for line in lines:
            self.lines.append(line)

    def __str__(self):
        to_string = ""
        for point in self.points:
            to_string += f"[{point.x}, {point.y}, {point.z}]\n"
        return to_string

