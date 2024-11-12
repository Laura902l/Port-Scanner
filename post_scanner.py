import socket
import ipaddress
from common_ports import PORTS

def get_open_ports(target, port_range, verbose=False):
    # Validate if the target is a valid URL or IP address
    try:
        ipaddress.ip_address(target)
    except ValueError:
        try:
            # Try resolving the domain to IP if it's not an IP address
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            return "Error: Invalid hostname"
    else:
        # If it's a valid IP address, just assign it
        target_ip = target

    open_ports = []

    # Scan the range of ports
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        # Try connecting to the port
        result = sock.connect_ex((target_ip, port))
        if result == 0:  # Port is open
            open_ports.append(port)
        sock.close()

    # If verbose mode is enabled, return detailed information
    if verbose:
        if len(open_ports) > 0:
            output = f"Open ports for {target} ({target_ip})\nPORT     SERVICE\n"
            for port in open_ports:
                service_name = PORTS.get(port, "unknown service")
                output += f"{port:<8} {service_name}\n"
            return output.strip()
        else:
            return f"Open ports for {target} ({target_ip})\nNo open ports found."
    else:
        return open_ports


if __name__ == "__main__":
    # Example test cases
    print(get_open_ports("scanme.nmap.org", [20, 80], True))
    print(get_open_ports("209.216.230.240", [440, 445], False))
    print(get_open_ports("www.stackoverflow.com", [79, 82], True))
    print(get_open_ports("invalid.url", [80, 85], True))
    print(get_open_ports("999.999.999.999", [80, 85], True))
