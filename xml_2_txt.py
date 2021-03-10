import xml.etree.ElementTree as ET
import os

sets = ['train', 'valid']
classes = ['tjfy','tjzp','tjpm','c','qr']  # 更改为自己训练的类别


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_set,image_id):
    in_file = open(r'F:\yolov5_Test\data\Annotations/%s.xml' % (image_id))                     #修改路径
    out_file = open(r'F:\yolov5_Test\data\labels/{}/{}.txt' .format(image_set,image_id), 'w')  #修改路径
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


for image_set in sets:
    if not os.path.exists('data/labels/{}'.format(image_set)):
        os.makedirs('data/labels/{}'.format(image_set))
    image_ids = open('data/ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
    print(image_ids)
    for image_id in image_ids:
        convert_annotation(image_set,image_id)

