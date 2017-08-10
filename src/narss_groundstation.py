# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "hani"
__date__ = "$Aug 10, 2017 9:51:54 PM$"

import SerialPortComm

if __name__ == "__main__":
    SerialPortComm.write(input("Send Message to Serial port >> "))
