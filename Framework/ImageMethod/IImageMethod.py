from abc import ABC, abstractmethod
from numpy import ndarray


class IImageMethod(ABC):

    @abstractmethod
    def process(self, frame: ndarray) -> ndarray:
        pass
