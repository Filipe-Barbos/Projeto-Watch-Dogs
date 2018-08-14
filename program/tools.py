import os
from . import computer

def shutdown():
	if computer.os() == "Windows":
		os.system("shutdown -s")
	elif computer.os() == "Linux":
		os.sytem("shutdown -h")
	else:
		print("Operational System not detected. Cannot able execute")
def reboot():
	if computer.os() == "Windows":
		os.system("shutdown -r")
	elif computer.os() == "Linux":
		os.system("shutdown -r")

	else:
		print("Operational System not detected. Cannot able execute")
