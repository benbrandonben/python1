# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:29:55 2023

@author: uif46649
"""

import sys 
import time
  
# stdout assigned to a variable 
#var = sys.stdout 
var=["","*","**","***","****","*****"]
#arr = ['geeks', 'for', 'geeks'] 
  
# printing everything in the same line 
#while(1)
#for i in range(5) : 
    #print(i,end='')
    #var.write(i) 
#for i in range(2):
for i in range(20):
    #sys.stdout=open(sys.stdout.fileno(),'w',0)
    m=i%5
    #print(m)
    if m==0:
        sys.stdout.flush()
    #print("\r 请等待：",'%s'%a, end="", flush=True)
    sys.stdout.write('\r请等待：{0}'.format(var[m+1]))
    
    
    time.sleep(0.5)
        #sys.stdou.close()
            
    #sys.stdout.write("\r")
    #sys.stdout.flush()
    #print("\r", end="", flush=True)
    #print('*',flush=True)
    #time.sleep(0.5)
    
# printing everything in a new line 
#for j in arr: 
#    var.write('\n'+j)

