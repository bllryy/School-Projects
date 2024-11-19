"""
Name: 
Section: 275-02
Desc: Project 1

"""

"""
Approach:
Get the empty arrays for hops and max hops
    also ttl if it dosent work
Spawn a send socket that sends the initial ping 
ping comes back and hits the recieve socket
print what we get back in the format
also web version in a website to get the line limit


while loop goes over and prints first location, second location, third, etc...
while ttl <= max_hops do while
"""



import socket
import struct
import time
#from scapy.all import *
import argparse
import string
import sys
import geopy
import requests
import folium



def traceroute(destination, max_hops=5, timeout=5, log_file ="traceroute_outfile.txt"):
    # get the destination IP address
    dest_ip = socket.gethostbyname(destination)
    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops.")
    
    # Open the log file
    with open(log_file, "w") as file:
        # Header for the log file
        header = (f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops: \n")
        file.write(header)

        # hops
        hops = []
        ttl = 1


        while ttl <= max_hops:

            start_time = time.time() # idk where to put this

            # create send/recieve socket
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

            # Set the ttl for out
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            recv_socket.settimeout(timeout)

            # send packet
            print(f"Sending packet with TTL = {ttl}...")
            send_socket.sendto(b'', (dest_ip, 33434))


        # try recieve
            try:
                data, addr = recv_socket.recvfrom(512)
                end_time = time.time()
                rtt = round((end_time - start_time) * 1000, 2) # rount trip time
                

                # print and log the hop information
                hop_info = (f"{ttl}\t{addr[0]}\t{rtt} ms\n")
                print(hop_info.strip())
                file.write(hop_info)

                hops.append(addr[0])

                # check for destination (also to end the try statement)
                if addr[0] == dest_ip:
                    print("Reached!")
                    file.write('Reached destination.\n')
                    break

            except socket.timeout:
                # Timeouts
                timeout_msg = (f"{ttl}\tRequest time out... \n")
                print(timeout_msg.strip())
                file.write(timeout_msg)
            
            finally:
                # clean the sockets
                recv_socket.close()
                send_socket.close()

            # Inciment for the next jump...
            ttl += 1

        # print the completion messg
        completion_msg = ("\nTraceroute complete.\n")
        print(completion_msg.strip())
        file.write(completion_msg)

def geolocate(ip):
    # ex using ipinfo.io
    url = f"https://ipinfo.io/{ip}/json" # change ip to what ever
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        loc = data.get("loc", None) # loc returns "lat and long"
        if loc:
            lat, lan = map(float, loc.split(','))
            return lat, lan
        return None, None

def plot_hops(hops): # again change when ready
    # create a map centered at the first hop
    base_map = folium.Map(location=hops[0], zoom_start=4)

    # add markers for each loop
    for index, (lat, lon) in enumerate(hops, start=1)
        if lat and lan:
            folium.Marker(
                location=(lat, lan),
                poput=f"Hop {index}"
                icon = folium.Icon(color="blue", icon="info-sign")
            ).add_to(base_map)

        # save to a html
        base_map.save('tracdroute_map.html')


if __name__ == "__main__":
    destination = input("Enter the IP address or domain name of the destination: ")
    traceroute(destination)