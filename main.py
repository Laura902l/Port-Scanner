from port_scanner import get_open_ports

# Test cases
if __name__ == "__main__":
    print(get_open_ports("scanme.nmap.org", [20, 80], True))
    print(get_open_ports("209.216.230.240", [440, 445], False))
    print(get_open_ports("www.stackoverflow.com", [79, 82], True))
    print(get_open_ports("invalid.url", [80, 85], True))
    print(get_open_ports("999.999.999.999", [80, 85], True))
