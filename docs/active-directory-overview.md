# Active Directory Overview

Active Directory (AD) is Microsoft's directory service for Windows domain networks. It provides centralized identity management, authentication, authorization, and policy enforcement for enterprise environments.

---

## What is Active Directory?

Active Directory enables organizations to centrally manage users, computers, groups, and other network resources.

Its primary functions include:

- **Authentication** – Verifying user identities before granting access.
- **Authorization** – Determining what authenticated users are permitted to access.
- **Directory Services** – Storing and organizing information about users, devices, and network resources.

---

## Why Active Directory is a Target

Because Active Directory manages nearly every resource within a Windows enterprise, it is one of the most valuable targets for attackers.

### Common Reasons

1. **Centralized Control** – A single system manages users, computers, and permissions.
2. **High Value** – Stores authentication credentials and security policies.
3. **Enterprise Adoption** – Used by the vast majority of medium and large organizations worldwide.

---

## Active Directory Attack Surface

| Attack Vector | Description |
|---------------|-------------|
| **LLMNR / NBT-NS** | Name resolution spoofing attacks used to capture NTLM credentials. |
| **SMB** | File-sharing protocol weaknesses and relay attacks. |
| **Kerberos** | Authentication protocol attacks such as Kerberoasting and AS-REP Roasting. |
| **LDAP** | Enumeration and directory service abuse. |
| **DNS** | Name resolution attacks and DNS spoofing. |
| **Group Policy (GPO)** | Misconfigurations that can lead to privilege escalation or persistence. |

---

## Active Directory Security Best Practices

Organizations should implement multiple layers of security to protect Active Directory.

### Recommended Practices

- **Least Privilege** – Grant users only the permissions they require.
- **Regular Auditing** – Continuously monitor for suspicious activity.
- **Patch Management** – Keep servers and clients updated with security patches.
- **Strong Authentication** – Enforce Multi-Factor Authentication (MFA) and strong password policies.
- **Network Segmentation** – Reduce the attack surface by isolating critical systems.
- **Security Monitoring** – Monitor authentication events, privilege changes, and unusual network activity.

---

## Key Learning Objectives

After studying Active Directory, you should understand:

- The purpose of Active Directory within enterprise networks.
- Core Active Directory services and components.
- Common attack vectors targeting Active Directory.
- Defensive strategies for securing Windows domains.
- The importance of continuous monitoring and security hardening.

---

## Further Reading

- **Microsoft Active Directory Documentation**  
  https://learn.microsoft.com/windows-server/identity/ad-ds/

- **MITRE ATT&CK – Enterprise Tactics**  
  https://attack.mitre.org/tactics/TA0004/

---

## Conclusion

Active Directory serves as the backbone of most Windows enterprise environments, making it a high-value target for attackers and a critical system for defenders to protect. Understanding its architecture, common attack vectors, and recommended security practices provides a strong foundation for both penetration testing and defensive security.

> **Note:** This documentation is intended for educational purposes and authorized security assessments conducted within controlled laboratory environments.

