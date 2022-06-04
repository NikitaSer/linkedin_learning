class DrawingAPIOne(object):
    """Implementation specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print(f"API_1 draw_circle at {x},{y} with r={radius}")


class DrawingAPITwo(object):
    """Implementation specific abstraction: concrete class two"""
    def draw_circle(self, x, y, radius):
        print(f"API_2 draw_circle at {x},{y} with r={radius}")


class Circle(object):
    """Implementation-independent abstraction: for example, there could be a rectangle class!"""
    def __init__(self, x, y, radius, drawing_api):
        """Initialize the necessary attributes"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of by another class: DrawingAPI"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation independent"""
        self._radius *= percent


# Build the first Circle object using APIOne
circle_1 = Circle(1, 2, 3, DrawingAPIOne())

# Draw a circle_1
circle_1.draw()

# Build the second Circle object using APITwo
circle_2 = Circle(1, 2, 3, DrawingAPITwo())

# Draw a circle_2
circle_2.draw()