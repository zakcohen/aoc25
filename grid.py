from point import Point

class Grid:
    def __init__(self):
        self.data = []

    def width(self):
        return len(self.data[0])

    def height(self):
        return len(self.data)

    def get(self, x: int, y: int):
        return self.data[y][x]
    
    def get_p(self, point: Point):
        return self.get(point.x, point.y)

    def set(self, x: int, y: int, value):
        self.data[y][x] = value

    def set_p(self, point: Point, value):
        self.set(point.x, point.y, value)

    def get_neighbors_4_p(self, point: Point):
        return self.get_neighbors_4(point.x, point.y)

    def get_neighbors_4(self, x, y):
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if self.is_in_bounds(nx, ny):
                neighbors.append(Point(nx, ny))
        return neighbors

    def is_in_bounds(self, x, y):
        return 0 <= x < self.width() and 0 <= y < self.height()

    def is_in_bounds_p(self, point: Point):
        return self.is_in_bounds(point.x, point.y)

    def copy(self):
        new_grid = Grid()
        new_grid.data = [row[:] for row in self.data]
        return new_grid
    
    def print_dense(self):
        for row in self.data:
            print(''.join(row))
