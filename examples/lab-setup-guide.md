# Lab Setup Guide

This guide explains how to build a safe Active Directory lab environment for testing the LLMNR and NBT-NS poisoning tool included in this repository.

> **Important:** Perform all testing inside an isolated laboratory environment. Never test these techniques on production systems or networks without explicit authorization.

---

# Minimum Requirements

## Hardware

- Computer with **16 GB RAM or more**
- **50 GB** or more of available disk space
- Hardware virtualization (Intel VT-x / AMD-V) enabled

## Software

- VirtualBox or VMware Workstation
- Windows Server 2019 or 2022 ISO
- Windows 10 or Windows 11 ISO
- Kali Linux ISO

---

# Lab Architecture

```
                     Virtual NAT Network

        +-----------------------------------------------+

        +----------------+      +----------------+      +----------------+
        | Domain          |      | Windows        |      | Kali Linux     |
        | Controller      |----->| Workstation    |<---->| Attacker       |
        | Server 2022     |      | Windows 10/11 |      | Python Toolkit |
        +----------------+      +----------------+      +----------------+

```

---

# Setup Steps

## 1. Install VirtualBox

Download and install VirtualBox (or VMware Workstation) on your host machine.

---

## 2. Create the Domain Controller

Create a virtual machine using **Windows Server 2022**.

Configure the following:

- Install the **Active Directory Domain Services (AD DS)** role.
- Promote the server to a Domain Controller.
- Create the domain:

```
lab.local
```

Create several users for testing, for example:

- Administrator
- User1
- User2

---

## 3. Create the Windows Workstation

Create a Windows 10 or Windows 11 virtual machine.

Then:

- Join the machine to **lab.local**
- Restart the workstation
- Log in using a domain account

---

## 4. Create the Attacker Machine

Create a Kali Linux virtual machine.

Install:

- Python 3
- pip
- Git

Clone this repository onto the attacker machine.

---

## 5. Install Required Tools

```bash
sudo apt update

sudo apt install python3 python3-pip

pip install scapy impacket colorama
```

---

# Testing the Attack

## Step 1 — Start the Poisoning Tool

```bash
cd ad-penetration-testing-toolkit/tools/01-llmnr-nbtns-poison/src

sudo python3 ad_poisoning.py
```

---

## Step 2 — Trigger the Attack

From the Windows workstation:

1. Open **File Explorer**
2. Type:

```
\\nonexistentserver
```

3. Press **Enter**

Windows will attempt DNS resolution, fail, and broadcast an LLMNR/NBT-NS request.

---

## Step 3 — Capture the Hash

If the attack succeeds, the captured credentials will be written to:

```
hashes.txt
```

or

```
hospital_hashes.txt
```

depending on the script being executed.

---

# Safety Tips

Always follow safe testing practices:

- Use a **NAT** virtual network instead of a bridged network.
- Create VM snapshots before testing.
- Use only fake credentials.
- Never connect the lab to a production environment.
- Restore snapshots after completing experiments.

---

# Troubleshooting

## Scapy Permission Denied

Run the script with elevated privileges.

```bash
sudo python3 script.py
```

---

## Windows Is Not Broadcasting

Verify that LLMNR is enabled.

You can also manually trigger name resolution by entering:

```
\\nonexistentserver
```

or

```text
ping nonexistentserver
```

---

## No Hashes Captured

Check the following:

- LLMNR is enabled on the Windows workstation.

```powershell
Get-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient"
```

- Windows Defender or endpoint protection is not blocking the test.
- All virtual machines are connected to the same virtual network.
- Network connectivity between the attacker and victim is working correctly.

---

# Clean Up

Delete any generated hashes after testing.

```bash
rm hashes.txt

rm hospital_hashes.txt
```

It is also recommended to restore your virtual machine snapshots to return the lab to a clean state.

---

# Conclusion

This lab provides a safe environment for understanding how LLMNR and NBT-NS poisoning attacks work in Active Directory networks. By completing this setup, you can study both offensive techniques and the defensive controls used to detect and mitigate credential capture attacks.

> **Reminder:** This guide is intended strictly for educational purposes and authorized security assessments performed within isolated laboratory environments.

