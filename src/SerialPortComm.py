

__author__ = "hani"
__date__ = "$Aug 10, 2017 10:26:07 PM$"


from serial.tools import list_ports

def getPorts():
    for i in range (0,len(list_ports.comports())):
        print (int(i),")",list_ports.comports()[i].device," > ",list_ports.comports()[i].description)
    
    

   
    
def main():
    getPorts()
    portNo = int(input("\nSelect Port >> "))
    print (list_ports.comports()[portNo].device)
    