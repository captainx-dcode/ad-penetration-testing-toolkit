# LLMNR and NBT-NS Poisoning: A Detailed Explanation

## 1. Introduction

**Link-Local Multicast Name Resolution (LLMNR)** and **NetBIOS Name Service (NBT-NS)** are legacy Windows name resolution protocols. They are used when a standard **DNS** query cannot resolve a hostname.

For example, when a user attempts to access `\\fileserver` and DNS cannot locate the host, Windows broadcasts an **LLMNR** or **NBT-NS** request across the local network, asking whether any device knows the requested hostname.

---

## 2. The Vulnerability

In many Windows environments, **LLMNR** and **NBT-NS** are enabled by default.

This creates a security weakness because **any device on the local network can respond to these broadcast requests**, whether it is the legitimate host or not.

An attacker can exploit this behavior by running a tool such as **Responder** or the custom Python script in this repository to poison the name resolution process and impersonate the requested host.

---

## 3. Attack Process

### Step-by-Step Breakdown

| Step | Description |
|------|-------------|
| **1. Initial Access** | The attacker gains access to the internal network. |
| **2. Listening** | The attacker's script waits for LLMNR and NBT-NS broadcast requests. |
| **3. Trigger** | A victim attempts to access a hostname that cannot be resolved through DNS. |
| **4. Spoofing** | The attacker responds first, pretending to be the requested host. |
| **5. Authentication** | The victim automatically attempts NTLM authentication with the attacker's machine. |
| **6. Credential Capture** | The NTLMv2 challenge-response hash is captured. |
| **7. Offline Cracking** | The captured hash can be cracked offline using tools such as Hashcat or John the Ripper. |

---

## 4. Why This Attack Works

| Factor | Explanation |
|--------|-------------|
| **Default Configuration** | LLMNR and NBT-NS are enabled on many Windows systems by default. |
| **Broadcast Protocols** | Broadcast traffic can be intercepted and answered by any host on the local network. |
| **No Authentication** | The protocols do not verify the identity of the responding system. |
| **NTLM Authentication** | Captured NTLM hashes can often be cracked offline if passwords are weak. |

---

## 5. Real-World Examples

### Case Study 1: FinCore Bank (Financial Industry)

**Attack Path**

LLMNR Poisoning → NTLMv2 Hash Capture → Hashcat Cracking → Domain Administrator

**Impact**

- Full Active Directory compromise
- Credential theft
- Privilege escalation

**Remediation**

- Disabled LLMNR
- Implemented network segmentation
- Rotated compromised passwords

---

### Case Study 2: MediCare Analytics (Healthcare)

**Attack Path**

IPv6 Misconfiguration → mitm6 + Responder → Credential Capture

**Impact**

- Potential exposure of patient information
- Increased risk of lateral movement

**Remediation**

- Disabled unnecessary IPv6 features
- Applied stricter Group Policy configurations

---

### Case Study 3: Skyline Studios (Media & Entertainment)

**Attack Path**

Phishing → SMB Relay → BloodHound Enumeration → Privilege Escalation

**Impact**

- Access to confidential production assets
- Excessive privilege abuse

**Remediation**

- Restructured Active Directory permissions
- Applied the Principle of Least Privilege

---

## 6. Mitigation Strategies

The following defensive controls significantly reduce the effectiveness of LLMNR and NBT-NS poisoning attacks:

- Disable **LLMNR** and **NBT-NS** through Group Policy.
- Enable **SMB Signing** to prevent relay attacks.
- Enforce strong password policies (12+ characters minimum).
- Enable **Multi-Factor Authentication (MFA)**.
- Implement network segmentation to reduce broadcast traffic.
- Monitor for unexpected **LLMNR** and **NBT-NS** traffic, as it may indicate misconfiguration or malicious activity.

---

## 7. Further Reading

- **MITRE ATT&CK:** LLMNR/NBT-NS Poisoning (T1557.001)  
  https://attack.mitre.org/techniques/T1557/001/

- **Microsoft Documentation:** Disabling LLMNR  
  https://learn.microsoft.com/windows-server/networking/

- **Responder**  
  https://github.com/lgandx/Responder

- **Hashcat**  
  https://hashcat.net/hashcat/

---

> **Note:** This documentation is intended strictly for educational purposes and authorized security assessments performed within controlled laboratory environments.
