# Mitigation Guide for LLMNR and NBT-NS Attacks

This guide outlines practical defensive measures that organizations can implement to reduce the risk of LLMNR and NBT-NS poisoning attacks in Active Directory environments.

---

## Quick Reference

| Mitigation | Difficulty | Effectiveness |
|------------|------------|---------------|
| Disable LLMNR | Easy | ⭐⭐⭐⭐⭐ High |
| Disable NBT-NS | Easy | ⭐⭐⭐⭐⭐ High |
| Enable SMB Signing | Medium | ⭐⭐⭐⭐⭐ High |
| Strong Password Policy | Easy | ⭐⭐⭐ Medium |
| Network Segmentation | Medium | ⭐⭐⭐ Medium |
| Multi-Factor Authentication (MFA) | Medium | ⭐⭐⭐⭐⭐ Very High |

---

## 1. Disable LLMNR via Group Policy

**Difficulty:** Easy  
**Security Impact:** High

LLMNR should be disabled wherever possible because it is one of the primary protocols exploited during poisoning attacks.

### Steps

1. Open **Group Policy Management Console (GPMC)**.
2. Create or edit a **Group Policy Object (GPO)** linked to your domain.
3. Navigate to:

```
Computer Configuration
└── Policies
    └── Administrative Templates
        └── Network
            └── DNS Client
```

4. Open **Turn off multicast name resolution**.
5. Set the policy to **Enabled**.
6. Apply the policy.

### Update Group Policy

```powershell
gpupdate /force
```

---

## 2. Disable NetBIOS over TCP/IP

**Difficulty:** Medium  
**Security Impact:** High

NetBIOS should also be disabled to eliminate another legacy name resolution mechanism frequently abused by attackers.

### Option A — Disable via DHCP

Configure the DHCP server to distribute the following option:

| DHCP Option | Value |
|------------|-------|
| NetBIOS Node Type | `0x2` (Disable NetBIOS) |

### Option B — Disable via Registry

```powershell
Set-ItemProperty `
-Path "HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces" `
-Name "NetbiosOptions" `
-Value 2 -Force
```

---

## 3. Enable SMB Signing

**Difficulty:** Medium  
**Security Impact:** High

SMB signing helps prevent SMB relay attacks by ensuring the integrity and authenticity of SMB communications.

### Group Policy Path

```
Computer Configuration
└── Windows Settings
    └── Security Settings
        └── Local Policies
            └── Security Options
```

Enable:

- **Microsoft network client: Digitally sign communications (always)**
- **Microsoft network server: Digitally sign communications (always)**

---

## 4. Enforce Strong Password Policies

**Difficulty:** Easy  
**Security Impact:** Medium

Even if NTLM hashes are captured, strong passwords make offline cracking significantly more difficult.

### Recommended Policy

- Minimum **14-character** passwords
- Complexity requirements enabled
- Password history enabled
- Regular password rotation
- Lockout after repeated failed logins

---

## 5. Enable Multi-Factor Authentication (MFA)

**Difficulty:** Medium  
**Security Impact:** Very High

MFA significantly reduces the impact of stolen credentials by requiring an additional authentication factor.

Recommended solutions include:

- Microsoft Authenticator
- FIDO2 Security Keys
- Smart Cards
- Windows Hello for Business

---

## 6. Network Segmentation

**Difficulty:** Medium  
**Security Impact:** Medium

Limit broadcast traffic by separating critical systems into different VLANs or network segments.

Benefits include:

- Smaller broadcast domains
- Reduced lateral movement
- Better monitoring and containment
- Improved network security

---

## 7. Monitoring and Detection

Security teams should continuously monitor for suspicious LLMNR and NBT-NS activity.

Indicators include:

- Unusual LLMNR broadcasts
- Unexpected NBT-NS responses
- Rogue systems answering name resolution requests
- Large numbers of failed SMB authentication attempts

Useful monitoring tools include:

- Microsoft Defender for Endpoint
- Microsoft Sentinel
- Wireshark
- Zeek
- Wazuh
- Splunk

---

## 8. Defense in Depth

No single security control completely prevents LLMNR and NBT-NS poisoning attacks.

A layered defense should include:

- Disable legacy name resolution protocols
- Enable SMB Signing
- Strong password policies
- Multi-Factor Authentication
- Network segmentation
- Continuous monitoring and alerting
- Regular security awareness training

---

## Conclusion

Protecting Active Directory requires a proactive approach that combines secure configuration, continuous monitoring, and user awareness. By disabling unnecessary legacy protocols and implementing layered security controls, organizations can significantly reduce the risk of credential theft and lateral movement.

> **Reminder:** These recommendations are intended to strengthen security within authorized environments. Regularly review Group Policy settings and security baselines to ensure legacy protocols remain disabled and defensive controls remain effective.

