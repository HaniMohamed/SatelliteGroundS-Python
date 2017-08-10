

__author__ = "hani"
__date__ = "$Aug 10, 2017 10:26:07 PM$"


from serial.tools import list_ports
import serial




def getPorts():
    for i in range (0,len(list_ports.comports())):
        print (int(i),")",list_ports.comports()[i].device," > ",list_ports.comports()[i].description)
    
    
def write(message):
    ser = serial.Serial(list_ports.comports()[portNo].device)  # open serial port
    print(ser.name)         # check which port was really used
    ser.write(message.encode( ))     # write a string
    ser.close() 

      
getPorts()
portNo = int(input("\nSelect Port >> "))
