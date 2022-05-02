import pandas as pd
import os
import xml.etree.ElementTree as eltree


df = pd.read_csv('./Train_car_split.csv')
directory_name = os.path.basename(os.getcwd())
full_path = os.path.abspath(os.getcwd())
root_elem = eltree.Element("main")
folder_name_elem = eltree.Element("folder")
full_path_elem = eltree.Element("path")
source_elem = eltree.Element("source")
size_elem = eltree.Element("size")
segmented_elem = eltree.Element("segmented")
object_elem = eltree.Element("object")
bounding_box_elem = eltree.Element("bndbox")
database_elem = eltree.SubElement(source_elem, "database")
file_name_elem = eltree.Element("filename")
width_elem = eltree.SubElement(size_elem, "width")
height_elem = eltree.SubElement(size_elem, "height")
depth_elem = eltree.SubElement(size_elem, "depth")

name_sub_elem = eltree.SubElement(object_elem, "name")
pose_sub_elem = eltree.SubElement(object_elem, "pose")

truncated_sub_elem = eltree.SubElement(object_elem, "truncated")
truncated_sub_elem.text = '0'

difficult_sub_elem = eltree.SubElement(object_elem, "difficult")
difficult_sub_elem.text = '0'

root_elem.append(folder_name_elem)
root_elem.append(full_path_elem)
root_elem.append(source_elem)
root_elem.append(size_elem)
root_elem.append(segmented_elem)
root_elem.append(object_elem)
root_elem.append(file_name_elem)

bounding_box_elem = eltree.SubElement(object_elem, "bndbox")
x_min = eltree.SubElement(bounding_box_elem, "xmin")
y_min = eltree.SubElement(bounding_box_elem, "ymin")
x_max = eltree.SubElement(bounding_box_elem, "xmax")
y_max = eltree.SubElement(bounding_box_elem, "ymax")

for index, row in df.iterrows():
    file_name = str(row['path'])

    folder_name_elem.text = directory_name
    file_name_elem.text = file_name
    full_path_elem.text = full_path

    database_elem.text = "Unknown"
    segmented_elem.text = "0"

    name_sub_elem.text = str(row['class_name'])

    pose_sub_elem.text = 'unspecified'

    x_min.text = str(row['x1'])
    y_min.text = str(row['y1'])
    x_max.text = str(row['x2'])
    y_max.text = str(row['y2'])
    tree = eltree.ElementTree(root_elem)

    with open(os.path.splitext(file_name)[0]+".xml", "wb") as files:
        tree.write(files)
        files.close()
