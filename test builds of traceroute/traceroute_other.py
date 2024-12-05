import socket
import time
import json
from geoip2.database import Reader

def geolocate(ip, reader):
    """Fetch latitude and longitude for a given IP address using a local GeoLite2 database."""
    try:
        response = reader.city(ip)
        return response.location.latitude, response.location.longitude
    except Exception as e:
        print(f"Error fetching geolocation for IP {ip}: {e}")
        return None, None

def traceroute(destination, max_hops=5, timeout=5, log_file="traceroute_outfile.json", db_path="GeoLite2-City.mmdb"):
    dest_ip = socket.gethostbyname(destination)
    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops.")
    
    traceroute_data = {
        "name": "Project 1",
        "section": "275-02",
        "description": "Traceroute with geolocation",
        "destination": destination,
        "destination_ip": dest_ip,
        "hops": []
    }

    try:
        reader = Reader(db_path)  # Open the GeoLite2 database
    except FileNotFoundError:
        print("GeoLite2 database not found. Please ensure the path is correct.")
        return

    ttl = 1
    while ttl <= max_hops:
        start_time = time.time()

        # Create sockets
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.settimeout(timeout)

        try:
            send_socket.sendto(b'', (dest_ip, 33434))
            data, addr = recv_socket.recvfrom(512)
            end_time = time.time()
            rtt = round((end_time - start_time) * 1000, 2)

            ip_address = addr[0]
            lat, lon = geolocate(ip_address, reader)
            hop_info = {
                "hop": ttl,
                "ip": ip_address,
                "rtt_ms": rtt,
                "latitude": lat,
                "longitude": lon
            }
            traceroute_data["hops"].append(hop_info)

            print(f"{ttl}\t{ip_address}\t{rtt} ms\tLocation: ({lat}, {lon})")

            if ip_address == dest_ip:
                print("Reached destination.")
                break
        except socket.timeout:
            traceroute_data["hops"].append({
                "hop": ttl,
                "ip": None,
                "rtt_ms": None,
                "latitude": None,
                "longitude": None
            })
            print(f"{ttl}\tRequest timed out.")
        finally:
            recv_socket.close()
            send_socket.close()

        ttl += 1

    # Close the database
    reader.close()

    # Save the traceroute data to a JSON file
    try:
        with open(log_file, "w") as file:
            json.dump(traceroute_data, file, indent=4)
        print(f"\nTraceroute complete. Results saved to {log_file}.")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")

if __name__ == "__main__":
    destination = input("Enter the IP address or domain name of the destination: ")
    traceroute(destination)
