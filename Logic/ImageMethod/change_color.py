from Framework.ImageMethod.IImageMethod import IImageMethod
from numpy import ndarray


class ChangeColorImageMethod(IImageMethod):

    def __init__(self, color='blue'):
        self._color = color

    def process(self, frame: ndarray) -> ndarray:
        temp = frame.copy()
        if self._color == 'blue':
            temp[:, :] = [255, 0, 0]
            return temp
        return frame

