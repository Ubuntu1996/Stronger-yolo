# -*- coding:utf-8 -*-

from __future__ import print_function
import os
import xml.etree.ElementTree as ET
import config as cfg

def convert_voc_annotation(data_path, data_type, anno_path, use_difficult_bbox=True):
    classes = ['stamp']
    img_inds_file = os.path.join(data_path, data_type + '.txt')
    with file(img_inds_file, 'r') as f:
        txt = f.readlines()
        image_inds = [line.strip() for line in txt]

    with file(anno_path, 'w') as f:
        for image_ind in image_inds:
            image_path = os.path.join(data_path, 'images', image_ind + '.jpg')
            annotation = image_path
            label_path = os.path.join(data_path, 'annotations', image_ind + '.xml')
            root = ET.parse(label_path).getroot()
            objects = root.findall('object')
            for obj in objects:
                difficult = obj.find('difficult').text.strip()
                if (not use_difficult_bbox) and(int(difficult) == 1):
                    continue
                bbox = obj.find('bndbox')
                class_ind = classes.index(obj.find('name').text.lower().strip())
                xmin = bbox.find('xmin').text.strip()
                xmax = bbox.find('xmax').text.strip()
                ymin = bbox.find('ymin').text.strip()
                ymax = bbox.find('ymax').text.strip()
                annotation += ' ' + ','.join([xmin, ymin, xmax, ymax, str(class_ind)])
            annotation += '\n'
            print(annotation)
            f.write(annotation)
    return len(image_inds)

if __name__ == '__main__':
    ANNOT_DIR_PATH = "/data/pan/projects/digits/iron_data"
    DATASET_PATH = "/data/pan/projects/digits/iron_data"
    train_annotation_path = os.path.join(ANNOT_DIR_PATH, 'train_annotation.txt')
    test_annotation_path = os.path.join(ANNOT_DIR_PATH, 'test_annotation.txt')
    if os.path.exists(train_annotation_path):
        os.remove(train_annotation_path)
    if os.path.exists(test_annotation_path):
        os.remove(test_annotation_path)
    num1 = convert_voc_annotation(DATASET_PATH, 'trainval', train_annotation_path, False)
    num2 = convert_voc_annotation(DATASET_PATH, 'test', test_annotation_path, False)
    print(num1)
    print(num2)