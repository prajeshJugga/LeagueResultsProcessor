from tokenize import Double


class GamePoints(object):
    """docstring for GamePoints."""
    def __init__(self, win_points: Double, draw_points: Double, loss_points: Double):
        self.win_points = win_points
        self.draw_points = draw_points
        self.loss_points = loss_points

    @property
    def win_points(self) -> Double:
        return self._win_points

    @win_points.setter
    def win_points(self, value):
        self._win_points = value

    @property
    def draw_points(self) -> Double:
        return self._draw_points

    @draw_points.setter
    def draw_points(self, value):
        self._draw_points = value

    @property
    def loss_points(self) -> Double:
        return self._loss_points

    @loss_points.setter
    def loss_points(self, value):
        self._loss_points = value
