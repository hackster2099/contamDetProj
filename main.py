import cv2 as cv
import numpy as np
import os
import sys
import torch 
import torch.nn as nn
from setLoad import MyDataset


imgBankPath = "/Users/faresshirali/Desktop/McNair/pythonFiles/imgBank/realistic_synthetic_petri_dataset"


dataset = MyDataset(imgBankPath)





