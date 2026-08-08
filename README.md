# Active Directory Penetration Testing Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tools: 1](https://img.shields.io/badge/tools-1-green.svg)](https://github.com/yourusername/ad-penetration-testing-toolkit)

---

## Overview

**Active Directory Penetration Testing Toolkit** is a comprehensive collection of Python scripts and documentation for simulating and understanding common **Active Directory attack vectors**. Each tool is designed for **educational purposes** and **authorized security testing** in controlled environments.

---

## IMPORTANT: Ethical Use

This toolkit is for **educational and authorized security testing only**.

### You Should

* **DO** use in your own lab environments.
* **DO** use with explicit written permission.

### You Should Not

* **DO NOT** use on production systems without authorization.
* **DO NOT** use for malicious purposes.

> **The author assumes NO responsibility for any misuse of this code.**

---

## Tool Suite

### Current Tools

| #      | Attack Vector                    | Tool              | Description                                        | Status     |
| ------ | -------------------------------- | ----------------- | -------------------------------------------------- | ---------- |
| **01** | **LLMNR/NBT-NS Poisoning**       | `ad_poisoning.py` | Capture NTLMv2 hashes via name resolution spoofing | ✅ Complete |
| **01** | **LLMNR/NBT-NS Poisoning (Lab)** | `NBT_final.py`    | Lab version for CodeGrade submission               | ✅ Complete |

### Planned Tools

| #      | Attack Vector                      | Status         |
| ------ | ---------------------------------- | -------------- |
| **02** | **SMB Relay Attacks**              | 🔜 Coming Soon |
| **03** | **IPv6 Attacks (mitm6)**           | 🔜 Coming Soon |
| **04** | **Passback Attacks**               | 🔜 Coming Soon |
| **05** | **Hash Capture (Responder Clone)** | 🔜 Coming Soon |
| **06** | **Reverse Shells**                 | 🔜 Coming Soon |
| **07** | **Post-Exploitation**              | 🔜 Coming Soon |

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/[YOUR_USERNAME]/ad-penetration-testing-toolkit.git
cd ad-penetration-testing-toolkit

# Create virtual environment (recommended)
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running a Tool

```bash
# LLMNR/NBT-NS Poisoning (Technical Lesson)
cd tools/01-llmnr-nbtns-poison/src
sudo python3 ad_poisoning.py

# LLMNR/NBT-NS Poisoning (Lab)
cd tools/01-llmnr-nbtns-poison/src
sudo python3 NBT_final.py
```

---

## Project Structure

```text
ad-penetration-testing-toolkit/
│
├── README.md                          # Updated with both tools
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── tools/
│   │
│   ├── 01-llmnr-nbtns-poison/        # Part 1 (Complete)
│   │   ├── README.md
│   │   ├── src/
│   │   │   ├── ad_poisoning.py
│   │   │   └── NBT_final.py
│   │   └── docs/
│   │       ├── attack_explanation.md
│   │       └── mitigation_guide.md
│   │
│   └── 02-mimikatz-automation/       # Part 2 (Coming Soon)
│       ├── README.md
│       ├── src/
│       │   └── mimikatz_automation.py  # Your new script
│       └── docs/
│           ├── mimikatz_explanation.md
│           └── mimikatz_mitigation.md
│
├── docs/                              # Global documentation
│   ├── active-directory-overview.md
│   ├── attack-methodology.md
│   └── defense-best-practices.md
│
└── examples/
    └── lab-setup-guide.md
```

---

## How It Works

### LLMNR/NBT-NS Poisoning Attack Flow

```text
[Victim Windows PC]                    [Attacker Machine]

       |                                       |
       | 1. User types \\fileserver            |
       | 2. DNS lookup fails                   |
       | 3. Broadcasts LLMNR/NBT-NS query      |
       |-------------------------------------->|
       |                                       |
       |                      4. Spoofed response
       |                     "I am fileserver"
       |<--------------------------------------|
       |                                       |
       | 5. SMB authentication                 |
       |-------------------------------------->|
       |                                       |
       | 6. NTLMv2 hash captured               |
       |    and logged to file                 |
```

---

## Documentation

* **Active Directory Overview**
* **Attack Methodology**
* **Defense Best Practices**
* **Lab Setup Guide**

---

## Learning Outcomes

By using this toolkit, you will:

* Understand common **Active Directory attack vectors**.
* Simulate attacks in **controlled environments**.
* Develop **defensive strategies**.
* Build **Python skills for security automation**.

---

## Future Development

This toolkit is actively maintained and will include:

* □ SMB Relay Attacks
* □ IPv6 Attacks (mitm6)
* □ Passback Attacks
* □ Hash Capture (Responder Clone)
* □ Reverse Shells
* □ Post-Exploitation
* □ BloodHound Integration

---

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/amazing-tool
```

3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.


---

## Project Files

The repository includes the following supporting files:

* **`.gitignore`** — Excludes virtual environments, logs, captured hashes, IDE files, and other generated artifacts from version control.
* **`requirements.txt`** — Lists all required Python dependencies for the toolkit.
* **`LICENSE`** — Contains the MIT License governing the use and distribution of this project.

---

## License

Distributed under the **MIT License**. See the **LICENSE** file for more information.

---

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/amazing-tool
```

3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## Disclaimer

This toolkit is intended **strictly for educational purposes and authorized security testing** in controlled environments.

Never execute these techniques against systems without explicit written authorization.

---

> **Security is a journey, not a destination. Use this toolkit responsibly.**


**Commit:**
```bash
git add README.md
git commit -m "docs: add main README with project overview and tool suite"
git push origin main