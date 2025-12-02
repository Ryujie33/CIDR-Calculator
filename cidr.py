import ipaddress
import sys

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    banner = f"""{Colors.BLUE}
 +-----------------------------------+
 |   Network CIDR Calculator v1.0    |
 +-----------------------------------+
       IP  +  MASK  =  NETWORK
    {Colors.ENDC}"""
    print(banner)

def calculate_network_details():
    print_banner()
    
    try:
        # Prompt the user
        ip_input = input(f"{Colors.BOLD}Enter IP address: {Colors.ENDC}").strip()
        mask_input = input(f"{Colors.BOLD}Enter Subnet Mask (e.g., 255.255.255.0): {Colors.ENDC}").strip()
        
        print("-" * 40)

        # Create the network object
        # The ipaddress library is smart enough to handle "IP/Mask" string format
        # strict=False allows passing a host IP (e.g. 192.168.1.5) and getting the network containing it
        network = ipaddress.IPv4Network(f"{ip_input}/{mask_input}", strict=False)

        # Calculations
        cidr_notation = str(network)
        netmask = str(network.netmask)
        wildcard = str(network.hostmask)
        total_ips = network.num_addresses
        
        # Calculate usable hosts (Total - Network Address - Broadcast Address)
        # Exception: /31 and /32 networks are edge cases
        usable_hosts = total_ips - 2 if total_ips > 2 else 0
        
        # Get first and last IP
        if total_ips > 1:
            first_ip = str(network.network_address + 1)
            last_ip = str(network.broadcast_address - 1)
            broadcast = str(network.broadcast_address)
        else:
            first_ip = "N/A"
            last_ip = "N/A"
            broadcast = "N/A"

        # Output Results
        print(f"{Colors.GREEN}[+] Result (CIDR): {cidr_notation}{Colors.ENDC}")
        print(f"    Netmask:       {netmask}")
        print(f"    Wildcard:      {wildcard}")
        print(f"    Broadcast:     {broadcast}")
        print(f"    Host Range:    {first_ip} - {last_ip}")
        print(f"    Usable Hosts:  {usable_hosts}")
        print("-" * 40)

    except ValueError as e:
        print(f"\n{Colors.FAIL}[!] Error: Invalid IP or Subnet Mask format.{Colors.ENDC}")
        print(f"{Colors.WARNING}Details: {e}{Colors.ENDC}")
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}\n[!] Operation cancelled by user.{Colors.ENDC}")
        sys.exit()
    except Exception as e:
        print(f"\n{Colors.FAIL}[!] An unexpected error occurred: {e}{Colors.ENDC}")

if __name__ == "__main__":
    calculate_network_details()