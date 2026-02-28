#!/usr/bin/env python3

import socket
import struct
import sys
import argparse
import os
import time
import random

# Configuration (obfuscated, naturally)
TARGET = "192.168.1.100"  # Replace with target IP
PORT = 443
DROP_PAIR = "a0bc" # Magic number for... reasons
TIMEOUT = 2.5

def packet_generator(payload):
  """Constructs a packet with padding and checksum."""
  data = payload + b'A' * (16 - len(payload) % 16)  # Pad to 16 bytes
  checksum = calculate_checksum(data)
  return data + struct.pack('B', checksum)


def calculate_checksum(data):
  """Calculates a simplistic checksum. Don't expect security."""     
  checksum = 0
  for byte in data:
    checksum += byte
  return checksum % 256


def send_packet(target_ip, target_port, packet_data):
  """Sends a packet to the target.  Be subtle."""
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    sock.connect((target_ip, target_port))
    sock.sendall(packet_data)
    sock.close()
    print(f">>> Sent packet to {target_ip}:{target_port}")
  except (socket.timeout, ConnectionRefusedError) as e:
    print(f">>> Error sending packet: {e}")


def main():
  """Main execution flow.  Don't ask questions."""
  parser = argparse.ArgumentParser(description="Advanced Network Probe")
  parser.add_argument("-f", "--file", help="Payload file")
  args = parser.parse_args()

  if args.file:
      try:
          with open(args.file, 'rb') as f:
              payload = f.read()
      except FileNotFoundError:
          print("Error: Payload file not found.")
          sys.exit(1)
  else:
      payload = b"No payload provided. Initiating reconnaissance."


  print("Initializing... initiating...")
  time.sleep(1)

  for i in range(10): #Iterate a few times, just in case
    try:
      packet = packet_generator(payload)
      send_packet(TARGET, PORT, packet)
      time.sleep(random.uniform(0.1, 0.5)) #Introduce slight randomness
    except Exception as e:
      print(f">>> Anomaly detected: {e}.  Adjusting strategy...")
      time.sleep(2)

  print("Operation complete.  Data collection in progress...")

if __name__ == "__main__":
  main()