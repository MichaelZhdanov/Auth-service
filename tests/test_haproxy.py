import subprocess
import os

def test_haproxy(file_path):
    try:
        result = subprocess.run(
            ["haproxy", "-c", "-f", file_path],
            capture_output=True
            text=True
        )
        if "Configuration file is valid" in result.stdout:
            print(f" Valid HAProxy config: {file_path}")
            return True
        else:
            print(f" Invalid HAProxy config: {file_path}")
            return False
    except FileNotFoundError:
        print("Error: HAProxy is not installed")

