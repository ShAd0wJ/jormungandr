#!/usr/bin/env python

import subprocess
import random
from random import randint, choice
from sys import argv
from string import hexdigits


def randIP(v):
    if v == 4:
        octets = []
        for x in range(4):
            octets.append(str(randint(0,255)))
        return '.'.join(octets)

    elif v == 6:
        octets = []
        for x in range(8):
            octet = []
            for x in range(4):
                octet.append(str(choice(hexdigits.lower())))
            octets.append(''.join(octet))
        return ':'.join(octets)

    else:
       return

def randMac():
    #alots for the random mac and returns the value of said random mac address
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
    )

def randMacGateway():
    #alots for the random mac and returns the value of said random mac address
    return "%02x:%02x:%02x:%02x:%02x:1" % (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
    )


def randMacChange():
    # First the wifi interfaces are taken down and reconfigured
    MAC=randMac()
    subprocess.call("sudo ifconfig wlan0 down && ifconfig wlan1 down", shell=True)
    subprocess.call("sudo ifconfig wlan0 hw ether " + MAC, shell=True)
    subprocess.call("sudo ifconfig wlan1 hw ether " + MAC, shell=True)
    subprocess.call("sudo ifconfig wlan0 up && ifconfig wlan1 up", shell=True)

def randIPChange():
    #second, the ip address of both interfaces are reconfigured using netmask
    IPv4=randIP(int(4))
    IPv6=randIP(int(6))
    subprocess.call("sudo ifconfig wlan0 " + IPv4, shell=True)
    subprocess.call("sudo ifconfig wlan1 " + IPv4, shell=True)

#Experimental
#def defaultGatewayChange():
    #third, the default gateway needs to be changed so that the address isn't traced back to the users router even if computer is disguised
#    gate=randMacGateway()
#    subprocess.call("sudo route add default gw " + gate, shell=True )

randMacChange()
randIPChange()
#defaultGatewayChange()
