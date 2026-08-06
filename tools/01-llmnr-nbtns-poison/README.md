# 🔐 LLMNR/NBT-NS Poisoning Tool

## 📌 Overview

This tool demonstrates **LLMNR (Link-Local Multicast Name Resolution)** and **NBT-NS (NetBIOS Name Service)** poisoning attacks. It captures **NTLMv2 authentication hashes** from vulnerable Windows workstations on the local network.

## 🎯 What It Does

1. **Listens** for LLMNR (port **5355**) and NBT-NS (port **137**) requests.
2. **Spoofs** responses to redirect victims to the attacker's machine.
3. **Captures** NTLMv2 authentication hashes.
4. **Logs** captured hashes for offline cracking.

---

## 📁 Files

| File | Description |
|------|-------------|
| `ad_poisoning.py` | Technical Lesson version (Educational) |
| `NBT_final.py` | Lab version (CodeGrade submission) |

---

## 🚀 Usage

```bash
# Run the Technical Lesson script
cd src
sudo python3 ad_poisoning.py

# Run the Lab script
cd src
sudo python3 NBT_final.py
```

---

## 📊 Example Output

```text
[*] Starting hospital network LLMNR and NBT-NS poisoning script...
[*] Listening for LLMNR and NBT-NS requests...
[!] Detected request from 192.168.1.100 for: FILESERVER
[+] Spoofed response sent to 192.168.1.100
[+] Captured credentials saved to hospital_hashes.txt
```

---

## 🛡️ Mitigation Strategies

- Disable **LLMNR** and **NBT-NS** via Group Policy (most effective).
- Enable **SMB Signing** to prevent relay attacks.
- Implement **strong password policies** (14+ characters).
- Enable **Multi-Factor Authentication (MFA)**.
- Use **network segmentation** to limit broadcast domains.

---

## 📚 Documentation

- Attack Explanation
- Mitigation Guide

---

## ✅ CodeGrade Rubric

This tool passes all CodeGrade auto-tests:

- ✅ `INTERFACE` variable defined.
- ✅ `scapy.sniff()` called with the correct filter.
- ✅ `packet.haslayer()` checks for UDP and Raw packets.
- ✅ `scapy.send()` sends the spoofed response.

---

> ⚠️ **Remember:** Use only in controlled laboratory environments and with explicit authorization.

