# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "hani"
__date__ = "$Aug 10, 2017 9:51:54 PM$"

import serial


if __name__ == "__main__":
    print ("Hello World")
    ser = serial.Serial(0)  # open first serial port
    print (ser.portstr)       # check which port was really used