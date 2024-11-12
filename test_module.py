import unittest
from port_scanner import get_open_ports

class TestPortScanner(unittest.TestCase):

    def test_valid_ip_single_port(self):
        result = get_open_ports("209.216.230.240", [80, 80], verbose=False)
        self.assertIsInstance(result, list)  # Expecting a list of open ports

    def test_valid_domain_single_port(self):
        result = get_open_ports("scanme.nmap.org", [22, 22], verbose=False)
        self.assertIsInstance(result, list)

    def test_invalid_hostname(self):
        result = get_open_ports("invalid.url", [80, 85], verbose=True)
        self.assertEqual(result, "Error: Invalid hostname")

    def test_invalid_ip(self):
        result = get_open_ports("999.999.999.999", [80, 85], verbose=True)
        self.assertEqual(result, "Error: Invalid IP address")

    def test_verbose_mode(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], verbose=True)
        self.assertTrue("Open ports for" in result)
        self.assertTrue("PORT     SERVICE" in result)
        self.assertTrue("ssh" in result)

    def test_multiple_ports(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], verbose=False)
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
