import socket
from socket import *
import time
import IP2Location
import json
import os


def traceroute(destination, max_hops=30, timeout=5, log_file="traceroute_outfile.json", db_path = "/usr/local/share/ip2location/IP2LOCATION-LITE-DB1.IPV6.BIN"): # pls fix above
    # Load IP2Location database  MAKE A DIR THAT YOU CAN PUT THE FILE IN !!!!!! ABSOLUTE MUST HAVE !!!!!!!
    try:
        ip2location_db = IP2Location.IP2Location(db_path)
    except Exception as e:
        print(f"Error loading IP2Location database: {e}... plse check the db location file and name...")
        return
    
    dest_ip = socket.gethostbyname(destination)
    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops.")

    traceroute_data = {
        "destination": destination,
        "destination_ip": dest_ip,
        "hops": []
    }

    ttl = 1
    while:
        start_time = time.time

        # making the sockets
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.settimeout(timeout)

        try:
            send_socket.sendto('b', dest_ip, 33434)
            data, addr = recv_socket.recvfrom(512)
            end_time = time.time()

            ip_address = addr[0]
            rtt = round((end_time - start_time) * 1000, 2)  # Round-trip time in ms

            # Get geolocation
            location_data = ip2location_db.get_all(ip_address)
            latitude = location_data.latitude
            longitude = location_data.longitude
            country = location_data.country_long

            hop_info = {
                "hop": ttl,
                "ip": ip_address,
                "rtt_ms": rtt,
                "latitude": latitude,
                "longitude": longitude,
                 "country": country }
            traceroute_data["hops"].append(hop_info)

            print(f"{ttl}\t{ip_address}\t{rtt} ms\t{country} ({latitude}, {longitude})")

            if ip_address == dest_ip:
                print("Reached destination.")
                break
        except socket.timeout:
            traceroute_data["hops"].append({
                "hop": ttl,
                "ip": None,
                "rtt_ms": None,
                "latitude": None,
                "longitude": None,
                "country": None })
            
            print(f"{ttl}\tRequest timed out...")
        finally:
            recv_socket.close()
            send_socket.close()

        ttl += 1

# Save results to JSON
    with open(log_file, "w") as file:
        json.dump(traceroute_data, file, indent=4)
    print(f"\nTraceroute complete. Results saved to {log_file}.")

if __name__ == "__main__":
    destination = input("Enter the IP address or domain name of the destination: ")
    traceroute(destination)
