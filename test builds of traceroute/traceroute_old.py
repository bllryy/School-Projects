import time
#from scapy.all import *
import argparse
import string
import sys



def tracroute(destination, max_hops=30, timeout=5):
    # hops
    hops = []
    ttl = 5

    #get ip
    dest_ip = socket.gethostbyname(destination)
    address = (dest_ip, 3343)
    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops:")



    while ttl <= max_hops:

        # create send/recieve socket
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        # Set the ttl of the socket/options?????
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.settimeout(timeout)

        # send packet
        print(f"Sending packet with TTL = {ttl}...")
        start_time = time.time()
        send_socket.sendto(b'', address)

        socket.recvfrom(address,dest_ip)


# decremnt ttl for reive
# https://docs.python.org/3/library/socket.html#socket.socket.recv




if __name__ == "__main__":
    destination = input("Enter the IP address or domain name of the destination: ")
    tracroute(destination)
