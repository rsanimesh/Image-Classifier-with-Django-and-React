from django.apps import AppConfig
from torchvision import models, transforms
from PIL import Image
import torch

class ImagesConfig(AppConfig):
    name = 'images'
