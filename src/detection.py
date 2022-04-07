"""
Saves a list of bounding boxes for an specific file in the Pascal VOC format.

Requirements: lxml
   pip install lxml==4.7.1

Example of usage:
    bbox1 = [80, 700, 100, 750]  # xmin, ymin, ymax, ymax
    bbox1 = [85, 705, 105, 755]
    bboxes = np.stack([bbox1, bbox2], axis=0)

    bbox2pascalvoc(bboxes,
                   input_filename="random.jpg",
                   classes=["classname1", "classname2"],
                   image_size=(512, 512, 3),
                   output_filename="random.xml")

References:
    - https://titanwolf.org/Network/Articles/Article?AID=5ed754ac-646d-47b6-843c-2282408c2fda
    - https://www.kaggle.com/dschettler8845/vinbigdata-convert-annotations-to-pascal-voc-xml

"""
import xml.etree.ElementTree as ET

from lxml.etree import Element, SubElement


def bbox2pascalvoc(bboxes, classes, input_filename, image_size, output_filename):
    """
    Convert a list of bounding boxes into the Pascal VOC format for a file.

    Args:
        bboxes: (list) [number_bboxes, xmin, ymin, xmax, ymax]
        classes: (list) [number_bboxes] class name of each bounding box
        input_filename: (str) filename of the input file for which the annotations
         were generated.
        image_size: (int, int, int) tuple with (width, height, channels)
         of the original input image
        output_filename: (str) output filename (.xml)

    Returns:
        - None

    """
    node_root = Element("annotation")

    # Header
    node_folder = SubElement(node_root, "folder")
    node_folder.text = "folder"

    node_filename = SubElement(node_root, "filename")
    node_filename.text = input_filename

    # Image size fields
    width, height, channels = image_size
    node_size = SubElement(node_root, "size")
    node_width = SubElement(node_size, "width")
    node_width.text = str(width)
    node_height = SubElement(node_size, "height")
    node_height.text = str(height)
    node_depth = SubElement(node_size, "depth")
    node_depth.text = str(channels)

    # Objects
    for bbox, current_class in zip(bboxes, classes):
        node_object = SubElement(node_root, "object")
        node_name = SubElement(node_object, "name")
        node_name.text = current_class
        # Other default fields that we set with some random values
        node_difficult = SubElement(node_object, "difficult")
        node_difficult.text = "0"
        node_truncated = SubElement(node_object, "truncated")
        node_truncated.text = "0"

        # Current bounding box
        node_bndbox = SubElement(node_object, "bndbox")
        node_xmin = SubElement(node_bndbox, "xmin")
        node_xmin.text = str(bbox[0])
        node_ymin = SubElement(node_bndbox, "ymin")
        node_ymin.text = str(bbox[1])
        node_xmax = SubElement(node_bndbox, "xmax")
        node_xmax.text = str(bbox[2])
        node_ymax = SubElement(node_bndbox, "ymax")
        node_ymax.text = str(bbox[3])

    tree = ET.ElementTree(node_root)
    tree.write(output_filename, encoding="unicode")
