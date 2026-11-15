import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
import os
import cv2 as cv

imgCleanFolder = "/Users/faresshirali/Desktop/McNair/pythonFiles/imgBank/realistic_synthetic_petri_dataset/clean"
imgContFolder = "/Users/faresshirali/Desktop/McNair/pythonFiles/imgBank/realistic_synthetic_petri_dataset/contaminated"



class MyDataset(Dataset):

   # instance variable, it contains image file paths as an array
   imgCollection: list

   # instance variable, it contains image file paths as an array
   lableCollection: list

   def __init__(self, imgCollection:list, labelCollection:list):
      
      self.imgCollection = imgCollection
      self.lableCollection = labelCollection

   def __getitem__(self, folderType:int ,index:int):
   
      # is it needed ? 
      #cleanFileName:str = "/clean_"
      #contFileName:str = "/contaminated_"

      if(folderType == 0):
         partialPath = str(self.imgCollection[0])

      elif(folderType == 1):
         partialPath = str(self.imgCollection[1])

      fileList = os.listdir(partialPath)

      print(str(fileList) + "\n")

      return fileList[index]


   # folder type referes to the type of images i want to look at. 0 for clean folder, 1 for contaminated folder
   def __len__(self, folderType:int):

      fileCount:int = 0
      fileList:list
      
      if(folderType == 0):
         filePath = str(self.imgCollection[0])

      elif (folderType == 1): 
         filePath = str(self.imgCollection[1])

      fileList = os.listdir(filePath)
   
      fileCount = len(fileList)

      return fileCount

