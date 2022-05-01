import pandas as pd
import os
import xml.etree.ElementTree as eltree

df = pd.read_csv('./image-label.csv')
DIRECTORY_NAME = os.path.basename(os.getcwd())
FULL_PATH = os.path.abspath(os.getcwd())
ROOT_ELEM = eltree.Element("Main")
FOLDER_NAME_ELEM = eltree.Element("folder")
FULL_PATH_ELEM = eltree.Element("path")
SOURCE_ELEM = eltree.Element("source")
SIZE_ELEM = eltree.Element("size")
SEGMENTED_ELEM = eltree.Element("segmented")
OBJECT_ELEM = eltree.Element("object")
BOUNDING_BOX_ELEM = eltree.Element("bndbox")

for index, row in df.iterrows():

    file_name = row['path']

    ROOT_ELEM.append(FOLDER_NAME_ELEM)
    ROOT_ELEM.append(FULL_PATH_ELEM)
    ROOT_ELEM.append(SOURCE_ELEM)
    ROOT_ELEM.append(SIZE_ELEM)
    ROOT_ELEM.append(SEGMENTED_ELEM)
    ROOT_ELEM.append(OBJECT_ELEM)
    FOLDER_NAME_ELEM.text = DIRECTORY_NAME
    FILE_NAME_ELEM = eltree.Element("filename")
    ROOT_ELEM.append(FILE_NAME_ELEM)
    FILE_NAME_ELEM.text = file_name
    FULL_PATH_ELEM.text = FULL_PATH
    DATABASE_ELEM = eltree.SubElement(SOURCE_ELEM, "database")
    DATABASE_ELEM.text = "Unknown"
    WIDTH_ELEM = eltree.SubElement(SIZE_ELEM, "width")
    HEIGHT_ELEM = eltree.SubElement(SIZE_ELEM, "height")
    DEPTH_ELEM = eltree.SubElement(SIZE_ELEM, "depth")
    SEGMENTED_ELEM.text = "0"
    NAME_SUB_ELEM = eltree.SubElement(OBJECT_ELEM, "name")
    NAME_SUB_ELEM.text = row['class_name']
    POSE_SUB_ELEM = eltree.SubElement(OBJECT_ELEM, "pose")
    POSE_SUB_ELEM.text = 'unspecified'
    TRUNCATED_SUB_ELEM = eltree.SubElement(OBJECT_ELEM, "truncated")
    TRUNCATED_SUB_ELEM.text = '0'
    DIFFICULT_SUB_ELEM = eltree.SubElement(OBJECT_ELEM, "difficult")
    DIFFICULT_SUB_ELEM.text = '0'
    BOUNDING_BOX_ELEM = eltree.SubElement(OBJECT_ELEM, "bndbox")
    X_MIN = eltree.SubElement(BOUNDING_BOX_ELEM, "xmin")
    Y_MIN = eltree.SubElement(BOUNDING_BOX_ELEM, "ymin")
    X_MAX = eltree.SubElement(BOUNDING_BOX_ELEM, "xmax")
    Y_MAX = eltree.SubElement(BOUNDING_BOX_ELEM, "ymax")
    X_MIN.text = str(row['x1'])
    Y_MIN.text = str(row['y1'])
    X_MAX.text = str(row['x2'])
    Y_MAX.text = str(row['y2'])
    tree = eltree.ElementTree(ROOT_ELEM)

    with open(os.path.splitext(file_name)[0]+".xml", "wb") as files:
        tree.write(files)
