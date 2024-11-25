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

make .json file
switch imports around
"""



import socket
import time
import folium
import json
import requests
from geoip2.database import Reader


def geolocate(ip, reader):
    """fetch the lat and long from the geoip2 db"""
    try:
        response = reader.city(ip)
        return response.location.latitude, response.location.longitude
    except:
        print(f"No Response from {ip}...")
        return None, None


def traceroute(destination, max_hops=5, timeout=5, log_file ="traceroute_outfile.json"):
    # get the destination IP address
    dest_ip = socket.gethostbyname(destination)
    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops.")  
    # open the db
    Reader = Reader(db_path)
    ttl = 1
    while ttl <= max_hops:
            start_time = time.time() # idk where to put this

            # create send/recieve socket
            recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            send_socket.socket.opt(socket.SQL_IP, socket.IP_TTL, ttl)
            recv_socket.settimeout(timeout)
        
        # try recieve
            try:
                send_socket.sendto(b''(dest_ip,33434))
                data, addr = recv_socket.recvfrom(512)
                end_time = time.time()
                rtt = round((end_time - start_time) * 1000, 2) # rount trip time

                ip_address = addr[0]
                lat, lon = geolocate(ip_address, Reader)
                hop_info = {
                    "hop": ttl,
                    "ip": ip_address,
                    "rtt_ms": rtt,
                    "latitude": lat,
                    "longitude": lon
                }
                traceroute_data["Hops"].append(hop_info)

                print(f"{ttl}\t{ip_address}\t{rtt} ms\tLocation: ({lat}, {lon})")

                if ip_address == dest_ip:
                    print("Reached Destination...")
                    break
            except socket.timeout:
                traceroute_data["hops"].append({
                    "hop": ttl,
                    "ip": None,
                    "rtt_ms": None,
                    "latitude": None,
                    "longitude": None
                })
                print(f"{ttl}\tRequest timed out...")
            finally:
                recv_socket.close()
                send_socket.close

            ttl += 1

    Reader.close()  # close db

    # save to file
    with open(log_file, "w") as file:
        json.dump(traceroute_data, file, indent=4)

    print(f"\nTraceroute complete... everything saved to {log_file}...")
                




if __name__ == "__main__":
    destination = input("Enter the IP address or domain name of the destination: ")
    traceroute(destination)
    






"""
# does not work below

def geolocate(ip):
    global ipinfo 

    if not ip:
        return None, None
    handler = ipinfo.getHandler(token) # either pass token or make it a global
    details = handler.getDetails(ip)
    loc = details.loc
    if loc:
        return map(float, loc.split(","))
    return None, None

def plot_hops(hops, token): # put in the 
    geolocations = []
    for ip in hops:
        if ip:
            lat, lon = geolocations(ip, token)
        if lat and lon:
                geolocations.append((lat, lon))
        
    if not geolocations:
        print("No valid geolocations to plot...")
        return
    map_center = geolocations[0]
    base_map = folium.Map(location=map_center, zoom_start=4)

    for i, (lat, lon) in enumerate(geolocations, start=1):
        folium.Marker(
            location=(lat, lon),
            popup=f"Hop {i}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(base_map)

    folium.PolyLine(geolocations, color="blue").add_to(base_map)
    base_map.save("traceroute_map.html")
    print("Map saved to traceroute_map.html")


token = "" # get from web
    hops = traceroute(destination)  # Ensure this function returns hops
    plot_hops(hops, token)
    


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
"""

"""
    WAS AT LINE 50 FOR THE .TXT
    # Open the log file
    with open(log_file, "w") as file:
        # Header for the log file
        header = (f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops: \n")
        file.write(header)

        # hops
        hops = []
        ttl = 1
"""