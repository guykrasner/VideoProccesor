from abc import ABCMeta, abstractmethod
from cv2 import VideoCapture



class IVideoMethod(ABCMeta):

    @abstractmethod
    def process(self, capture: VideoCapture):
        pass
