import os
import socket
import time
import IP2Location
import json
import folium

def traceroute(destination, max_hops=30, timeout=5, log_file="traceroute_outfile.json", db_path = "/usr/local/share/ip2location/IP2LOCATION-LITE-DB5.IPV6.BIN"):
    # expand the user home directory in the database db_path
    # db_path = os.path.expanduser(db_path)

    # Load IP2Location database
    try:
        ip2location_db = IP2Location.IP2Location(db_path)
    except Exception as e:
        print(f"Error loading IP2Location database: {e}. Please check the database location and name.")
        return
    
    try:
        dest_ip = socket.gethostbyname(destination)
    except socket.gaierror as e:
        print(f"Error resolving destination {destination}: {e}")
        return

    print(f"Traceroute to {destination} ({dest_ip}), max {max_hops} hops.")

    traceroute_data = {
        "destination": destination,
        "destination_ip": dest_ip,
        "hops": []
    }

    ttl = 1
    while ttl <= max_hops:
        start_time = time.time()

        # Create sockets
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        recv_socket.settimeout(timeout)

        try:
            # Send UDP packet to an unreachable port
            send_socket.sendto(b"", (dest_ip, 33434))
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
                "country": country
            }
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
                "country": None
            })
            print(f"{ttl}\tRequest timed out...")
        finally:
            recv_socket.close()
            send_socket.close()

        ttl += 1

    # Save results to JSON
    with open(log_file, "w") as file:
        json.dump(traceroute_data, file, indent=4)
    print(f"\nTraceroute complete. Results saved to {log_file}.")

def visualize_traceroute_on_map(json_file, output_map="traceroute_map.html"):
    try:
        with open(json_file, "r") as file:
            traceroute_data = json.load(file)
    except Exception as e:
        print(f"Error reading traceroute JSON file: {e}")
        return

    # Create a base map centered at an approximate starting point
    base_map = folium.Map(location=[0, 0], zoom_start=2)

    for hop in traceroute_data.get("hops", []):
        if hop["latitude"] is not None and hop["longitude"] is not None:
            # Add a marker for each hop
            folium.Marker(
                location=[hop["latitude"], hop["longitude"]],
                popup=(
                    f"Hop: {hop['hop']}<br>"
                    f"IP: {hop['ip']}<br>"
                    f"RTT: {hop['rtt_ms']} ms<br>"
                    f"Country: {hop['country']}"
                ),
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(base_map)

    # Save the map to an HTML file
    base_map.save(output_map)
    print(f"Map visualization saved as {output_map}")

if __name__ == "__main__":
    destination = input("Enter the IP address or domain name of the destination: ")
    traceroute(destination)

