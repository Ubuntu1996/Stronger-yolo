# coding: utf-8

import test
import os
import numpy as np
from PIL import Image
import cv2

if __name__ == '__main__':
    T = test.YoloTest()
    test_dir = '/data/pan/projects/digits/iron_data/images'
    result_dir = '/data/pan/projects/digits/iron_data/results'
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    image_paths = [os.path.join(test_dir, image) for image in os.listdir(test_dir)]
    for image_path in image_paths:
        save_path = os.path.join(result_dir, os.path.basename(image_path))
        image = np.array(Image.open(image_path))
        image = T.detect_image(image)
        print save_path
        cv2.imwrite(save_path, image)