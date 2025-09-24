# Script Obfuscator

**Script Obfuscator** is a universal Python-based tool to obfuscate any script file (`.py`, `.sh`, `.ps1`, `.bat`, etc.) using **Base64** or **Hexadecimal** encoding. It hides the original content and generates a loader that executes the script at runtime.  

This tool is perfect for educational purposes, learning obfuscation techniques, or protecting source code from casual reading.

---

## GitHub Repository

[https://github.com/The-xploit/Script_Obfuscator]

---

## Features

- Obfuscate **Python, Bash, PowerShell, and other scripts**.
- Two encoding options:
  - **Base64 encoding** (`base64_obfuscator.py`)
  - **Hex encoding** (`hex_obfuscator.py`)
- Automatically generates a **loader** to execute obfuscated content.
- Makes Bash scripts executable automatically.
- Simple CLI interface.

---

## Requirements

- Python 3.9 or higher
- Compatible with Linux, macOS, and Windows

---

## Download

Clone the repository:

```bash
git clone https://github.com/The-xploit/Script_Obfuscator.git
cd Script_Obfuscator
```

## Usage
Base64 Obfuscation
``` python3
python3 base64_obfuscator.py <input_file> -o <output_file>
```
Hexadecimal Obfuscation
``` python3
python3 hex_obfuscator.py <input_file> -o <output_file>
```

## Arguments

  <input_file>: The script you want to obfuscate (.py, .sh, .ps1, etc.)

  <output_file>: (Optional) Name of the output obfuscated file. Defaults to <input_file>.obf.

## Examples
1. Obfuscate a Python script with Base64
``` python3
python3 base64_obfuscator.py test.py -o test_obf.py
```
2. Obfuscate a Bash script with Hex
``` python3
python3 hex_obfuscator.py test.sh -o test_obf.sh
```
3. Obfuscate a PowerShell script with Base64
```python3
python3 base64_obfuscator.py script.ps1 -o script_obf.ps1
```
4. Obfuscate a Python script with Hex
```python3
python3 hex_obfuscator.py app.py -o app_obf.py
```

After running these commands, the output files will be obfuscated versions of the original scripts. Bash scripts will automatically be made executable.

## How it works

Reads the input file as raw bytes.

Encodes it in Base64 or Hexadecimal.

Generates a loader script:

Python: exec(base64.b64decode(...)) or exec(binascii.unhexlify(...))

Bash: echo ... | base64 --decode | bash or echo ... | xxd -r -p | bash

PowerShell: [System.Convert]::FromBase64String(...) | Invoke-Expression or [System.Convert]::FromHexString(...) | Invoke-Expression

For Bash, sets the output file as executable automatically.

## Disclaimer

This tool is intended for educational purposes and authorized experiments only. Do not use it for illegal or malicious activities.

Use responsibly and ethically.
