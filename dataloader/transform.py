from PIL import Image
from torchvision import transforms
import numpy as np
import torch

# Compose
class Compose(object):
    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, img, anno_class_img):
        for t in self.transforms:
            img, anno_class_img = t(img, anno_class_img)
        return img, anno_class_img

# Resize
class Resize(object):
    def __init__(self, resize: tuple):
        self.resize = resize

    def __call__(self, img, anno_class_img):
        img = img.resize(self.resize,
                         Image.BICUBIC)
        anno_class_img = anno_class_img.resize(
            self.resize, Image.NEAREST)

        return img, anno_class_img

# Normalize
class Normalize_Tensor(object):
    def __init__(self, color_mean: tuple, color_std: tuple):
        self.color_mean = color_mean
        self.color_std = color_std

    def __call__(self, img, anno_class_img):

        # PIL to Tensor, also normalize size
        img = transforms.functional.to_tensor(img)

        # normalize colour
        img = transforms.functional.normalize(
            img, self.color_mean, self.color_std)

        # transform img to numpy
        anno_class_img = np.array(anno_class_img)  # [height][width]

        # 'ambigious' has 255, so use for background 
        index = np.where(anno_class_img == 255)
        anno_class_img[index] = 0

        # annotation umg to tensor
        anno_class_img = torch.from_numpy(anno_class_img)

        return img, anno_class_img

class DataTransform():
    def __init__(self, resize, color_mean, color_std, mode):
        if mode == 'train':
            self.data_transform = Compose([
                Resize(resize),
                Normalize_Tensor(color_mean, color_std)
            ])
        elif mode == 'eval':
            self.data_transform = Compose([
                Resize(resize),
                Normalize_Tensor(color_mean, color_std)
            ])

    def __call__(self, img, anno_class_img):
        return self.data_transform(img, anno_class_img)
