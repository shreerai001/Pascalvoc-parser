from xml.etree import ElementTree
import pandas as pd
import glob

final_data = pd.DataFrame()

for file in glob.glob('resources/*.xml'):
    dom = ElementTree.parse(file)

    path = dom.find('filename').text

    for cars_obj in dom.findall('object'):
        cars_class = cars_obj.find('name').text

        for coordinate in cars_obj.findall('bndbox'):
            x1 = coordinate.find('xmin').text
            y1 = coordinate.find('ymin').text
            x2 = coordinate.find('xmax').text
            y2 = coordinate.find('ymax').text

    cars_columns = ['path', 'x1', 'y1', 'x2', 'y2', 'class_name']
    data = [[path, x1, y1, x2, y2, cars_class]]

    df = pd.DataFrame(data, columns=cars_columns)
    final_data = final_data.append(df)


final_data.to_csv('image-label.csv', index=False)