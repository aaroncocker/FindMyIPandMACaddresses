#!/usr/bin/python3

# import packages and throw an exception should they not be installed 
try:
    import ipaddress
    import socket
    import uuid
    import binascii

except:
    print("Error! Unable to find needed Python 3 packages on your system.")
      
def main():
    # open socket connection 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
   
    # extract MAC address from operating system as hex value and convert to string and assign IP address to variable
    mac_address = hex(uuid.getnode())
    mac_address = str(mac_address)
    ip_address = s.getsockname()[0]
   
    # close socket connection
    s.close()
   
    # partition mac address into pairs and insert a colon to format as a human readable MAC address
    formatted_mac_address = [mac_address[i:i+2] for i in range(0, len(mac_address), 2)]
    
    # determine whether not network is IPv4 or IPv6
    ip_network_type = ipaddress.ip_address(ip_address).version
    
    # print out addresses 
    print("Your IP address is",ip_address)
    print("Your MAC address is",':'.join(formatted_mac_address))
    print("You have an IPv",ip_network_type,"network address")

# run main program subroutine    
main()
