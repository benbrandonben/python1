# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:06:46 2023

@author: uif46649
"""

import cantools
import can
import sys

dbc_file = r"D:\DSUsers\uif46649\ziliao\python\ADASCAN_S202_MCA_V3.1_20221027_FC_add55E.dbc"
dbc = cantools.db.load_file(dbc_file)

txtpath = r"D:\DSUsers\uif46649\ziliao\python\text.txt"
txtpath1 = r"D:\DSUsers\uif46649\ziliao\python\text1.txt"
txt = open(txtpath, 'w')
txt1 = open(txtpath1, 'w',encoding ='utf-8')
f = r"D:\DSUsers\uif46649\ziliao\python\2023.08.11_at_12.25.08_radar-mi_880_reset.blf"
log_data = can.BLFReader(f)
for msg in log_data:
    if msg.channel == 0:
        #根据DBC解析信号后输出
        decoded = {}
        try:
            dec = dbc.decode_message(msg.arbitration_id, msg.data)
            if dec:
                for key, data in dec.items():
                    if key not in decoded:
                        decoded[key] = []
                    decoded[key].append([hex(msg.arbitration_id),msg.timestamp,data])
                    if msg.arbitration_id == 0x244:
                        #print("signal name:{<30}CAN_ID:{<10}data:{}".format(key,hex(msg.arbitration_id),msg.timestamp,data), file=txt1)
                        print(msg.timestamp,'%-5s' % hex(msg.arbitration_id),'%-10s' % key,data, file=txt1)
                    #if data not in decoded:
                        #decoded[data] = []
                    #decoded[data].append([msg.timestamp, msg.arbitration_id])
        except:
            pass
        #将blf中的msg打印输出到txt文件中
        if msg.arbitration_id == 0x244:
            print(msg, file = txt)
            #print(decoded, file=txt1,sep="\n")
            #print(key,data, file=txt1)
#    else :
        #print("无效")
            #print(msg.arbitration_id)   


