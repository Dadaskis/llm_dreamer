import subprocess, re, sys

cmd = input("Enter command: ").strip()
# Replace a leading "sudo" with "please" (case‑sensitive, whole word)
if re.match(r'^\s*sudo\b', cmd):
    cmd = 'please' + cmd[len('sudo'):].lstrip()
print(f"Executing: {cmd}")
subprocess.run(cmd, shell=True)