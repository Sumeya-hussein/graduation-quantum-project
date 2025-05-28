# RSA-32 & Quantum Attack Demo

## Description
This project provides a complete end-to-end demonstration of how a toy **32-bit RSA** implementation can be used for “secure” messaging between two classical endpoints (Alice ↔ Bob), then broken by **Shor’s quantum factoring algorithm**. It also shows why **Quantum Key Distribution (QKD)** is the only truly future-proof key exchange method in the face of scalable quantum computers.

---

## Features
- **Classical RSA-32 pipeline**  
  - 16-bit prime generation & 32-bit keypair  
  - Message padding, encryption & decryption  
- **Secure channel simulation**  
  - Alice encrypts `HELLO BOB!`, Bob decrypts it  
- **Quantum payload preparation**  
  - Export public modulus & ciphertext for attack  
- **Shor’s algorithm demo**  
  - Factors `N = 15` on a local simulator  
  - Hardware-ready hook for 32-bit modulus  
- **Reproducible environment**  
  - Python 3.8 virtualenv  
  - Qiskit 0.25.0 + Terra 0.17.0, Aer 0.8.0, Aqua 0.9.0, Ignis 0.6.0, IBMQ-Provider 0.12.2

---

## Prerequisites
- **System Python 3.x** (for classical demos)  
- **Python 3.8** (for quantum demo)  
  *Install via your OS package manager or the deadsnakes PPA on Ubuntu*  
- **Git** (to clone the repo)

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/rsa32-shor-attack-simulation.git
   cd rsa32-shor-attack-simulation
2. Classical demo dependencies
    No external packages required beyond the Python standard library.

3. ## Set up the quantum demo environment

**Create & activate Python 3.8 venv**
python3.8 -m venv qkd-legacy
source qkd-legacy/bin/activate

**Upgrade pip and install pinned Qiskit stack**
pip install --upgrade pip
pip install -r requirements_legacy.txt --use-deprecated=legacy-resolver

Usage
Classical RSA-32 Demo

# Generate keys, encrypt & decrypt a sample message
python rsa32.py

# Simulate Alice → Bob messaging
python communication.py

# Prepare quantum attack payload
python quantum_payload.py

Quantum Attack Demo

# With the qkd-legacy venv active:
python shor_attack.py

# (Optional) Uncomment the real-modulus hook in shor_attack.py
# then re-run to observe simulator limits.
deactivate

Project Structure

rsa32-shor-attack-simulation/
├── rsa32.py                 # Classical RSA-32 implementation
├── communication.py         # Alice↔Bob secure channel simulation
├── quantum_payload.py       # Exports public modulus & ciphertext
├── shor_attack.py           # Shor’s algorithm demo (N=15)
├── requirements_legacy.txt  # Qiskit 0.25.0 environment pins
└── README.md                # Project overview & instructions

Configuration & Presets

    Python interpreter paths

        python → your system’s Python 3.x for RSA scripts

        qkd-legacy/bin/python → Python 3.8 inside the quantum venv

    Pinned dependencies in requirements_legacy.txt ensure reproducibility:

    qiskit==0.25.0
    qiskit-terra==0.17.0
    qiskit-aer==0.8.0
    qiskit-ignis==0.6.0
    qiskit-ibmq-provider==0.12.2
    qiskit-aqua==0.9.0

    Padding block size is set to 4 bytes in rsa32.py (adjustable as needed).

Author

Sumaya Hussein Ismail
