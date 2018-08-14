from program import computer, cpu, memory, tools, disks, network
import sys

# Get arguments from terminal
params = sys.argv

# Checks if was send any param
if len(params) > 1:
	if params[1] == "-os" or params[1] == "-operationalsystem":
		print("Operational System: ", computer.os())
		print("Version: ", computer.osVersion())

	elif params[1] == "-n" or params[1] == "-name":
		print("Network Name (Node): ", computer.name())

	elif params[1] == "-d" or params[1] == "-distro":
		print("Distribution: ", computer.distro())

	elif params[1] == "-p" or params[1] == "-processor":
		if len(params) == 4 and params[2] == "--pe" or params[2] == "--percentage" and int(params[3]) >= 1:
			for x in range(int(params[3])):
				consume = cpu.percentage()
				print("Using: ", consume.user + consume.system, "%")
				print("Free: ", consume.idle, "%")
				print("############################")
		elif len(params) == 4 and params[2] == "--b" or params[2] == "--benchmarking " and int(params[3]) >= 1:
			avg = 0
			print("Analysing CPU use...")
			for x in range(int(params[3])):
				consume = cpu.percentage()
				avg += consume.user + consume.system
			avg = avg/int(params[3])
			print("Use average during:", params[3], " seconds: ", round(avg,1), "%")
		else:
			print("CPU (Processor): ", computer.cpu())
			print("Velocity: ", cpu.freq(), "GHz")
			print("Cores: ", cpu.cores())
			print("Physical Cores: ", cpu.phyCores())

	elif params[1] == "-m" or params[1] == "-memory":
		if str(params).find("--s") > 0 or str(params).find("--size") > 0:
			print("Memory size:", memory.size(), "GBs")
		if str(params).find("--pe") > 0 or str(params).find("--percentage") > 0:
			print("Memory percentage:", memory.percentage(), "%")
		if str(params).find("--f") > 0 or str(params).find("--free") > 0:
			print("Memory free:", memory.free(), "GBs")
		if str(params).find("--u") > 0 or str(params).find("--used") > 0:
			print("Memory used:", memory.used(), "GBs")

	elif params[1] == "-di" or params[1] == "-disks":
		if str(params).find("--i") > 0 or str(params).find("--info") > 0:
			disksList = disks.info()
			i = 0
			print("Number of disks:", len(disksList))
			while i < len(disksList):
				print("#########################")
				print("Mount point: ", disksList[i].mountpoint)
				print("Filesytem type: ", disksList[i].fstype)
				i += 1

	elif params[1] == "-ne" or params[1] == "-network":
		if str(params).find("--b") > 0 or str(params).find("--bytes") > 0:
			bytesNetwork = network.info()
			print("Bytes sent: ", round(bytesNetwork.bytes_sent/(1024**3),2), "GBs")
			print("Bytes received: ", round(bytesNetwork.bytes_recv/(1024**3),2), "GBs")
		if str(params).find("--p") > 0 or str(params).find("--packet") > 0:
			packatesNetwork = network.info()
			print("Packets sent: ", packatesNetwork.packets_sent)
			print("Packets received: ", packatesNetwork.packets_recv)

	elif params[1] == "-a" or params[1] == "-architeture":
		print("Architeture: ", computer.arch())

	elif params[1] == "-s" or params[1] == "-shutdown":
		print("Shutting down...")
		tools.shutdown()

	elif params[1] == "-r" or params[1] == "-reboot":
		print("Rebooting...")
		tools.reboot()
	else:
		print("Param invalid. Please try again")
else:
	print("############################# HELP / COMMANDS #############################")
	print("#                                                                         #")
	print("########################### OPERATIONAL SYSTEM ############################")
	print("# -os (-operationalsystem) --> Show operational system and version        #")
	print("#                                                                         #")
	print("############################# NETWORK NAME ################################")
	print("# -n (-name) --> Show network name (node)                                 #")
	print("#                                                                         #")
	print("############################# DISTRIBUTION ################################")
	print("# -d (-distro) --> Show distribution                                      #")
	print("#                                                                         #")
	print("############################## PROCESSOR ##################################")
	print("# -p (-processor) -->                                                     #")
	print("# 	--pe (--percentage) --> Show processor percentage                 #")
	print("# 	--b (--benchmarking) --> Show processor benchmarking              #")
	print("#                                                                         #")
	print("############################### MEMORY ####################################")
	print("# -m (-memory) -->                                                        #")
	print("# 	--s (--size) --> Show memory size                                 #")
	print("# 	--pe (--percentage) --> Show memory percentage                    #")
	print("# 	--f (--free) --> Show free memory                                 #") 
	print("# 	--u (--used) --> Show used memory                                 #")
	print("#                                                                         #")
	print("############################### DISKS #####################################")
	print("# -d (-disks) -->                                                         #")
	print("# 	--i (--info) --> Show disks                                       #")
	print("#                                                                         #")
	print("############################## NETWORK ####################################")
	print("# -ne (-network) -->                                                      #")
	print("# 	--b (--bytes) --> Show network bytes                              #")
	print("# 	--p (--packet) --> Show network packet                            #")
	print("#                                                                         #")
	print("############################ ARCHITETURE ##################################")
	print("# -a (-architeture) --> Show architeture                                  #")
	print("#                                                                         #")
	print("############################## SHUTDOWN ###################################")
	print("# -s (-shutdown) --> Shutdown the system                                  #")
	print("#                                                                         #")
	print("############################### REBOOT ####################################")
	print("# -r (-reboot) --> Reboot the system                                      #")
	print("#                                                                         #")
	print("###########################################################################")