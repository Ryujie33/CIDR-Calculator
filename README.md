# 🛡️ Python Network Subnet Calculator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight, terminal-based tool for network engineers and penetration testers. It quickly calculates CIDR notation, wildcard masks, and usable host ranges from a given IP and Subnet Mask.

## ⚡ Features

- **CIDR Calculation:** Converts IP + Netmask (e.g., `255.255.255.0`) into CIDR notation (e.g., `/24`).
- **Deep Analysis:** Instantly calculates:
  - Network ID
  - Broadcast Address
  - Wildcard Mask (crucial for Cisco ACLs)
  - First & Last Usable IP Addresses
  - Total Count of Usable Hosts
- **Smart Input:** Uses `strict=False` logic, meaning you can input a specific host IP (e.g., `192.168.1.55`) and the tool will correctly find the network it belongs to.
- **Visual Feedback:** Color-coded terminal output for easy reading.

## 🚀 Installation & Usage

### 1. Prerequisites
Ensure you have Python 3 installed.
```bash
python --version

2. Run the Script
Navigate to the folder containing the script and run:

python cidr.py

📖 Example Output
 +-----------------------------------+
 |   Network CIDR Calculator v1.0    |
 +-----------------------------------+
       IP  +  MASK  =  NETWORK
Enter IP address: 10.0.0.5
Enter Subnet Mask (e.g., 255.255.255.0): 255.255.255.240
----------------------------------------
[+] Result (CIDR): 10.0.0.0/28
    Netmask:       255.255.255.240
    Wildcard:      0.0.0.15
    Broadcast:     10.0.0.15
    Host Range:    10.0.0.1 - 10.0.0.14
    Usable Hosts:  14
----------------------------------------

⚠️ Troubleshooting
Error: "The ampersand (&) character is not allowed" This is a PowerShell syntax error.

Fix: Do not drag and drop the file path if it adds an &. Simply type python subnet.py in the terminal.

Error: "ValueError: ... has host bits set"

Fix: The script handles this automatically now! It will calculate the network ID even if you provide a host IP.

📜 License
This project is open-source and available under the MIT License.