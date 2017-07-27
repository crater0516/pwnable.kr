from pwn import *

def main () :
	USER = "col"
	HOST = "pwnable.kr"
	PORT = 2222
	PASS = "guest"
	s = ssh(USER, HOST, PORT, PASS)

	gad1 = "\xC8\xCE\xC5\x06"
	gad2 = "\xCC\xCE\xC5\x06"
	payload = gad1 * 4 + gad2

	r = s.process(["/home/col/col", payload])
	r.interactive()

if __name__ == "__main__" :
	main()
