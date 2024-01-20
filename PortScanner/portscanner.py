#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2: 
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("_" * 50)
print("Scanning target " +target)
print("Time started: " +str(datetime.now()))
print("_" * 50)

try: 
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt: 
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()

'''import argparse
import socket
from datetime import datetime

def scan(target, start_port, end_port):
    # Add a pretty banner
    print("_" * 50)
    print("Scanning target " + target)
    print("Time started: " + str(datetime.now()))
    print("_" * 50)

    try:
        for port in range(start_port, end_port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} is open")

    except KeyboardInterrupt:
        print("\nExiting program.")

    except (socket.gaierror, socket.error) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Port scanner.')
    parser.add_argument('target', type=str, help='Target IP address')
    parser.add_argument('start_port', type=int, help='Start port')
    parser.add_argument('end_port', type=int, help='End port')

    args = parser.parse_args()
    scan(args.target, args.start_port, args.end_port)'''
