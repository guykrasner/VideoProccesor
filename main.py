
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

from Logic.ImageMethod.change_color import ChangeColorImageMethod


def main():
    img = cv.imread(r'Resources/Images/messi.jpg')
    image_processor = ChangeColorImageMethod()
    processed_frame = image_processor.process(img)
    cv.imshow("Original Frame", img)
    cv.imshow("Processed Frame", processed_frame)
    pass


if __name__ == '__main__':
    main()
