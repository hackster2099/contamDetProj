import cv2 as cv
import numpy as np
import os
import sys
import torch 
import torch.nn as nn
from setLoad import MyDataset

cleanDataSet = "/Users/faresshirali/Desktop/McNair/pythonFiles/imgBank/realistic_synthetic_petri_dataset/clean"
contDataSet = "/Users/faresshirali/Desktop/McNair/pythonFiles/imgBank/realistic_synthetic_petri_dataset/contaminated"


dataSetList = [cleanDataSet, contDataSet]
dataSetLabel = [0,1]

dataset = MyDataset(dataSetList, dataSetLabel)


dataset.__getitem__(0,3)










