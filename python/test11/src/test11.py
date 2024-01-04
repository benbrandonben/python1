# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from ctypes import *
import can
import os
    
class CanHeadInfo(Structure):
    _pack_ = 1
    _fields_ = [
        ("ECUHwVersion_Buffer", c_ubyte * 15),  # ECU硬件版本号 F191
        ("DcmDID_ECUSN_a", c_ubyte * 13),  # F194
        ("VINDataIdentifier", c_ubyte * 17),  # F190
        ("DID_CA_Fingerprint_a", c_ubyte * 7),  # 应用程序刷写指纹信息 F184
        ("ECUSwVersion_Buffer", c_ubyte * 15),  # ECU软件版本号 F189
        ("ECU_Hardware_Number", c_ubyte * 21),  # ECU硬件件号 F187
        ("ECUSoftware_Number", c_ubyte * 20),  # ECU软件件号 F188
    ]


class CanData(Structure):
    _pack_ = 1
    _fields_ = [
        ("timestamp", c_uint64),  # 1970-1-1 0:0到当前的微秒数
        ("can_id", c_uint16),
        ("channel", c_uint8),  #  报文通道号：1-1R1V，2-Reserved，3-ADAS ACAN, 4-Reserved
        ("data_length", c_uint8),
        ("data", c_ubyte * 64),
        #("data", c_ulong ),
    ]



class ADRBIN:
    SIZE_DATA = sizeof(CanData)
    SIZE_HEAD = sizeof(CanHeadInfo)    
    
    def __init__(self, path):
        print("文件路径：", path)
        self.raw=open(path,'rb')
        self.rawhead =CanHeadInfo.from_buffer_copy(self.raw.read(self.SIZE_HEAD))
        #with open("./reset_reason.txt",'w') as file0:
        #    print(self.rawhead.DcmDID_ECUSN_a,'\n',self.rawhead.ECUHwVersion_Buffer,file=file0)
        self.msgs=[]
        #print("framecnt",self.frame_cnt())
        for i in range(self.frame_cnt()):
        #for i in range(5):
            record = self.raw.read(self.SIZE_DATA)
            #print(record,'/n')
            frame = CanData.from_buffer_copy(record)
            if frame.data_length==0:
                print("零")
            else:
                print("dlc",frame.data_length)
                msg = can.Message(
                    timestamp=frame.timestamp / 1e6,
                    arbitration_id=frame.can_id,
                    is_extended_id=False,
                    bitrate_switch=True,
                    is_fd=True,
                    channel=frame.channel - 1,
                    dlc=frame.data_length,
                    data=[frame.data[i] for i in range(frame.data_length)],
                    )
                self.msgs.append(msg)
    
    def to_blf(self, path=None):
        blffile = (
            can.BLFWriter(self.raw.name + ".blf")
            if path is None
            else can.BLFWriter(path)
        )
        [blffile.on_message_received(msg) for msg in self.msgs]
        blffile.file.close()
        print("blf file ", blffile.file.name, " created") 

    def to_asc(self, path=None):
        ascfile = (
            can.ASCWriter(self.raw.name + ".asc")
            if path is None
            else can.ASCWriter(path)
        )
        [ascfile.on_message_received(msg) for msg in self.msgs]
        ascfile.file.close()
        print("ASC file ", ascfile.file.name, " created")           
        
    def filesize(self):
        return (os.path.getsize(self.raw.name))

    def frame_cnt(self):
        return((self.filesize()-sizeof(CanHeadInfo))//sizeof(CanData))


if __name__ == "__main__":
    
    textpath = r".\52000010100063070.dat"
    adr=ADRBIN(textpath)
    adr.to_blf()
    adr.to_asc()