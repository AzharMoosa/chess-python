class Valid_One:
    # Global Variables
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    dx = None
    dy = None

    def __init__(self, starting_point, ending_point):
        self.x1 = starting_point[0]
        self.y1 = starting_point[1]
        self.x2 = ending_point[0]
        self.y2 = ending_point[1]
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1
