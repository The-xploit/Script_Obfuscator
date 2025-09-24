#!/usr/bin/python3

import argparse
import os
import sys

def obfuscate_file(input_file: str, output_file: str):
    if not os.path.isfile(input_file):
        print(f"Input file not found: {input_file}")
        return

    # Read file content as bytes
    with open(input_file, "rb") as f:
        content = f.read()

    # Encode as hex
    encoded_hex = content.hex()

    # Determine loader based on file extension
    ext = os.path.splitext(input_file)[1].lower()
    if ext == ".py":
        runner = f"""import binascii
exec(binascii.unhexlify('{encoded_hex}'))"""
    elif ext == ".sh":
        runner = f"""#!/bin/bash
echo '{encoded_hex}' | xxd -r -p | bash"""
    elif ext == ".ps1":
        runner = f"""# PowerShell obfuscated
$hex = '{encoded_hex}'
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromHexString($hex)) | Invoke-Expression"""
    else:
        # Generic: use Python loader
        runner = f"""import binascii
exec(binascii.unhexlify('{encoded_hex}'))"""

    # Write output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(runner)

    # Make executable if bash
    if ext == ".sh":
        os.chmod(output_file, 0o755)

    print(f"[+] Obfuscated file written to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Universal Script Obfuscator (Hex)")
    parser.add_argument("input", help="Input file (.py, .sh, .ps1, etc.)")
    parser.add_argument("-o", "--output", help="Output obfuscated file")
    args = parser.parse_args()

    output_file = args.output or (args.input + ".obf")
    obfuscate_file(args.input, output_file)

if __name__ == "__main__":
    main()
