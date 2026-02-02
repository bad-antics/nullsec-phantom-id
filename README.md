<div align="center">

# 👻 NullSec Phantom ID

[![Rust](https://img.shields.io/badge/Rust-1.75+-f85149?style=for-the-badge&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/License-GPL--3.0-3fb950?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-58a6ff?style=for-the-badge)](https://github.com/bad-antics/nullsec-phantom-id)

**Device Identity Spoofing & Evasion Framework**

*IMEI Modification • Device Fingerprinting • Baseband Tools • Anti-Tracking*

⚠️ **For authorized security research only. Modifying IMEI is illegal in many jurisdictions.**

</div>

---

## 🎯 Overview

NullSec Phantom ID is a comprehensive device identity evasion framework designed for security researchers and authorized red team operations. It provides tools for analyzing and modifying device identifiers to test tracking resistance and conduct authorized penetration testing.

## ⚡ Features

| Feature | Description |
|---------|-------------|
| 📱 **IMEI Analysis** | Decode, validate, generate IMEIs |
| 🔧 **Baseband Tools** | AT command interface, modem control |
| 🎭 **Device Fingerprinting** | Modify Android/iOS device profiles |
| 📡 **Radio Identity** | IMSI, ICCID manipulation tools |
| 🔒 **Anti-Tracking** | Evade device-based tracking systems |
| 🖥️ **Serial Spoofing** | Hardware serial number tools |

## 🛠️ Components

### 1. IMEI Toolkit
```bash
# Analyze IMEI structure
phantom-id imei analyze 353456789012345

# Validate IMEI checksum
phantom-id imei validate 353456789012345

# Generate valid IMEI for testing
phantom-id imei generate --manufacturer samsung --model s23

# Generate batch for research
phantom-id imei batch --count 100 --output imeis.txt
```

### 2. Device Profile Spoofing
```bash
# List available profiles
phantom-id profile list

# Apply Android profile
phantom-id profile apply android-pixel-8

# Apply iOS profile  
phantom-id profile apply ios-iphone-15

# Custom profile
phantom-id profile custom \
  --manufacturer "Samsung" \
  --model "SM-G998B" \
  --android-id "abc123def456"
```

### 3. Baseband Interface
```bash
# Connect to modem
phantom-id baseband connect /dev/ttyUSB0

# Send AT commands
phantom-id baseband at "AT+CGSN"

# Read current IMEI
phantom-id baseband read-imei

# Interactive mode
phantom-id baseband shell
```

### 4. Radio Identity Tools
```bash
# IMSI analysis
phantom-id radio imsi-decode 310260123456789

# ICCID generator
phantom-id radio iccid-generate --provider verizon

# Network identity scan
phantom-id radio scan
```

## 📦 Installation

```bash
# Build from source
cargo build --release

# Install
sudo cp target/release/phantom-id /usr/local/bin/
```

## 🔧 Supported Devices

### Android (Root Required)
- Qualcomm devices (via QPST/QFIL)
- MediaTek devices (via SP Flash Tool hooks)
- Samsung (via engineering modes)

### Modems
- Quectel EC25/EG25
- Sierra Wireless
- Huawei HiLink
- ZTE MF series

### Research Hardware
- Software Defined Radios (for analysis only)
- Baseband debug interfaces
- JTAG/SWD for modem chips

## ⚠️ Legal Disclaimer

This tool is provided for **authorized security research only**. 

- Modifying IMEI is **illegal** in most countries
- Use only on devices you own or have authorization to test
- This tool is for educational and research purposes
- The authors are not responsible for misuse

## 🔬 Research Applications

- Testing device tracking resistance
- Mobile forensics research
- Cellular network security assessment
- Anti-fraud system testing
- Device identity privacy research

---

<div align="center">

**[bad-antics](https://github.com/bad-antics)** • Part of [NullSec Linux](https://github.com/bad-antics/nullsec-linux)

</div>
