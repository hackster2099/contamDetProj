import cv2 as cv
import numpy as np
import os
import sys
import torch 
import torch.nn as nn
from setLoad import MyDataset
from torch.utils.data  import DataLoader

imgBankPath = "/Users/faresshirali/Desktop/McNair/pythonFiles/imgBank/realistic_synthetic_petri_dataset"


dataSet = MyDataset(imgBankPath)
dataSet.__getitem__(21)








