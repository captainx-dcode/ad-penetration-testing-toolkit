# Active Directory Security Penetration Testing — Mimikatz

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## Overview

This project demonstrates an **Active Directory security penetration-testing scenario involving Mimikatz**.

The purpose of this module is to help understand how credential-related information can become exposed on compromised Windows systems and why protecting authentication material is important in Active Directory environments.

The Python component is intended to support the **educational demonstration and automation of the lab workflow**, while Mimikatz provides the underlying security-testing functionality.

> ** This project is intended strictly for educational purposes and authorized security assessments performed in controlled laboratory environments.**

---

## Learning Objectives

By completing this module, you will understand:

* **Active Directory credential security**
* **Windows authentication and credential storage**
* **The security role of Mimikatz**
* **How Python can support security-testing workflows**
* **Credential exposure risks on compromised systems**
* **Defensive controls for protecting authentication material**
* **The importance of least privilege and endpoint security**

---

## What Is Mimikatz?

**Mimikatz** is a Windows security research and penetration-testing tool that demonstrates techniques involving Windows authentication credentials and security mechanisms.

It has been widely used by security professionals to understand how attackers may attempt to obtain credential material after gaining access to a Windows system.

In an authorized lab, studying Mimikatz helps defenders understand:

1. How credential material can be exposed after system compromise.
2. Why administrative privileges must be carefully controlled.
3. How endpoint security controls can detect credential-access activity.
4. Why credential protection is an important part of Active Directory security.

---

## Demonstration Workflow

The general laboratory workflow is:

```text
┌─────────────────────┐
│  Active Directory   │
│      Environment    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Compromised Windows │
│       System        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Python Security     │
│      Script         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Mimikatz        │
│ Security Research   │
│      Utility        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Credential Security │
│    Demonstration    │
└─────────────────────┘
```

The exercise should be performed using **dedicated virtual machines and test accounts** rather than production credentials.

---

## Technologies Used

| Technology              | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| **Python**              | Security automation and lab workflow     |
| **Mimikatz**            | Windows credential-security research     |
| **Active Directory**    | Directory and authentication environment |
| **Windows Server**      | Domain Controller                        |
| **Windows Client**      | Test workstation                         |
| **VirtualBox / VMware** | Isolated laboratory environment          |

---

## Project Structure

```text
02-mimikatz/
│
├── README.md
├── src/
│   └── <python-security-script>.py
│
├── docs/
│   ├── mimikatz-explanation.md
│   ├── attack-methodology.md
│   └── mitigation-guide.md
│
└── examples/
    └── lab-setup-guide.md
```

---

## Installation

### Prerequisites

Before starting the laboratory exercise, prepare:

* **Python 3.6+**
* A Windows test workstation
* An Active Directory laboratory environment
* A dedicated test account
* Mimikatz for authorized security testing
* Administrator privileges where required by the laboratory exercise

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Python Demonstration

From the project directory:

```bash
python src/<python-security-script>.py
```

The exact command depends on the Python script included in the module.

> **Note:** Run the demonstration only against systems and accounts specifically created for the laboratory.

---

## Expected Demonstration

The exercise demonstrates the relationship between:

```text
Python Automation
       │
       ▼
Windows Security Context
       │
       ▼
Credential-Access Research
       │
       ▼
Mimikatz
       │
       ▼
Security Findings
       │
       ▼
Defensive Recommendations
```

The objective is **not simply to obtain credentials**, but to understand why credential exposure is possible and how defenders can prevent or detect it.

---

## Defensive Considerations

Organizations should implement multiple layers of protection against credential-access techniques.

### 1. Least Privilege

Limit administrative privileges and avoid using privileged accounts for routine activities.

### 2. Credential Protection

Enable Windows security features designed to protect credential material and reduce credential theft opportunities.

### 3. Endpoint Detection

Use endpoint security and EDR solutions to monitor suspicious credential-access behavior.

### 4. Privileged Account Management

Separate standard user accounts from privileged administrative accounts.

### 5. Strong Authentication

Use strong passwords and **Multi-Factor Authentication (MFA)** where supported.

### 6. Network Segmentation

Separate critical Active Directory infrastructure from ordinary workstation networks.

### 7. Monitoring

Monitor authentication activity, privilege escalation, suspicious process execution, and unusual access to security-sensitive Windows components.

---

## Ethical and Legal Use

This module is intended **only for educational purposes and authorized penetration testing**.

### DO

* Use dedicated virtual machines.
* Use fake or laboratory credentials.
* Test only systems you own or have explicit permission to assess.
* Take VM snapshots before testing.
* Document your findings.
* Apply the demonstrated techniques to improve defensive controls.

### DO NOT

* Test against production systems without authorization.
* Extract credentials belonging to other users.
* Use the techniques against public or third-party systems.
* Deploy the tools for unauthorized access.
* Use captured credentials outside the laboratory.

---

## Further Reading

### Mimikatz Resources

* **ParrotSec Mimikatz Repository**
  https://github.com/ParrotSec/mimikatz

* **Impacket Mimikatz Example**
  https://github.com/fortra/impacket/blob/master/examples/mimikatz.py

* **Mimikatz Download Repository**
  https://github.com/Mimikatz-Download

* **Mimikatz Official Website**
  https://mimikatz.org/

* **Varonis: What Is Mimikatz?**
  https://www.varonis.com/blog/what-is-mimikatz

### Active Directory Security

* **Microsoft Active Directory Documentation**
  https://learn.microsoft.com/windows-server/identity/ad-ds/

* **MITRE ATT&CK**
  https://attack.mitre.org/

---

## Key Takeaways

This module demonstrates an important principle in Active Directory security:

> **A compromised endpoint can become a source of valuable authentication information.**

Understanding tools such as Mimikatz allows penetration testers to identify credential-security weaknesses while helping defenders implement stronger protections.

The ultimate goal of the exercise is therefore **not credential theft itself, but understanding the attack path well enough to detect, prevent, and mitigate it.**

---

> **Security is a journey, not a destination. Use this toolkit responsibly.**
