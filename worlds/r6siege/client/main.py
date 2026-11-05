import subprocess
import sys

try:
    connection_information = subprocess.run([sys.executable, "app\\connection_screen.py"],
                                             capture_output = True, text = True, check = True)
except subprocess.CalledProcessError:
    exit()

connection_information_output = connection_information.stdout.strip().split()
host = connection_information_output[0]
port = connection_information_output[1]
slot = connection_information_output[2]

subprocess.run([sys.executable, "app\\operator_screen.py", host, port, slot])