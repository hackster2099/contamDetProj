import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math
import os
import cv2 as cv


class MyDataset(Dataset):

   # instance variable, it contains image file paths as an array
   imgCollection: list

   # instance variable, it contains image file paths as an array
   labelCollection: list

   def __init__(self, rootPath:str):
      
      self.imgCollection = []
      self.labelCollection = []

      cleanImgPath:str = str(rootPath) + "/clean"
      contImgPath:str = str(rootPath) + "/contaminated"

      for NumOfFiles in range(0, (len(os.listdir(cleanImgPath))-1)):
         for files in (os.listdir(cleanImgPath)):
            if(files.startswith("clean_" + str(NumOfFiles) + ".png")):
               self.imgCollection.append(os.path.join(cleanImgPath, files))
               self.labelCollection.append(0)
               break
      

      for NumOfFiles in range(0, (len(os.listdir(contImgPath))-1)):
         for files in (os.listdir(contImgPath)):
            if(files.startswith("contaminated_" + str(NumOfFiles) + ".png")):
               self.imgCollection.append(os.path.join(contImgPath, files))
               self.labelCollection.append(1)
               break
         
   def __getitem__(self, index:int):

      return self.imgCollection[index]

   # folder type referes to the type of images i want to look at. 0 for clean folder, 1 for contaminated folder
   def __len__(self):
      return len(self.imgCollection)

