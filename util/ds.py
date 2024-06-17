import os
from PIL import Image
import numpy as np


def load_dataset(images_path, labels_path):
    images = []
    labels_f = []

    for image_file in os.listdir(images_path):
        if image_file.endswith('.jpg'):
            image = Image.open(os.path.join(images_path, image_file))
            image = image.resize((320, 320))
            image_array = np.array(image) / 255.0
            images.append(image_array)

            file_name = os.path.splitext(image_file)[0]
            label_path = os.path.join(labels_path, file_name + '.txt')

            if os.path.exists(label_path):
                with open(label_path, 'r') as f:
                    lines = f.readlines()
                    labels = [line.split() for line in lines]
                    labels = [int(label[0]) for label in labels]
                    label = labels[0] if labels else 5
                    labels_f.append(label)
            else:
                labels_f.append(5)  # No label found for this image

    print(f"Total images loaded: {len(images)}")
    print(f"Total labels loaded: {len(labels_f)}")

    return images, labels_f
