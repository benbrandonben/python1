# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:41:36 2023

@author: uif46649
"""

#def printadd(path):
#    print("文件路径：", path)
    
#textpath = r"D:\DSUsers\uif46649\ziliao\python\reset_reason.txt"
#printadd(textpath)

from ctypes import *

raw=open(r"D:\DSUsers\uif46649\ziliao\python\test11\src\reset_reason1.txt",'rb')
for i in range (3):
    record = raw.read(10)
    with open(r"D:\DSUsers\uif46649\ziliao\python\test11\src\reset_reason2.txt",'w') as file0:
        print(record,'.\n',file=file0)
#    print(frame)